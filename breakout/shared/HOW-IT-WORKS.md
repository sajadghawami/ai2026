# Breakout: build your agent team

**Goal:** your group builds a small team of AI agents that solves one task, and a judge agent that scores the result.
**Time:** 40 minutes of group work, then 3 minutes to show it.

The cases are simplified so they fit into 40 minutes. They are still real decisions, and you build a real agent network for them. You don't need to know anything about pricing.

## The idea: you are the harness

In the talk, the harness was the body around the model: it runs the loop and passes results from one step to the next. Today you do that job by hand.

- Each agent is **one ChatGPT chat with its own instruction**, owned by one person.
- The output of one agent is pasted into the chat of the next one. Nothing else is passed on.
- A **judge agent** scores the final result against criteria your group defines.
- The developers in your group build the same chain in Codex, so it runs without copy and paste.
- The data is bigger than one screen. Let ChatGPT analyze the files with code instead of reading them by eye.

## Roles

| Role | How many | What you do |
|---|---|---|
| Product owner | 1 | Decide what a good result looks like. Write the criteria. |
| Agent owner | 1 per agent | Own one agent's instruction. Run it, improve it. |
| Tester | 1–2 | Own the judge agent. Score every run. Name the weakest step. |
| Developer | 2–3 | Put the group's instructions into the `agents/` folder and run the chain in Codex. |

More people than roles? Pair up with an agent owner.

## Timeline

| Min | What |
|---|---|
| 0–5 | Read the brief. Pick roles. Open your group's Teams chat for the handoffs. |
| 5–15 | Everyone works on their own part with their role card. Product owner and tester agree on the criteria. |
| 15–25 | Run the whole chain on case A. The judge scores it. |
| 25–30 | Improve the weakest agent. Run again. |
| 30 | **Case B arrives** in your Teams chat: new data your chain has never seen. |
| 30–37 | Run your improved chain on case B, unchanged. The judge scores it. Does it hold up? |
| 37–40 | Prepare the demo. |

## Three rules

1. **One new chat per agent run.** Paste the instruction, then the input. An agent must not see what the other agents saw.
2. **Pass on only the HANDOFF block.** If the next agent is missing something, fix the instruction, not the handoff.
3. **Change one agent at a time,** then let the judge score again. Otherwise you don't know what helped.

## The demo (3 minutes)

1. The chain: which agents, in which order.
2. The judge's scores: first run on case A, last run on case A, and case B.
3. One thing that went wrong, and what you changed.
