# FitConnect MVP

FitConnect is a web platform that helps people organise and join fitness
meetups and wellness events — running clubs, yoga classes, group hikes,
and similar. The MVP is delivered as an Agile project for the the module
module.

## Team

| Member          | Role                                     |
|-----------------|------------------------------------------|
| 91Eduard        | Backend, data models, business logic     |
| GMatei90        | Tests, QA, documentation                 |
| MateiCosmin88   | Views, templates, UI/UX, Scrum Master    |

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The site is then available at http://127.0.0.1:8000.

## Running the tests

```bash
python manage.py test
```

## Repository layout

```
fitconnect/           Django project package (settings, urls, wsgi)
accounts/             User registration, login, profile
events/               Event model, CRUD, dashboard
rsvp/                 RSVP model and notifications
templates/            Shared templates (base, landing page)
docs/                 Agile project artefacts (backlog, sprints, risks)
```

## Agile artefacts

Planning and process documentation lives in `docs/`:

- `product_backlog.md` – prioritised user stories
- `sprint_plan.md` – sprint schedule and team responsibilities
- `definition_of_done.md` – DoD and TDD cycle policy
- `risk_register.md` – Agile Risk Board
- `sprints/` – per-sprint plans, boards and retrospectives
- `burndown.csv` – velocity and burndown data
