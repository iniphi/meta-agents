#!/usr/bin/env python3
"""check_agent.py - conformance check over the traces a meta-agent install leaves.

Usage:
    python check_agent.py <root> [--charter F] [--start F] [--state F] [--direction F]

<root> is the folder holding the install (the context-system folder). The
pages are looked up in the usual places unless you name them. Standard
library only; one file, so it can be fetched on its own.

It prints one PASS, FAIL or SKIP line per check and exits 1 if any check
FAILED. SKIP means a check could not run because an earlier one failed.
It checks that the traces exist, have content and agree with each other. It
cannot tell whether the content is wise, true or well chosen: that stays
with the owner (see stages/7-verify.md, "What this cannot tell").
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Callable

PARTS = ["Identity", "Mandate", "Owned spine", "Scope boundaries", "Sharp test"]
DEFAULTS = {
    "charter": ["context/charter.md", "charter.md"],
    "start": [".claude/skills/start/SKILL.md", "start.md"],
    "state": ["context/state.md", "state.md"],
    "direction": ["context/direction.md", "direction.md"],
}
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NEGATION = re.compile(r"\b(not|never|no|nobody|neither|cannot|without)\b|n't")
FREE_EDIT = re.compile(r"\b(any|every|each) session (may|can) (edit|change|rewrite)"
                       r"|\b(may|can) edit (this|the) (page|charter)|edit (this page|the charter) freely")
VAGUE_END = re.compile(r"^(as|when|whenever|if|any ?time)\b.*\b(needed|necessary|required|appropriate|useful|relevant)$")
REVIEW_RE = re.compile(r"\breview\w*\W+(?:\w+\W+){0,2}?(\d{4}-\d{2}-\d{2})", re.I)
Result = tuple["bool | None", str]


def read(path: Path | None) -> str | None:
    # utf-8-sig: a byte-order mark before a first-line heading would hide that heading.
    return path.read_text(encoding="utf-8-sig") if path is not None and path.is_file() else None


def find(root: Path, kind: str, given: str | None) -> Path | None:
    if given:
        return Path(given) if Path(given).is_absolute() else root / given
    return next((root / r for r in DEFAULTS[kind] if (root / r).is_file()), None)


def split_sections(text: str, marker: str) -> list[tuple[str, str]]:
    """Split on lines starting with `marker` + space, ignoring fenced code."""
    out: list[tuple[str, list[str]]] = []
    fenced = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith(marker + " "):
            out.append((line[len(marker) + 1:].strip(), []))
        elif out:
            out[-1][1].append(line)
    return [(t, "\n".join(b)) for t, b in out]


def title_is(title: str, name: str) -> bool:
    t = title.lower().strip()
    return t == name.lower() or t.startswith(name.lower() + " (")


def section(text: str, name: str, marker: str = "##") -> str | None:
    return next((b for t, b in split_sections(text, marker) if title_is(t, name)), None)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", s)).strip().lower().rstrip(".;:")


def real_text(body: str | None) -> str:
    """Body without comments, headings and <placeholder> tokens."""
    if not body:
        return ""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = "\n".join(ln for ln in body.splitlines() if not ln.lstrip().startswith("#"))
    return re.sub(r"<[^>\n]*>", "", body).strip()


def words(s: str) -> int:
    return len(re.findall(r"\w+", s))


def first_line(body: str | None) -> str | None:
    for ln in real_text(body).splitlines():
        if ln.strip():
            return norm(ln)
    return None


def tools_of(charter: str) -> list[tuple[str, str]] | None:
    body = section(charter, "Toolset")
    return None if body is None else [(norm(t), b) for t, b in split_sections(body, "###")]


def identity_split(start: str | None) -> tuple[str, str] | None:
    """(text before the Agent Identity heading, the block) or None."""
    if start is None:
        return None
    lines = start.splitlines(keepends=True)
    fenced, head, end = False, None, len(lines)
    for i, ln in enumerate(lines):
        if ln.strip().startswith("```"):
            fenced = not fenced
        if fenced:
            continue
        if head is None and re.match(r"## Agent Identity\b", ln):
            head = i
        elif head is not None and ln.startswith("## "):
            end = i
            break
    if head is None:
        return None
    return "".join(lines[:head]), "".join(lines[head + 1:end])


def field(block: str, name: str) -> str | None:
    pat = re.compile(r"^[\s\-*>]*\**" + re.escape(name) + r"\**\s*:\s*(.+)$", re.I)
    return next((norm(m.group(1)) for ln in block.splitlines() if (m := pat.match(ln))), None)


class Ctx:
    def __init__(self, root: Path, a: argparse.Namespace) -> None:
        self.paths = {k: find(root, k, getattr(a, k)) for k in DEFAULTS}
        self.text = {k: read(p) for k, p in self.paths.items()}
        self.charter = self.text["charter"]
        self.ident = identity_split(self.text["start"])


def need_charter(c: Ctx) -> Result | None:
    return None if c.charter is not None else (None, "needs the charter, which is missing")


def chk_charter_exists(c: Ctx) -> Result:
    if c.charter is None:
        return False, "no charter found (looked for context/charter.md, charter.md)"
    return True, f"found {c.paths['charter'].name}"


def chk_headings(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    titles = [t for t, _ in split_sections(c.charter, "##")]
    missing = [p for p in PARTS if not any(title_is(t, p) for t in titles)]
    return (False, "missing heading(s): " + ", ".join(missing)) if missing else (True, "all five headings present")


def chk_filled(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    empty = []
    for p in PARTS:
        body = section(c.charter, p)
        if body is None:
            continue  # a missing heading is the previous check's failure
        if p == "Scope boundaries":
            for sub in ("In scope", "Not mine"):
                if words(real_text(section(body, sub, "###"))) < 3:
                    empty.append(f"{p} / {sub}")
        elif words(real_text(body)) < 3:
            empty.append(p)
    return (False, "no real content under: " + ", ".join(empty)) if empty else (True, "every part has content")


def chk_change_rule(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    body = section(c.charter, "Change rule")
    if body is None:
        return False, "no 'Change rule' heading"
    flat = norm(body)
    sents = re.split(r"(?<=[.!?;])\s+|,\s*|\s+(?:and|but)\s+", flat)
    stated = lambda phrase: any(phrase in s and not NEGATION.search(s) for s in sents)
    missing = [m for m, p in (("'a session may propose'", "may propose"), ("'only the owner'", "only the owner")) if not stated(p)]
    if missing:
        return False, "change rule lacks an unnegated sentence with " + " and ".join(missing)
    if FREE_EDIT.search(flat):
        return False, "change rule lets sessions edit the charter"
    return True, "change rule: sessions may propose, only the owner changes"


def chk_season(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    body = section(c.charter, "Current season")
    if body is None:
        return False, "no 'Current season' heading"
    found = DATE_RE.findall(body)
    if not found:
        return False, "current season carries no YYYY-MM-DD date"
    try:
        dates = [date.fromisoformat(d) for d in found]
    except ValueError:
        return False, "current season has a date that is not a real calendar date"
    m = REVIEW_RE.search(body)
    if not m:
        return False, "current season has no review date (write 'review by YYYY-MM-DD')"
    rest = DATE_RE.findall(body[:m.start(1)] + body[m.end(1):])
    if not rest:
        return False, "current season has a review date but no date it was set"
    if date.fromisoformat(m.group(1)) < date.fromisoformat(rest[0]):
        return False, "review-by date is before the date the season was set"
    return True, "current season has a set date and a review date"


def chk_toolset(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    tools = tools_of(c.charter)
    if tools is None:
        return False, "no section titled exactly 'Toolset'"
    if not tools:
        return False, "Toolset names no tools (one ### heading per tool)"
    return True, f"{len(tools)} tool(s) declared"


def runs_when_ok(value: str) -> bool:
    v = norm(re.sub(r"<[^>]*>", "", value))
    return words(v) >= 3 and not VAGUE_END.match(v)


def chk_runs_when(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    tools = tools_of(c.charter)
    if not tools:
        return None, "needs declared tools"
    pat = re.compile(r"^[\s\-*]*\**runs when\**\s*:\s*(.*)$", re.I)
    bad = [n for n, b in tools if not any((m := pat.match(ln)) and runs_when_ok(m.group(1)) for ln in b.splitlines())]
    if bad:
        return False, "no usable 'Runs when:' line (a trigger in 3+ words, not 'as needed') for: " + ", ".join(bad)
    return True, "every tool has a usable 'Runs when:' line"


def chk_for_sign(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    tools = tools_of(c.charter)
    if not tools:
        return None, "needs declared tools"
    problems = []
    for name, body in tools:
        miss = [lab for lab, key in (("For:", "for"), ("Sign it ran:", "sign it ran"))
                if not any(words(real_text(m.group(1))) >= 3 for ln in body.splitlines()
                           if (m := re.match(r"^[\s\-*]*\**" + key + r"\**\s*:\s*(.*)$", ln, re.I)))]
        if miss:
            problems.append(f"{name} (no {' or '.join(miss)})")
    if problems:
        return False, "tool(s) missing a 'For:' or 'Sign it ran:' line of 3+ words: " + "; ".join(problems)
    return True, "every tool says what it is for and how to tell it ran"


def chk_ratified(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    lines = [ln for ln in c.charter.splitlines() if re.search(r"\bratif", ln, re.I)]
    if any(re.search(r"\b(not|un)[- ]?ratified|\bnot yet ratified", ln, re.I) for ln in lines):
        return False, "the charter says it is not ratified"
    for ln in lines:
        for d in DATE_RE.findall(ln):
            try:
                date.fromisoformat(d)
                return True, f"ratification line carries the date {d}"
            except ValueError:
                pass
    return False, "no line says the charter was ratified with a real YYYY-MM-DD date"


def chk_identity_block(c: Ctx) -> Result:
    if c.ident is None:
        return False, "start routine missing, or has no '## Agent Identity' block"
    before = re.sub(r"\A---\n.*?\n---\n", "", c.ident[0], flags=re.S)
    steps = [ln for ln in before.splitlines() if re.match(r"\s*(\d+[.)]|[-*])\s+\S", ln)]
    if words(real_text(before)) < 15 or len(steps) < 2:
        return False, "identity block must follow the start routine's own steps (15+ words and 2+ list items before it)"
    return True, "identity block sits after the start routine's own steps"


def first_sentence(body: str | None) -> str | None:
    paras = [p for p in re.split(r"\n\s*\n", real_text(body)) if p.strip()]
    if not paras:
        return None
    return norm(re.split(r"(?<=[.!?])\s+", " ".join(paras[0].split()))[0])


def _same(c: Ctx, name: str, part: str, pick: Callable[[str | None], str | None] = first_line, what: str = "first line") -> Result:
    if (r := need_charter(c)):
        return r
    if c.ident is None:
        return None, "needs the identity block, which is missing"
    mine, theirs = field(c.ident[1], name), pick(section(c.charter, part))
    if mine is None:
        return False, f"identity block has no '{name}:' line"
    if theirs is None:
        return False, f"charter '{part}' has no {what}"
    return (True, f"identity {name.lower()} matches the charter") if mine == theirs else (False, f"identity '{name}' differs from the charter's {what}")


def chk_id_identity(c: Ctx) -> Result:
    return _same(c, "Identity", "Identity", first_sentence, "first sentence")


def chk_id_mandate(c: Ctx) -> Result:
    return _same(c, "Mandate", "Mandate")


def chk_id_sharp(c: Ctx) -> Result:
    return _same(c, "Sharp test", "Sharp test")


def chk_id_toolset(c: Ctx) -> Result:
    if (r := need_charter(c)):
        return r
    tools = tools_of(c.charter)
    if c.ident is None or not tools:
        return None, "needs the identity block and declared tools"
    line = field(c.ident[1], "Toolset")
    if line is None:
        return False, "identity block has no 'Toolset:' line"
    mine, theirs = [norm(t) for t in re.split(r"[,;]", line) if t.strip()], [n for n, _ in tools]
    dup = sorted({n for n in mine + [] if mine.count(n) > 1} | {n for n in theirs if theirs.count(n) > 1})
    if dup:
        return False, "tool named twice: " + ", ".join(dup)
    if sorted(mine) != sorted(theirs):
        return False, "toolset names differ: " + ", ".join(sorted(set(mine) ^ set(theirs)))
    return True, "identity toolset names match the charter, each once"


def chk_direction(c: Ctx) -> Result:
    d, s = c.text["direction"], c.text["state"]
    if d is None:
        return False, "no direction page found (looked for context/direction.md, direction.md)"
    if c.paths["state"] and c.paths["direction"].resolve() == c.paths["state"].resolve():
        return False, "the direction page is the state page"
    heads = [("End state", "end state"), ("Done test", "done test")]
    for label, key in heads:
        body = next((b for t, b in split_sections(d, "##") if re.match(key.replace(" ", "[- ]?"), t.lower())), None)
        if words(real_text(body)) < 3:
            return False, f"direction page has no real content under '{label}'"
    if s is not None:
        if norm(s) == norm(d) or any(re.match(k.replace(" ", "[- ]?"), t.lower()) for t, _ in split_sections(s, "##") for _, k in heads):
            return False, "the state page holds the same content, or an End state / Done test of its own"
    return True, "direction page has an end state and done test, apart from the state page"


CHECKS = [
    ("charter-exists", chk_charter_exists), ("charter-headings", chk_headings),
    ("charter-parts-filled", chk_filled), ("change-rule", chk_change_rule),
    ("current-season", chk_season), ("toolset-declared", chk_toolset),
    ("toolset-runs-when", chk_runs_when), ("toolset-for-sign", chk_for_sign),
    ("charter-ratified", chk_ratified), ("identity-block", chk_identity_block),
    ("identity-identity", chk_id_identity), ("identity-mandate", chk_id_mandate), ("identity-sharp-test", chk_id_sharp),
    ("identity-toolset", chk_id_toolset), ("direction-page", chk_direction),
]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Conformance check over a meta-agent install.")
    ap.add_argument("root", help="folder holding the install")
    for k in DEFAULTS:
        ap.add_argument("--" + k)
    args = ap.parse_args(argv)
    root = Path(args.root)
    if not root.is_dir():
        print(f"FAIL root: {root} is not a folder")
        return 1
    ctx, failed = Ctx(root, args), 0
    for name, fn in CHECKS:
        ok, msg = fn(ctx)
        print(f"{'SKIP' if ok is None else 'PASS' if ok else 'FAIL'} {name}: {msg}")
        failed += ok is False
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
