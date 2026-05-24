# FitConnect Sprint Plan

## Methodology

The team follows **Scrum with light-weight Kanban visualisation**.

- Sprint length: **2 weeks** (except Sprint 0 and Sprint 4).
- Ceremonies: sprint planning (Mon), daily stand-up (10 min, Teams),
  sprint review + retrospective (Fri of week 2).
- Product Owner: rotating (each sprint one team member represents the client).
- Scrum Master: MateiCosmin88.

## Team composition

| Member          | Primary responsibility                          |
|-----------------|-------------------------------------------------|
| 91Eduard        | Backend, data models, business logic            |
| GMatei90        | Tests, QA, documentation                        |
| MateiCosmin88   | Views, templates, UI/UX, Scrum Master           |

Every member contributes to every sprint; the labels above capture the
*lead* for that discipline.

## Sprint schedule (8 weeks)

| Sprint | Dates                 | Goal                                                       | Capacity (points) |
|--------|-----------------------|------------------------------------------------------------|--------------------|
| 0      | 21 – 27 May 2026      | Team setup, backlog, planning, environment ready           | –                  |
| 1      | 28 May – 10 Jun 2026  | Accounts: registration, login, logout, profile             | 8                  |
| 2      | 11 – 24 Jun 2026      | Events: model, CRUD, browse list, dashboard                | 14                 |
| 3      | 25 Jun – 8 Jul 2026   | RSVP: join, cancel, attendee list, email + in-app reminder | 12                 |
| 4      | 9 – 16 Jul 2026       | Polish: Bootstrap, landing page, exploratory testing, docs | 7                  |

## Sprint 1 – Accounts (28 May – 10 Jun)

Goal: a visitor can register, log in and log out; a logged-in user can see a
placeholder dashboard.

Stories: US01, US02, US03, US04.

Acceptance criteria are captured in each story on the sprint board.
Testing strategy: TDD for all views (`accounts/tests/test_views.py`) and
form validation (`accounts/tests/test_forms.py`).

## Sprint 2 – Events and dashboard (11 – 24 Jun)

Goal: users can create, edit, delete and browse events; the dashboard shows
their upcoming events.

Stories: US05, US06, US07, US08.

## Sprint 3 – RSVP and notifications (25 Jun – 8 Jul)

Goal: users can join and cancel events; organisers can see attendees;
users receive email confirmation and a 24 h reminder banner.

Stories: US09, US10, US11, US12, US13.

## Sprint 4 – Polish and testing (9 – 16 Jul)

Goal: presentable UI, landing page, exploratory bugs fixed, retrospectives
finalised.

Stories: US14, US15, US16.
