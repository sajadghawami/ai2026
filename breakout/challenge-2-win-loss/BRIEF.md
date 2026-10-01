# Challenge 2: win/loss interviews

**Type:** client work

## The situation

Your client Tessara sells route-planning software to logistics companies. After every won or lost deal, someone interviews the buyer. The notes pile up and nobody reads them. The head of sales asks: "Why do we win, why do we lose, and what does price have to do with it?"

## The task

Build an agent team that turns the interview notes into a one-page summary.

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1a | Coder A | Code the first half of the interviews: outcome, reasons, role of price. | First half of the case data | `agents/1-coder.txt` |
| 1b | Coder B | The same for the second half. Runs in parallel with Coder A. | Second half of the case data | `agents/1-coder.txt` |
| 2 | Synthesizer | Combine both codings into findings with counts. | Both handoffs | `agents/2-synthesizer.txt` |
| 3 | Advisor | Turn the findings into three recommendations for the head of sales. | Synthesizer's handoff | `agents/3-advisor.txt` |
| J | Judge | Score the summary. | Case data + summary | `agents/judge.txt` |

Coder A and Coder B use the same instruction. That's deliberate: if they code differently, the synthesizer gets a mess. Each coder adds one line to say which part is theirs, for example "Your part: interviews 1 to 4."

## The cases

- **Case A:** `data/interviews-A.md` (8 interviews; Coder A takes 1–4, Coder B takes 5–8).
- **Case B:** `data/interviews-B.md` (6 more interviews; split 9–11 and 12–14).

## What good looks like (starting point; the product owner decides)

- Every finding names the interviews it comes from.
- The counts are right.
- Price reasons are separated from other reasons.
- No quote that isn't in the notes.
