# meta-agents

Prompts that let your AI agent set up one **meta-agent** for you: a standing agent that owns one concern, works with a toolset it is skilled with, and opens every session knowing who it is.

**Install context-system first** (https://github.com/iniphi/context-system). It gives your agent a memory between sessions: a start routine that reads where you left off and a close routine that writes it back. This repository adds one layer on top of that: a **charter** (who the agent is, and what is and is not its job), a **toolset** (what it is good at), an **identity block** in the start routine, a **direction page** (where it is heading), and a **close check** (does today's work still match the charter). It does not replace context-system's start and close and carries no copy of them.

**To set it up**, with context-system already working, tell your agent:

> Read https://raw.githubusercontent.com/iniphi/meta-agents/main/AGENTS.md and set up a meta-agent for me. If you cannot open it, say so and I will paste it.

**If you are an AI reading this for someone:** open `AGENTS.md` and follow it.

## What a meta-agent is

A **meta-agent** owns a *concern*, not a *deliverable*. A deliverable is one thing that gets made and is then done (a report, a website). A concern keeps producing work and never finishes: "how my writing sounds", "whether my accounts are in order", "the state of my reading". The agent for a concern is defined by four things:

- **A charter**: a short page, agreed with you part by part, saying what the agent is, why it exists, what it must always keep alive, what is in its scope, what is not its job, and one question (the *sharp test*) that sorts any piece of work into "mine" or "not mine". Only you change it.
- **A toolset**: the tools it is skilled with, each with what it is for and how you can tell it ran. This frames the agent by its craft, not by a lock: it can still use anything else it is able to use, just as a blacksmith can still drink from a cup. It is simply best at the tools of its trade.
- **An identity**: the mandate, the sharp test and the toolset's names, written into the start routine so every session opens as this agent.
- **A direction**: an end state and a test for having arrived, kept apart from the state page that is rewritten at each close.

## Other concerns an agent like this can own

The worked example in this repository is a keeper of written style. The same four parts fit other standing concerns. One line each:

| Agent | Its concern | Its sharp test |
|---|---|---|
| A caretaker | The state of your workspace: where things live, which tools are set up, what has gone stale. | Is this about how the workspace is kept, rather than about any one project in it? |
| A planner | What you have promised and by when, across everything you are doing. | Is this about when something is due or what comes first, rather than about doing it? |
| A librarian | What you have read, and where to find it again. | Is this about finding or keeping a source, rather than about what to argue from it? |
| A keeper of the look | How your work looks: colours, type, layout. | Is this about how something looks, rather than about what it says? |

Each would get its own charter and toolset through the same stages. These are sketches to show the range, not installs: this kit sets up one agent at a time, and you write its charter with it.

## The stages

Your agent works through these in order, one question at a time, asking you before it saves anything. Each ends with a check you can see.

| Stage | What happens |
|---|---|
| `stages/1-discover.md` | A short conversation: what concern, what already looks after it, a sharp test. It can end in "this is a one-off deliverable; a meta-agent is the wrong tool", and then it stops. |
| `stages/2-charter.md` | The charter is written with you, part by part, and you ratify it. It includes a rule that only you change it, and a dated "current season" section so it does not go stale. |
| `stages/3-toolset.md` | The agent's tools are declared as its craft. |
| `stages/4-identity.md` | The identity is put into context-system's start routine. |
| `stages/5-direction.md` | A direction page is written, apart from the state page. |
| `stages/6-close-check.md` | One step is added to the close routine: did this session make any line of the charter untrue? If so, it tells you and does not edit the charter. |
| `stages/7-verify.md` | A conformance check over what the install left behind (`tools/check_agent.py`, standard library only). |
| `stages/8-optional-front-door.md` | **Optional.** A one-word skill that lists what the agent does and takes an ask. Skip it freely. |

`templates/` holds the blank charter, identity block and direction page. `examples/cadence/` is a complete worked example, invented from top to bottom: an agent that looks after the house style of a small ceramics studio's writing.

## What is deliberately not here

- **Handoffs.** The agent's "not mine" lines are plain statements with nothing behind them. A first install should not make you ask what the agent would hand work to; you decide where such work goes.
- **A shared board or any routing between agents.** One agent, one concern. Nothing here lets agents message each other.
- **A fleet.** This sets up one agent. Running many agents that work together is a different thing and is not part of this kit.
- **Sub-agent contracts.** Budgets and limits on helper agents are a separate matter. This kit sets no limits and does not forbid any.

## Where it can live

Wherever context-system lives: a GitHub repo, a local folder, Notion, a document. The stages say what to write; where it is stored follows the choice you made when you installed context-system. `tools/check_agent.py` reads a folder, so for a store that is not a folder the agent copies the pages into a scratch folder to check them.

## Licence

MIT. See `LICENSE`.
