# Agile vs Waterfall: a critical comparison

At the start of the FitConnect MVP the team weighed Agile against a
Waterfall approach for an 8-week, small-team delivery. This note
captures the position we took and the evidence from the project that
supports it.

## Waterfall in one sentence

Waterfall treats software delivery as a **linear phase gate** — full
requirements first, then full design, then full implementation, then
testing, then delivery. Change is expensive because it forces a return
to an earlier phase.

## Agile in one sentence

Agile treats delivery as a **cadence of short, working increments**;
change is expected and cheap, because every increment is a legitimate
place to re-plan.

## Comparison against FitConnect

| Aspect                | Waterfall would have looked like…                                              | What we actually did (Agile)                                                                 |
|-----------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Requirements          | Fixed brief captured week 1, frozen for 8 weeks.                              | Prioritised backlog (`product_backlog.md`) revisited every sprint planning.                  |
| Design                | Full ERD and screen wireframes signed off before any code.                    | Small model changes driven by tests (Event Sprint 2, RSVP Sprint 3).                        |
| Implementation        | One long "build phase", integration only at the end.                          | Working software at the end of every sprint; feature branches merged frequently.             |
| Testing               | QA phase after implementation.                                                | TDD red/green pairs visible in `git log`; ATDD examples in `docs/atdd_examples.md`.           |
| Feedback              | Client sign-off at the end.                                                   | End-of-sprint reviews with the client; retro notes in `docs/sprints/sprintN/`.               |
| Change accommodation  | Change requests raised in a separate change-control process.                  | Sprint retrospectives adjusted the plan (e.g. Sprint 3 → add pre-push hook, add pytest).    |
| Risk                  | Big-bang risk near the end when integration first happens.                    | Risks tracked continuously in `docs/risk_register.md`, reviewed each planning meeting.       |

## Where Waterfall still wins (honest evaluation)

- Regulated / safety-critical systems where a full requirements
  document is a legal obligation.
- Fixed-price fixed-scope contracts where the client cannot accept an
  emergent design.
- Very large teams working across boundaries where hand-offs need
  formal specification.

For FitConnect none of those apply: a lean startup MVP with a small
in-house team is the textbook case for Agile.

## Evidence in this repository

- **Working software over comprehensive documentation** – every sprint
  ended with a passing test suite and a runnable site; docs describe
  *how the team worked*, not the code itself.
- **Individuals and interactions over processes and tools** – roles
  (`sprint_plan.md`) are lead responsibilities, not hard silos; pair
  work is called out in the sprint boards.
- **Customer collaboration over contract negotiation** – the Product
  Owner role rotated and drove the MoSCoW ordering in the backlog.
- **Responding to change over following a plan** – Sprint 3 dashboard
  was extended in the same sprint after retro feedback; the reminder
  duplicate bug was fixed by adding a regression test in Sprint 4.

## Verdict

For a lean 8-week MVP with rotating client feedback, Agile is the
better fit and the git history shows it: 40+ commits distributed
across 4 sprints, TDD cycles preserved, changes accommodated inside
sprints rather than deferred to a change-control queue.
