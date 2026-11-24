# Stage 7: Verify

A check over what the install left behind. It reads the files and asks whether they exist, have content and agree with each other. It does not ask whether the agent is wise.

## To the AI reading this

**With a shell and Python 3.** You do not need a copy of this repository. Fetch the one script into a scratch folder, away from the person's files, and run it against their folder (the one with `context/` in it):

```
mkdir scratch-check
curl -sSL -o scratch-check/check_agent.py https://raw.githubusercontent.com/iniphi/meta-agents/main/tools/check_agent.py
python scratch-check/check_agent.py <their folder>
```

(Without `curl`: `python -c "import urllib.request as u; u.urlretrieve('https://raw.githubusercontent.com/iniphi/meta-agents/main/tools/check_agent.py','scratch-check/check_agent.py')"`.) Read the script before you run it and tell the person what it does: it only reads files and prints. It uses only the standard library. Delete the scratch folder after.

By default it looks for `context/charter.md`, `.claude/skills/start/SKILL.md`, `context/state.md` and `context/direction.md`. If the pages are elsewhere, pass `--charter`, `--start`, `--state`, `--direction`. If the store is not a folder (a chat, a document), copy the pages into a scratch folder under those names first.

It prints one `PASS`, `FAIL` or `SKIP` line per check and exits 1 on any `FAIL`. A `SKIP` means an earlier check failed and this one could not run; fix the `FAIL` first.

**Without a shell.** Do the same checks by reading, and say plainly that you did them by hand. The by-hand route is **weaker**: it covers every row of the table, but you will miss what a script does not miss (a date such as 2031-02-30 that is not real, a tool named twice, a mandate that differs by one word). Say so to the person, and offer to run the script later.

### What the checks enforce

| Check | Fails unless |
|---|---|
| charter-exists | A charter file is found |
| charter-headings | The headings Identity, Mandate, Owned spine, Scope boundaries and Sharp test each appear, spelled exactly (a parenthetical after is allowed) |
| charter-parts-filled | Each of the five has at least three words of real text (not a comment or a `<placeholder>`), and Scope boundaries has both an "In scope" and a "Not mine" subsection with text |
| change-rule | A "Change rule" section has one sentence with "may propose" and one with "only the owner", each in a clause (split at commas, semicolons, "and" and "but") with no negation word, and no phrase letting any session edit the charter |
| current-season | A "Current season" section has a date it was set and a review date (for example "Set 2031-02-03; review by 2031-05-01"), both real calendar dates (YYYY-MM-DD), the review date not before the set date |
| toolset-declared | A section titled "Toolset" (a parenthetical after is allowed) holds at least one `###` tool heading |
| toolset-runs-when | Every tool has a "Runs when:" line of at least three words that is not a placeholder and not a bare "as/when/whenever/if/any time ... needed/necessary/required/appropriate/useful/relevant" phrase |
| toolset-for-sign | Every tool has a "For:" line and a "Sign it ran:" line, each of at least three words of real text; the failure names each tool and what it lacks |
| charter-ratified | Some line says the charter was ratified and carries a real calendar date, and no line says "not ratified" |
| identity-block | The start routine has an "Agent Identity" heading, outside any fenced code, after at least 15 words and two list items of the routine's own |
| identity-identity | The block's Identity line equals the first sentence of the charter's Identity section |
| identity-mandate | The block's Mandate line equals the first line of the charter's Mandate section |
| identity-sharp-test | The block's Sharp test line equals the first line of the charter's Sharp test section |
| identity-toolset | The block's Toolset names and the charter's tool headings are the same list, each name once |
| direction-page | A direction page exists, is not the state page and not the same text, has at least three words under each of "End state" and "Done test", and the state page has neither heading |

### What this cannot tell

- Whether the charter is true, wise or well worded: it checks that words are there, not what they say.
- Whether a change rule that passes is meant: a rule reworded to allow edits, or carrying a loophole ("unless the owner is away ..."), or contradicted elsewhere on the page, can slip through.
- Whether a "Runs when" trigger is a good one. The script rejects only a value of under three words, a placeholder, or a bare "as/when/whenever/if/any time ... needed/necessary/..." phrase. A trigger that is long but meaningless ("Whenever Mara is around") passes; that is a judgement for the person, not the script. Nor does it know whether the tool exists and runs; stage 3's check (you watch it run) covers that.
- Whether a "For:" or "Sign it ran:" line says anything: filler of three real words passes.
- Whether the sharp test is a real question: a statement of three or more words matches its copy in the block just as well.
- Whether a "Not mine" line is free of a place to send the work ("Not mine; give it to X"): the script checks only that the line has text.
- Whether the season is still current: a review date that has already passed still passes.
- Whether a ratification is genuine: a line with the word and a real date is enough for the script; whether the owner said yes is between you and them.
- Whether the agent chose the right tool for a job. That is judgement and is not scripted.
- Whether the start routine's list items are really its steps.

## When a check fails

Fix what it names and run it again. Never edit the script to make it pass. If the fix is to a line of the ratified charter, it is a change: put it to the owner and record it as the change rule says. A mismatch between the identity block and the charter is usually the block drifting, so correct the block, not the charter.

## The judgement questions

Ask the owner these three, one at a time, and write nothing down unless they want a change:

1. When you read the identity line, does it sound like the agent you wanted?
2. Is there anything under "Not mine" you would want it to do, or anything it does that you would want under "Not mine"?
3. Is each tool in the toolset one you would expect it to reach for first?

## Check

The script prints only `PASS` lines and exits 0 (or, by hand, every row is true and you have said that it was by hand), and the owner has answered the three questions. Say so in one line.

Next: `8-optional-front-door.md`, which can be skipped.
