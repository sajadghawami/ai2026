# Role cards

Find your role. Copy the message into a new ChatGPT chat and fill in the brackets.

---

## Product owner

You decide what "good" means. Without your criteria the judge has nothing to score.

```
I am the product owner in a workshop exercise. My group builds a chain of AI agents for this task:

[paste the BRIEF of your challenge]

Help me define, in five minutes:
1. The goal in one sentence.
2. Who reads the result and what they do with it.
3. Four criteria for a good result. For each: a name, what a score of 1 looks like and what a score of 5 looks like.

Ask me at most three questions first. Keep everything short enough to paste into a chat.
```

Give the criteria to the tester. During the runs, read the final result yourself: do you agree with the judge's score?

---

## Agent owner

You own one agent. Its starting instruction is in the `agents` folder of your challenge.

**Improve the instruction (minutes 5–20):**

```
I own one agent in a chain of AI agents. This is its current instruction:

[paste the instruction from the agents folder]

This is an example of the input it will receive:

[paste the input: the data for the first agent, or a HANDOFF block from the agent before you]

The next agent in the chain is: [name and one sentence about what it does]

1. Follow the instruction on this input and show me the result.
2. Tell me three weaknesses of the instruction, judged by what the next agent needs.
3. Rewrite the instruction. Keep it under 150 words.
```

**Run the agent (minutes 20–35):** open a **new chat** every time. Paste your current instruction, then the input. Copy only the HANDOFF block to the next person.

Send your latest instruction to the developers whenever you change it.

---

## Tester

You own the judge agent. Its starting instruction is `agents/judge.txt`.

**Build the judge (minutes 5–20):**

```
I am the tester in a workshop exercise. I own the judge agent that scores the final result of a chain of AI agents.

This is the task:
[paste the BRIEF of your challenge]

These are the product owner's criteria:
[paste the criteria]

This is the current judge instruction:
[paste agents/judge.txt]

1. Rewrite the judge instruction so it scores exactly these criteria from 1 to 5, with one sentence of evidence per score.
2. Draft three checks a careless result would fail, for example a number that is not in the data. I will decide which ones to keep.
```

Read the three checks. Keep the ones you agree with and add them to the judge instruction. **You approve the checks, not the model.**

**Score a run (minutes 20–35):** open a **new chat**. Paste the judge instruction, the original input data and the final result. Tell the group the scores and which agent you think caused the lowest one.

---

## Developer

You make the chain run without copy and paste.

1. Open your challenge folder in Codex.
2. Say: `run the chain on case A`. The file `AGENTS.md` tells Codex what to do. No API key is needed.
3. Whenever a teammate improves an instruction, paste it into the matching file in `agents/` and run again.
4. Compare: does the automatic run get the same judge score as the run by hand? If not, why?

Then continue with `DEVELOPER-TRACK.md` in your challenge folder: build checks in code that make the judge harder to fool, and give them to the agents as a tool.
