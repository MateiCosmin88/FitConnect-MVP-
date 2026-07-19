# Methodology justification

The team needed to pick a project- and risk-management approach that
fitted an 8-week delivery with three people and a low-tolerance-for-
waste client. This note explains why we chose a **Scrum + Kanban + XP
hybrid** rather than any one framework in its pure form.

## Frameworks considered

| Framework          | What it emphasises                                                                        | Fit for FitConnect                                              |
|--------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Scrum**          | Time-boxed sprints, defined roles (PO, SM, Dev), planning + review + retrospective        | Strong fit — 8 weeks maps cleanly to 4 × 2-week sprints.       |
| **Kanban**         | Continuous flow, WIP limits, pull-based board columns                                     | Useful for visualising cards during a sprint.                   |
| **XP**             | TDD, pair programming, refactoring, collective ownership, continuous integration          | Very strong fit — the client wanted engineering rigour.         |
| **DSDM**           | Business roles, MoSCoW prioritisation, timeboxing                                         | Overhead too high for a 3-person team; only borrow MoSCoW.     |
| **FDD**            | Feature-driven, class-owner per feature                                                   | Rigid ownership contradicts the "collective ownership" goal.   |
| **Crystal Clear**  | Small co-located teams, frequent delivery                                                 | Compatible but adds no distinct artefact we need.               |

## Choice: Scrum-based skeleton with XP practices, visualised on a Kanban board

- **Scrum** provides the rhythm — sprints, planning, review,
  retrospective, sprint board. Roles: Product Owner rotates each
  sprint; Scrum Master is MateiCosmin88; the whole team is the
  Development Team.
- **XP** provides the engineering discipline — TDD (Red-Green-
  Refactor), collective code ownership (evidenced by the mixed author
  list in `git shortlog`), Continuous Integration via GitHub Actions,
  and simple design ("do the simplest thing that could possibly work").
- **Kanban** provides the visualisation — the sprint board in Trello
  uses Backlog → Ready → In Progress → In Review → Done.
- **MoSCoW** (borrowed from DSDM) drives the ordering of the product
  backlog and keeps the team honest about "Must vs Should" during
  planning.

## Where each ceremony lives

| Ceremony             | Cadence               | Evidence                                       |
|----------------------|-----------------------|------------------------------------------------|
| Sprint planning      | First Monday morning  | Sprint board files                             |
| Daily stand-up       | 10 minutes / day      | Discussed on Teams; not artefact-preserved.    |
| Sprint review        | Friday of week 2      | Retrospective files                            |
| Sprint retrospective | Immediately after review | `docs/sprints/sprintN/retrospective.md`      |
| Risk review          | Start of every planning | `docs/risk_register.md`                       |

## How risk management fits

Risk is treated as a first-class Scrum artefact – it is reviewed at the
top of every sprint planning session, and any newly discovered risks
are recorded in `docs/risk_register.md` with likelihood × impact
scoring. Sprint 4 also uses the **Pre-Mortem** technique (see the
Pre-Mortem section of the risk register) to flush out end-of-project
risks before the final client demo.

## Why not "just Scrum" or "just XP"

- **Pure Scrum** would not mandate TDD or CI, and our client explicitly
  asked for evidence of test-first work.
- **Pure XP** would not force sprint boundaries; without them the team
  would struggle to slot delivery against the fixed 8-week cadence and
  the review meetings with the client.
- **Pure Kanban** would give no timeboxes and no forced retrospectives;
  velocity would be harder to track.

The hybrid keeps the accountability of Scrum, the engineering rigour
of XP, and the visual clarity of Kanban, at a total ceremony overhead
of about 90 minutes per sprint — an acceptable cost for a three-person
team.
