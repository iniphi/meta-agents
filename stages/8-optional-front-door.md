# Stage 8 (OPTIONAL): A front door

**This stage is optional. The agent is complete without it.** Offer it once, in one line ("Do you want a one-word door that lists what the agent looks after and takes an ask?"), and skip it on a no.

A front door is a small skill named after the agent. Typed on its own, it says what the agent looks after and what it is good at. Typed with an ask, it takes the ask using a tool from the toolset.

## To the AI reading this

Create `.claude/skills/<agent name>/SKILL.md` in the GitHub layout of context-system (in another store, a Project, Gem or saved prompt with the same text). The header holds only `name` and `description`. Fill the body from the charter; do not retype the charter's content into it, or the two will drift. The body says:

> **With no ask.** Read the charter and the direction page and print: what the agent is (Identity), what it looks after (In scope), its toolset (each tool's name and its "For" line), the current season in one line, and the done test from the direction page.
>
> **With an ask.** Take it, as an ordinary session of the agent. Pick the tool in the toolset whose "For" line fits, say which one you are reaching for, and do the work in this session, ending as every session does with the close routine. If no tool fits, do the work with whatever else is to hand and note in the log that the toolset has a gap; the owner may want a new tool, and adding one is a change to the charter.

Write only that. The door starts nothing unattended, schedules nothing and sends nothing anywhere: it works inside a session the owner is in.

Show the person the skill and get a yes before saving. Save as context-system's saving routine says.

## Check

Type the agent's name with nothing after it: the list appears, naming what the agent looks after and its toolset by name, drawn from the charter. Type it with an ask that is in scope: it takes the ask and says which tool from the toolset it is using.
