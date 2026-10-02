# Developer track

For the developers in the group. Everyone else works with ChatGPT and the role cards; you make the chain run on its own and make the judge harder to fool.

No API key is needed. Codex plays the agents; you build the code around them.

## Level 1: run the chain (10 min)

Open this folder in Codex and say `run the chain on case A`. `AGENTS.md` tells Codex what to do. Whenever a teammate improves an instruction, paste it into the matching file in `agents/` and run again.

## Level 2: build the checks (20 min)

A judge that is an LLM can be talked into a good score. Some things can be checked with code instead. Ask Codex to build `checks.py` with tests (`pytest`) for the checks below, then run them on the latest result in `runs/`.

- Recompute the fee from the named people's day rates in `consultants.csv` and the days in the plan. It must match the draft and stay under the tender's ceiling.
- Every named person exists in `consultants.csv`, is free before the project starts, has no conflicting note for the project period and has the sector experience the tender asks for.
- The fee respects the ceiling after the Q&A answers at the end of the tender, not only the one in the main text.
- The timeline fits the tender's start and end dates and the firm's earliest start.
- Every requirement and every condition in the tender is mentioned in the draft.
- The draft has the sections the tender asks for, in that order, and fits the page limit (about 450 words per page).
- Every reference named in the draft appears in `references.csv` with `may_name_client` = yes.

Keep the checks honest: they read the original data files, never the agents' output, to find out what is true.

## Level 3: give the checks to the agents (stretch)

Turn `checks.py` into a tool the agents use before they hand off. For example, write a skill (`skills/check-result/SKILL.md`) that tells the agent to run the checks and fix what fails. Run the chain again and compare the judge's score before and after.

## In the demo

Show one check that caught something the LLM judge missed, or say honestly that none did.
