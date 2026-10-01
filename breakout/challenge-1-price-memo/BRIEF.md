# Challenge 1: the price-research memo

**Type:** client work

## The situation

Your client Alvora sells PlanPilot, a project-management tool for mid-sized companies. The CEO asks: "Are we priced right against the competition?" She wants a one-page memo with a clear recommendation.

## The task

Build an agent team that turns the data into that memo.

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1 | Researcher | Pull the facts that matter for the price question out of the data. | The case data | `agents/1-researcher.txt` |
| 2 | Analyst | Position PlanPilot against the competitors and recommend a price. | Researcher's handoff | `agents/2-analyst.txt` |
| 3 | Writer | Write the memo for the CEO. | Analyst's handoff | `agents/3-writer.txt` |
| J | Judge | Score the memo. | Case data + memo | `agents/judge.txt` |

## The cases

- **Case A:** the Pro plan. Data: `data/product-pro.md` and `data/competitors.csv`.
- **Case B:** a planned Enterprise plan. Data: `data/product-enterprise.md` and `data/competitors.csv`.

## What good looks like (starting point; the product owner decides)

- A recommendation with a number.
- Every figure in the memo comes from the data.
- The reasoning can be followed in two minutes.
- The main risk of the recommendation is named.
