# Breakout: build your agent team

**Goal:** your group builds a small team of AI agents that solves one task, and a judge agent that scores the result.
**Time:** 40 minutes of group work, then 3 minutes to show it.

## The idea: you are the harness

In the talk, the harness was the body around the model: it runs the loop and passes results from one step to the next. Today you do that job by hand.

- Each agent is **one ChatGPT chat with its own instruction**, owned by one person.
- The output of one agent is pasted into the chat of the next one. Nothing else is passed on.
- A **judge agent** scores the final result against criteria your group defines.
- The developers in your group build the same chain in Codex, so it runs without copy and paste.

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
| 0–5 | Read the brief. Pick roles. Open a shared place for handoffs (your group's Teams chat or one shared document). |
| 5–20 | Everyone works on their own part with their role card. Product owner and tester agree on the criteria. |
| 20–35 | Run the whole chain on case A. The judge scores it. Improve the weakest agent. Run again, or run case B. |
| 35–40 | Prepare the demo. |

## Three rules

1. **One new chat per agent run.** Paste the instruction, then the input. An agent must not see what the other agents saw.
2. **Pass on only the HANDOFF block.** If the next agent is missing something, fix the instruction, not the handoff.
3. **Change one agent at a time,** then let the judge score again. Otherwise you don't know what helped.

## The demo (3 minutes)

1. The chain: which agents, in which order.
2. The judge's score on the first run and on the last run.
3. One thing that went wrong, and what you changed.
