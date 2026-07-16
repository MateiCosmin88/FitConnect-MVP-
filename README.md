# FitConnect MVP

FitConnect is a web platform that helps people organise and join fitness
meetups and wellness events — running clubs, yoga classes, group hikes,
cycling meets and similar. Delivered as an 8-week Agile group project
for the the module module.

## Team

| Member          | Role                                     |
|-----------------|------------------------------------------|
| 91Eduard        | Backend, data models, business logic     |
| GMatei90        | Tests, QA, documentation                 |
| MateiCosmin88   | Views, templates, UI/UX, Scrum Master    |

## Features (all delivered)

- User registration, login, logout and profile
- Event creation, editing and deletion (organiser-only)
- Browsing upcoming events with sport tags
- Personal dashboard with 24-hour reminder banner
- RSVP: join, cancel, see attendees (organiser-only)
- Email confirmation on RSVP (console backend in dev)
- Responsive Bootstrap 5 UI

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional, for /admin
python manage.py runserver
```

The site is then available at http://127.0.0.1:8000.

## Running the tests

Either runner works:

```bash
python manage.py test          # 40 tests
pytest                         # same 40 tests via pytest-django
```

## Repository layout

```
fitconnect/           Django project package (settings, urls, wsgi)
accounts/             User registration, login, profile
events/               Event model, CRUD, dashboard, RSVP, notifications
templates/            Shared templates and per-app templates
docs/                 Agile project artefacts (backlog, sprints, risks)
```

## Agile artefacts

- `docs/product_backlog.md` – prioritised user stories
- `docs/sprint_plan.md` – 8-week sprint schedule
- `docs/definition_of_done.md` – DoD and TDD cycle policy
- `docs/risk_register.md` – Agile Risk Board
- `docs/atdd_examples.md` – ATDD/BDD examples for three stories
- `docs/burndown.csv` – velocity data for all four sprints
- `docs/sprints/sprintN/` – per-sprint board, retrospective and any
  additional artefacts (exploratory testing findings in Sprint 4)

## Delivery summary

- 16 committed stories, 16 delivered
- 40 automated tests, 100 % pass, ~35 s wall time
- Rolling velocity: 11 points/sprint
