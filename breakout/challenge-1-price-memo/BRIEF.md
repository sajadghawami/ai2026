# Challenge 1: the price-research memo

**Type:** client work

## The situation

Your client Alvora sells PlanPilot, a project-management tool for mid-sized companies. The CEO asks: "Are we priced right against the competition?" She wants a one-page memo with a clear recommendation. The data from sales and from the product has more in it than the sales team's opinions.

## The task

Build an agent team that turns the data into that memo.

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1 | Researcher | Analyze the data and pull out the facts that matter for the price question. | The case data | `agents/1-researcher.txt` |
| 2 | Analyst | Position PlanPilot against the competitors and recommend a price. | Researcher's handoff | `agents/2-analyst.txt` |
| 3 | Writer | Write the memo for the CEO. | Analyst's handoff | `agents/3-writer.txt` |
| J | Judge | Score the memo. | Case data + memo | `agents/judge.txt` |

## The cases

- **Case A, the Pro plan.** Data in `data/`:
  - `product-pro.md`: the product, the price and notes from sales
  - `competitors.csv`: 16 competitor plans
  - `deals.csv`: 200 won and lost deals from the last 12 months
  - `usage.csv`: 180 customers, paid users against active users
- **Case B, a planned Enterprise plan.** In the folder `case-b/`. **Open it only at minute 30.** Run your improved chain on it without changing the instructions first.

## What good looks like (starting point; the product owner decides)

- A recommendation with a number.
- Every figure in the memo comes from the data.
- The memo uses what the deals and the usage show, not only what sales says.
- The main risk of the recommendation is named.
