# Hands-on: let the model improve the prompt

**Goal:** a prompt that sends each customer statement about price to the right team, as accurately as possible.
**Time:** 20 minutes. **Tool:** ChatGPT. Work alone; ask your neighbor if you get stuck.

**Your files**

| File | What it is |
|---|---|
| `practice.csv` | 60 customer statements. For improving your prompt. |
| `practice_labels.csv` | The correct team for each practice statement. |
| `test.csv` | 30 new statements. For the final test only. |
| `test_labels.csv` | The correct teams for the test. Upload only at the very end. |
| `starter-prompt.txt` | A first, weak prompt to start from. |

Statements and correct answers are in separate files on purpose: the model must not see the answers while it classifies.

The seven teams: `atlas`, `bridge`, `compass`, `delta`, `ember`, `falcon`, `harbor`.

The team names say nothing about what a team does. Each team handles one type of price objection, and every statement goes to exactly one team. Some statements fit two teams. The sales team has rules for that, but nobody wrote them down: your prompt has to find them.

---

## Step 1: measure the starter prompt (5 min)

Open a new chat. Upload only `practice.csv`. Send this message, with the text from `starter-prompt.txt` pasted in:

```
I uploaded practice.csv with customer statements (column "statement").
Classify every statement by following only this prompt:
"""
[paste the starter prompt here]
"""
Show me a table with id and your answer.
```

When the table is there, upload `practice_labels.csv` in the same chat and send:

```
Compare your answers with the "label" column in practice_labels.csv.
Show me the score as "correct / 60" and a table of all misses: id, statement, your answer, correct label.
```

Write down your score: **Practice, round 1: ____ / 60**

## Step 2: let the model improve the prompt (10 min)

In the same chat, send:

```
Look at the misses. Which rules would have prevented them?
Rewrite my classification prompt so that it gets these right.
Write a definition for every team and rules for statements that fit two teams. Do not copy statements from the file into the prompt.
Show me the new prompt in a code block.
Then run it on all 60 statements again and show me the score and the misses.
```

Repeat this two or three times. Read the misses each time: is the model wrong, or is the rule unclear?

Write down your best score: **Practice, last round: ____ / 60**

## Step 3: the honest test (5 min)

Open a **new chat**. Upload only `test.csv`. Send this, with your final prompt pasted in:

```
I uploaded test.csv with customer statements (column "statement").
Classify every statement by following only this prompt:
"""
[paste your final prompt here]
"""
Show me a table with id and your answer.
```

When the table is there, upload `test_labels.csv` in the same chat and send:

```
Compare your answers with the "label" column in test_labels.csv.
Show me the score as "correct / 30" and the misses.
```

Write down your score: **Test: ____ / 30**

---

## Compare your two numbers

Turn both into percent (practice ÷ 60, test ÷ 30).

- **About the same:** your prompt learned rules that carry over.
- **Test clearly lower:** your prompt learned the practice file, not the task.

Why a new chat for the test? From step 2 on, the model in the practice chat has seen the correct answers, so its practice score flatters. Only a fresh chat with new statements tells you how good the prompt really is.

**Working in Codex instead?** Open this folder in Codex and say "start the hands-on". The file `AGENTS.md` guides it through the same three steps.
