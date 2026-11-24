# Stage 3: Toolset

The agent is framed by what it is good at, not by what it is kept away from. A master blacksmith can still use a cup to drink from or an axe to chop wood. They are simply better with the tools of the forge, and that is what defines them. This stage writes down the agent's forge.

## To the AI reading this

Open the ratified charter. Its Toolset section is still the template's placeholder. Ask **one question at a time**.

1. "What do you, or this work, use today to look after the concern?" Prompt with kinds, not names: files it keeps, folders of examples, routines or skills, scripts, accounts and connected tools, a way of checking its own work. Take what they list. Add only what they agree to.
2. For each tool they want in the toolset, write three lines under a heading that is the tool's name alone (the name you will paste into the start routine; each tool appears once):
   - **For:** what the tool is for, in one sentence.
   - **Runs when:** the moment the agent reaches for it, named in **at least three words**. "As needed", "when needed", "whenever", "always", "sometimes" and an unfilled placeholder are not triggers. The conformance script rejects a value of fewer than three words, an unfilled placeholder, and a phrase that starts with as, when, whenever, if or any time and ends in needed, necessary, required, appropriate, useful or relevant. A longer vague trigger ("Whenever Mara is around") gets past the script: whether a trigger names a real moment is a judgement you and the owner make, so ask whether you could tell, afterwards, that the moment had come. "Any text meant for readers is drafted or changed" is a good one.
   - **Sign it ran:** what the person can see afterwards: a file that changed, a line in the log, a note at the top of the output.
3. A tool must exist, or be made in this stage. If it does not exist yet, make the smallest working first version now, or leave it out and write a to-do file for it (context-system's `todo/` format). Never declare a tool that is not there.
4. Ask: "Is there anything else it should be good at that is not on the list?" Stop when they say no. A short list is better: three to six tools.

Write the tools into the charter's Toolset section (the heading must read `## Toolset`; a note in brackets after the word, such as `## Toolset (current)`, is allowed). Keep the sentence the template carries there saying the list is not a whitelist, and keep it true. Because the charter is ratified, show the owner the added section and get an explicit yes, and add a line to "Record of changes" with the date and "toolset declared".

## What this is not

Say it plainly to the owner: **this is not a whitelist.** The agent can still use anything else it is able to use. The list says what it is skilled with and reaches for first.

Some owners want a hard limit as well (an agent that cannot touch a given folder or account). That is optional and separate. It is set in the settings of the tool the agent runs in, not in this charter, and this kit does not build it. If they ask, say so and point them at that tool's own permission settings.

## Check

For each tool, the person asks to see it run and you run it once. They can see its "Sign it ran" appear. A tool with no visible sign is rewritten until it has one, or dropped.

Next: `4-identity.md`.
