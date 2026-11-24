# Stage 5: Direction

The state page says where the last session stopped, and context-system rewrites it at every close. It cannot also say where the agent is heading, because that would be rewritten away. The direction page is the horizon, kept apart.

## To the AI reading this

Use `templates/direction.md`. Write it next to the charter (in the GitHub layout, `context/direction.md`, with the `description` and `updated` header context-system requires). Do not put any of it in `context/state.md`.

Ask **one question at a time**:

1. **End state.** "Imagine this agent has done what it exists to do. What is true then that is not true now?" A few sentences.
2. **Done test.** "What one thing could you check, or say, that would settle that we have arrived?" It must be something the owner would actually look at. Push back on vague ones ("it works well") until it is plain ("three letters in a row go out with only spelling fixes").
3. **Horizon.** "When should we look at this again?" A date. Write what happens if the test is not met by then.
4. **What would move it.** Events that would change the end state. Say that any change to the agent's concern goes to the charter first, and only the owner changes the charter.

Add a single line to the "Where I left off" lines of the state page only if the first session needs it: "Direction lives in `context/direction.md`." Never copy the end state or the done test into the state page.

Rebuild the index if context-system gave you a script for it.

## Rule for later sessions

The direction page is rewritten only when the horizon moves and only with the owner, not at each close. A close that notices the horizon has moved says so in the log and tells the owner; it does not edit the page on its own.

## Check

The person opens two files and sees the difference: the state page says where we stopped; the direction page says where we are going and how we will know. The done test is in their own words and they can say it aloud. `end state` and `done test` appear only in the direction page.

Next: `6-close-check.md`.
