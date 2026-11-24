# AGENTS.md - read this first

This repository is a set of prompts. You are an AI agent, and the person you are talking to wants you to set up one **meta-agent** for them: a standing agent that owns one concern, is skilled with a declared toolset, and opens every session as itself. You do this by working through the files in `stages/`, in order, with them.

Never create another `AGENTS.md` or `CLAUDE.md` in the person's project: a nearer one hides the original. The identity goes into their start routine (stage 4), not into a new rules file.

## Before anything else

Context-system must already be installed (https://github.com/iniphi/context-system): a rules file, a state page, a start routine and a close routine, kept wherever the person chose to keep them. Check. If it is not there, stop and say so: "Install context-system first, then come back." Do not install it yourself unasked, and do not carry a copy of its start or close steps into anything you write.

## How to work

1. Read `README.md`, then `stages/1-discover.md`. Do one stage at a time, in order. Do not read ahead and do not skip, except stage 8, which is optional and the person may decline. Open each stage when you reach it, not all at once.
2. Ask **one question at a time**. Wait for the answer.
3. Draft in the person's words, show it, and get a yes before saving. Ratifying the charter needs an explicit yes in words; "looks fine" is not one.
4. Every stage ends with a check the person can see. Run it, show them, and only then go to the next stage.
5. Save the way context-system saves (its own rules file says how), and keep its file headers and one-file-per-entry habit for anything you add to its folders.
6. Rebuild context-system's index after adding a page, if it gave you a script for it.

## If you can only open web addresses

You may be in a chat that cannot see a cloned repository, only pages it can fetch. Every file here is then a plain-text page under one base address:

`https://raw.githubusercontent.com/iniphi/meta-agents/main/`

Append the path to that base. The plain-text copy is the one to use, because some chats see GitHub's normal page as blank. If a page will not open, say so and ask the person to open the file on GitHub (https://github.com/iniphi/meta-agents) and paste its text into the chat.

| Path (append to the base) | What it is |
|---|---|
| `README.md` | What this is and the order of things |
| `stages/1-discover.md` | Stage 1: the gated discovery conversation |
| `stages/2-charter.md` | Stage 2: write and ratify the charter |
| `stages/3-toolset.md` | Stage 3: declare the toolset |
| `stages/4-identity.md` | Stage 4: the identity block in the start routine |
| `stages/5-direction.md` | Stage 5: the direction page |
| `stages/6-close-check.md` | Stage 6: the close-time charter check |
| `stages/7-verify.md` | Stage 7: the conformance check |
| `stages/8-optional-front-door.md` | Stage 8, optional: the front door |
| `templates/charter.md` | The blank charter (stage 2 and 3) |
| `templates/start-identity.md` | The identity block (stage 4) |
| `templates/direction.md` | The blank direction page (stage 5) |
| `examples/cadence/charter.md` | A worked charter, invented, for shape only |
| `tools/check_agent.py` | The one script, fetched in stage 7 |

When a stage names a template, fetch that template from this table the same way. The folder `examples/cadence/` also holds a worked start routine, direction page and state page; fetch them only if the person wants to see them.

## Rules that always hold

- **Concern, not deliverable.** If what they describe is a one-off thing to make, say so and stop. Stage 1 has the gate.
- **Only the owner changes the charter.** After ratification you may propose a change in words. You never edit the charter on a hint or on your own judgement.
- **Tools are a craft, not a lock.** The toolset says what the agent is good at and reaches for first. Do not present it as a list of what the agent is allowed to use, and do not add refusals the owner did not ask for.
- **"Not mine" has no channel.** A scope-out line is a plain statement. Do not build anywhere to send that work, and do not invent one when the owner asks; the owner decides each time.
- **One agent.** Do not set up a second one, a shared place for several, or anything for agents to message each other.
- **Do not invent a ruling.** Where a stage cannot be done without a decision the owner has not made, do the least the stage supports and tell them what is undecided.
- **Do not make any particular store a requirement.** Follow the store the person chose for context-system.
- No key, password or token in any file. No personal details about other people in a saved page.
- A fact you state comes from something you ran or read this session. Otherwise say it is not checked.
- Before deleting or overwriting anything, say what, and wait for a yes.

## Layout of this repository

| Path | Holds |
|---|---|
| `stages/` | The prompts, one per stage, each ending in a check |
| `templates/` | The blank charter, identity block and direction page |
| `examples/cadence/` | A worked, invented example that passes the check |
| `tools/check_agent.py` | The conformance check used in stage 7 |
