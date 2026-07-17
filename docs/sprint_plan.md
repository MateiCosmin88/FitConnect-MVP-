# FitConnect Sprint Plan

## Methodology

The team follows **Scrum + Kanban + XP** as justified in
`docs/methodology_justification.md`. Sprint length is **2 weeks**
except Sprint 0 (setup, 1 week) and Sprint 4 (polish, 1 week).

### Agile Manifesto values on this project

- **Individuals and interactions over processes and tools** – daily
  10-minute stand-up; pair work called out on the sprint board.
- **Working software over comprehensive documentation** – every sprint
  ends with a passing test suite and a demo-able site; docs describe
  *how the team works*, not the code itself.
- **Customer collaboration over contract negotiation** – Product Owner
  rotates each sprint; MoSCoW ordering revisited at every planning
  meeting.
- **Responding to change over following a plan** – Sprint retrospectives
  add items to the next sprint's plan (see `docs/sprints/sprintN/`).

### XP practices used

- **Test-Driven Development** (see `docs/testing_strategy.md` and the
  `test:` / `feat:` commit pairs).
- **Pair programming** – called out on sprint boards where two names
  appear against one story.
- **Continuous Integration** – GitHub Actions runs on every push and
  PR (`.github/workflows/ci.yml`).
- **Collective code ownership** – `git shortlog` shows every team
  member touching every app.
- **Simple design** – "do the simplest thing that could possibly
  work"; e.g. keeping the auth model as `django.contrib.auth.User`
  and only adding a custom profile if needed post-MVP.

## Ceremonies

- Sprint planning (Mon, ≈45 min).
- Daily stand-up (10 min, Microsoft Teams).
- Sprint review + retrospective (Fri of week 2).
- Risk review at the top of every planning meeting
  (`docs/risk_register.md`).

## Team composition

| Member          | Primary responsibility (lead)                        |
|-----------------|------------------------------------------------------|
| 91Edward        | Backend, data models, business logic                 |
| GMatei90        | Tests, QA, documentation, CI                         |
| MateiCosmin88   | Views, templates, UI/UX, Scrum Master                |

Every member contributes to every sprint; the labels above capture
the *lead* for that discipline. Product Owner role rotates each
sprint.

## Sprint schedule (8 weeks)

| Sprint | Dates                 | Goal                                                       | Capacity (points) |
|--------|-----------------------|------------------------------------------------------------|--------------------|
| 0      | 21 – 27 May 2026      | Team setup, backlog, planning, environment ready           | –                  |
| 1      | 28 May – 10 Jun 2026  | Accounts: registration, login, logout, profile             | 8                  |
| 2      | 11 – 24 Jun 2026      | Events: model, CRUD, browse list, dashboard                | 14                 |
| 3      | 25 Jun – 8 Jul 2026   | RSVP: join, cancel, attendee list, email + in-app reminder | 12                 |
| 4      | 9 – 16 Jul 2026       | Polish: Bootstrap, landing page, exploratory testing, docs | 9                  |

## Per-sprint goals

- **Sprint 1 – Accounts** (US01, US02, US03, US04). Test-first for
  every view.
- **Sprint 2 – Events and dashboard** (US05, US06, US07, US08). Model
  built with an `upcoming()` custom manager to keep views trivial.
- **Sprint 3 – RSVP and notifications** (US09, US10, US11, US12,
  US13). Email backend swapped for `locmem` in tests; console backend
  in dev.
- **Sprint 4 – Polish** (US14, US15, US16). Bootstrap 5 retro-fit,
  exploratory testing session, docs finalisation.

Per-sprint boards, retrospectives, and burndown updates live under
`docs/sprints/sprintN/` and `docs/burndown.csv`.
