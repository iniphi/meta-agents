# Worked example: an agent that looks after one person's house style

An invented owner, Mara, runs a small ceramics studio. Her agent, Cadence, looks after the studio's house style: it keeps a style sheet of her settled preferences and a dated ledger of her corrections, so that nothing she has fixed once needs fixing again. It does not write the studio's texts; they are hers.

Everything here is made up. Read it to see the shape, then write your own.

| File | What it shows | Where it lives in a real install |
|---|---|---|
| `charter.md` | The five parts, the toolset (stage 3), the change rule, a dated season | `context/charter.md` |
| `start.md` | A start routine with the identity block added after its own steps (stage 4) | `.claude/skills/start/SKILL.md` |
| `direction.md` | The horizon page (stage 5) | `context/direction.md` |
| `state.md` | A stand-in for the state page, so the check can see the two pages are apart | `context/state.md` |

This folder passes the conformance check:

```
python tools/check_agent.py examples/cadence
```
