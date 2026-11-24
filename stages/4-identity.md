# Stage 4: Identity in the start routine

So far the charter is a page. This stage makes every session open as the agent, by putting a short identity block into the start routine context-system installed.

## To the AI reading this

Find the start routine. In the GitHub layout of context-system it is `.claude/skills/start/SKILL.md`. In another store it is wherever the instructions that run at the start of a session live (in the chat-only version, the "To the AI" lines at the top of the save block). Say which one you found.

Do **not** create another `AGENTS.md` or `CLAUDE.md`: context-system forbids it, because a nearer one hides the original. Do **not** copy context-system's start steps into anything of your own. The routine keeps its own steps, and you add one block after them.

Build the block from `templates/start-identity.md`, copying from the charter **word for word**:

- Identity: the charter's Identity, first sentence.
- Mandate: the first line of the charter's Mandate section.
- Sharp test: the first line of the charter's Sharp test section.
- Toolset: the tool names exactly as the headings in the charter's Toolset section, separated by commas, each once.
- The path to the charter and to the direction page (stage 5 creates the latter; write the path now).

Put the block under its own heading, `## Agent Identity`, **after** the routine's existing text, and change nothing above it. (The conformance check expects the routine's own steps, as a list, to come before the block.) Show the person the block and where you put it, and get a yes before saving.

The block carries only the essentials, so it costs a few lines at every start. The charter is opened only when scope is in doubt. Because a copy can drift from the charter, stage 7 checks that the two still agree, and stage 6 watches for the charter going untrue.

Save with context-system's own saving routine (in the GitHub layout, the commit steps in its `AGENTS.md`).

## Check

Open a **fresh** session (a new chat or a new terminal session) and say only "start". After the three lines of where things stand, the reply must include one line naming the agent and its sharp test. The person sees the session open as the agent. If it does not, the block is in the wrong place or the routine is not the one that runs; fix that before moving on.

Next: `5-direction.md`.
