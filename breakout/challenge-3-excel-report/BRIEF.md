# Challenge 3: from monthly export to report

**Type:** internal efficiency

## The situation

Every month someone exports the orders from the ERP system and spends half a day cleaning the file and writing the same report for the management meeting. The export is messy in the same ways every month.

## The task

Build an agent team that turns the raw export into the monthly report.

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1 | Cleaner | Fix the export and list what was fixed. | The raw export | `agents/1-cleaner.txt` |
| 2 | Validator | Check the cleaned table against the rules below. Stop the chain if something is off. | Cleaner's handoff | `agents/2-validator.txt` |
| 3 | Report writer | Write the monthly report. | Validator's handoff | `agents/3-report-writer.txt` |
| J | Judge | Score the report. | Raw export + report | `agents/judge.txt` |

Upload the CSV to the Cleaner's chat. Let it compute with code; don't let it estimate.

## The business rules

1. An order ID counts once. Exact duplicate rows are export errors.
2. Negative quantities are returns. They reduce revenue.
3. Revenue of a row = quantity × unit price. If the `total` column says something else, the total is wrong: use quantity × unit price and mention the row.
4. A missing region becomes "Unknown" and is mentioned in the report.
5. Product names have one correct spelling each: Sensor S1, Sensor S2, Gateway G1, Service Plan.

## The cases

- **Case A:** `data/export-2026-08.csv` (August).
- **Case B:** `data/export-2026-09.csv` (September). The report should compare with August.

## What good looks like (starting point; the product owner decides)

- The total revenue is right.
- Revenue by region and by product is right.
- The report says what was fixed in the data.
- A manager can read it in two minutes.

The facilitator has the correct numbers.
