# Breakout challenge: run the agent chain

This folder is a workshop exercise. The user is a developer in a group that builds a chain of AI agents by hand in ChatGPT. Your job is to run the same chain automatically. Keep your messages short.

## How to run the chain

When the user says "run the chain on case A" (or B):

1. Read `BRIEF.md` for the task, the order of the agents and which data files belong to the case.
2. For each agent in that order, read its instruction from `agents/`. Follow only that instruction, on only the input it is supposed to get: the case data for the first agent, and the HANDOFF block of the previous agent for every later one. Use a separate sub-agent per step if you can; otherwise start each step from a clean slate and do not use what earlier steps saw.
3. Save each agent's full output to `runs/<case>/<number>-<agent>.md`.
4. Last, run `agents/judge.txt` on the case data and the final result. Save it as `runs/<case>/judge.md`.
5. Show the user the final result, the judge's scores and the step the judge names as the weakest.

## Rules

- Do not edit the instructions in `agents/` yourself unless the user asks. Teammates own them.
- Do not let an agent see more than its instruction and its input. That is the point of the exercise.
- No API key is needed. You play each agent yourself.
- If the user asks you to improve the chain: change one instruction, run again, and report the score before and after.
- If the user says "start the developer track", read `DEVELOPER-TRACK.md` and guide them through it, one level at a time.
