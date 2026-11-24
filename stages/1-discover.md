# Stage 1: Discover

A short conversation that decides whether this is a meta-agent at all. It ends in a yes or a stop, and it is allowed to end in a stop.

## To the AI reading this

Before you ask anything, check that context-system is installed: there is a rules file (`AGENTS.md`), a state page (`context/state.md` in the GitHub layout), and a start routine. If not, stop and say: "Install context-system first (https://github.com/iniphi/context-system), then come back." Do nothing else.

Ask **one question at a time** and wait for each answer. Do not offer a charter yet.

1. **The concern.** "What do you want taken care of, month after month, that you keep having to re-explain to an assistant?" Take their words. Say it back in one line.

2. **The gate: a concern, not a deliverable.** A meta-agent owns a concern: something that keeps producing work and never finishes. It does not own a deliverable: one thing that gets made and is then done. Ask: "If the next piece of work in this area shipped tomorrow, would the concern still be there the day after?"
   - If yes, go on.
   - If no, say plainly: "This is a deliverable, not a concern. A meta-agent is the wrong tool. Use your normal start and task routines for it." Write nothing, and stop.

3. **The nearest existing thing.** "What already looks after this, even badly? A person, a folder, a project, a routine, a habit?" If something already owns it fully, say so and ask whether they want to replace it or leave it. If they leave it, stop. If it owns only part, note which part is left over: that is the concern.

4. **The sharp test.** A sharp test is one question that sorts any piece of work into "this is the concern's" or "this is not". Draft one with them, then try it on three real pieces of work they name: two they would expect to be the concern's and one they would not. It must sort all three correctly. If it does not, change the question, not the examples.

5. **A name.** One word they will be happy to type, for the agent.

6. **Record it.** Write one file in `decisions/` (context-system's format): `<YYYY-MM-DD>-meta-agent-discovery.md`, with the concern in one line, the nearest existing thing, the sharp test, the three sorted examples, and "proceed". Rebuild the index if context-system gave you a script for it.

## Check

Say back, in five lines at most: the concern, the nearest existing thing, the sharp test, how the three examples sorted, and the name. The person says yes, or tells you what is wrong. A stop at step 2 or 3 counts as a passed stage: the person saw the reason.

Next: `2-charter.md`.
