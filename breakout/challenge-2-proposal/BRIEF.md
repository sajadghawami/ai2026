# Challenge 2: proposal draft from a tender

**Type:** client work and internal efficiency

## The situation

A tender arrives on Monday, the proposal is due on Friday, and the first day goes into reading the document and finding out what is actually being asked. Your group builds the team that produces a first draft within minutes.

## The task

| # | Agent | Job | Gets | File |
|---|---|---|---|---|
| 1 | Extractor | Pull out every requirement, deadline and evaluation criterion. | The tender | `agents/1-extractor.txt` |
| 2 | Planner | Plan the approach, the team and the fee within the limits of the tender. | Extractor's handoff + `data/our-profile.md` | `agents/2-planner.txt` |
| 3 | Writer | Write the proposal draft. | Planner's handoff | `agents/3-writer.txt` |
| J | Critic (the judge) | Check the draft against the tender and score it. | Tender + `data/our-profile.md` + draft | `agents/judge.txt` |

## The cases

- **Case A:** `data/tender-A.md` (a regional energy supplier).
- **Case B:** `data/tender-B.md` (a furniture manufacturer).

Both use `data/our-profile.md`, the profile of your fictional consulting firm.

## What good looks like (starting point; the product owner decides)

- Every must-have requirement of the tender is answered.
- The fee and the timeline respect the limits in the tender.
- The draft follows the structure the tender asks for.
- Nothing about your firm is invented: only what is in the profile.
