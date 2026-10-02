# Challenge 2: proposal draft from a tender

**Type:** client work and internal efficiency

## The situation

A tender arrives on Monday, the proposal is due on Friday, and the first day goes into reading the document and finding out what is actually being asked. Your group builds the team that produces a first draft within minutes.

## The task

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1 | Extractor | Pull out every requirement, deadline and evaluation criterion. | The tender | `agents/1-extractor.txt` |
| 2 | Planner | Plan the approach, pick the team and calculate the fee within the limits of the tender. | Extractor's handoff + the firm's files in `data/` | `agents/2-planner.txt` |
| 3 | Writer | Write the proposal draft. | Planner's handoff | `agents/3-writer.txt` |
| J | Critic (the judge) | Check the draft against the tender and score it. | Tender + the firm's files + draft | `agents/judge.txt` |

## The cases

- **Case A:** `data/tender-A.md`, a regional energy supplier.
- **Case B:** a second tender. Arrives in your Teams chat at minute 30. Run your improved chain on it without changing the instructions first.

Both cases use the files of your fictional consulting firm in `data/`:

- `our-profile.md`: who we are and how we work
- `consultants.csv`: 48 people with level, day rate, sector experience, the date they are free and notes
- `references.csv`: 30 past projects, and whether we may name the client
- `past-proposals.csv`: 100 earlier proposals with fee, budget ceiling and outcome

## What good looks like (starting point; the product owner decides)

- Every must-have requirement of the tender is answered.
- The named people are free in time and have fitting experience.
- The fee is calculated from their day rates and respects the limits in the tender.
- The draft follows the structure the tender asks for, and every reference may be named.
