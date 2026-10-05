# Hands-on: let the model improve the prompt

This folder is a 20-minute workshop exercise. The user is a participant. Guide them through the three steps below, one step at a time, and wait for them after each step. Keep your messages short.

## Task

Improve a prompt that routes customer statements about price to the team that should follow up. Each statement gets exactly one of seven teams:
`atlas`, `bridge`, `compass`, `delta`, `ember`, `falcon`, `harbor`.

Each team handles one type of price objection. Many statements fit two teams. The labels follow unwritten rules about what each team handles and which team wins. Finding these rules from the misses is the point of the exercise.

## Files

- `practice.csv`: 60 statements. Use these to improve the prompt.
- `practice_labels.csv`: the correct `label` for each practice statement. Read it only after you have written your predictions, to look at the misses.
- `test.csv`: 30 statements without labels. Use only in step 3.
- `test_labels.csv`: the labels for the test. **Do not open this file yourself.** Only `score.py` reads it.
- `final.csv`: 20 more statements for the final exam (step 4).
- `final_labels.csv`: the labels for the final exam. **Do not open this file yourself.** Only `score.py` reads it.
- `starter-prompt.txt`: the weak starting prompt.
- `my-prompt.txt`: the current version of the participant's prompt (create it in step 1 as a copy of the starter prompt).
- `score.py`: compares a predictions file with the labels. Usage: `python3 score.py predictions.csv practice_labels.csv` or `python3 score.py predictions.csv test_labels.csv`.

## Rules for you

- When you classify, follow only the text in `my-prompt.txt`. Do not read the label files while classifying, and do not use knowledge about the labels that the prompt does not contain.
- Classify with your own judgment, row by row. Do not write a keyword script.
- Write predictions as CSV with the header `id,prediction`.
- Never paste statements from `practice.csv` into the prompt. The prompt should contain rules and definitions, not memorized examples.

## Steps

1. **Measure the starter prompt.** Copy `starter-prompt.txt` to `my-prompt.txt`. Classify all 60 practice statements into `predictions_practice.csv`. Run `score.py` against `practice_labels.csv`. Show the score and the misses.
2. **Improve the prompt.** Look at the misses, propose rules that would have prevented them, rewrite `my-prompt.txt`, classify again, score again. Repeat two or three times. Show the score after each round.
3. **The honest test.** Classify `test.csv` with the final `my-prompt.txt` into `predictions_test.csv`. Run `score.py` against `test_labels.csv`. Show both scores in percent, practice and test, and explain the gap in one or two sentences.
4. **Round 2 and the final exam.** Look at the test misses, improve `my-prompt.txt` once more (rules, not statements). Classify `final.csv` into `predictions_final.csv`, run `score.py` against `final_labels.csv`, and show all three scores in percent: practice, test, final.
