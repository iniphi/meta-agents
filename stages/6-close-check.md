# Stage 6: Close check

A charter goes stale when a session quietly does something the charter says it does not do, or stops doing something it says it does. This stage adds one check to the close routine so that the drift is seen on the day it happens.

## To the AI reading this

Open context-system's close routine (in the GitHub layout, `.claude/skills/close/SKILL.md`). Do **not** copy it and do not rewrite its steps. Add one numbered step, after the step that files to-dos and decisions, with this text:

> **Charter check.** Read the Identity, Scope boundaries, Toolset and Current season of the charter. Ask of each line: did this session make it untrue? Examples: work was done that sits under "Not mine"; a tool in the toolset was not used, or a different one became routine; the season's review date has passed. If a line is now untrue, write a "Charter" entry in the session log saying which line, what happened, and what you propose; tell the owner in the closing line. Never edit the charter. If nothing is untrue, write "Charter check: nothing untrue."

Show the person the added step and get a yes before saving. Save as context-system's saving routine says.

Also say this to the person: tools may carry their own close-time check. If a tool in the toolset has "Runs when: at close", that is where it runs, and the charter check does not replace it.

## What to do when a line is untrue

1. Tell the owner what happened, in plain words, and quote the line.
2. Offer two ways out: the session's work was a mistake and is put right, or the charter should change. Only the owner picks.
3. If the owner changes the charter, make the edit with them in the room, add the dated entry to "Record of changes" with their words, and re-run stage 7's check.
4. If the owner does nothing, the log keeps the entry and the next session sees it. No session fixes it alone.

## Check

Run a test close. The session log has a "Charter check" line (or a "Charter" entry). The charter file has not changed: the person can see this in the version history or by comparing the file to what it was before the close.

Next: `7-verify.md`.
