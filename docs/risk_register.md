# FitConnect Agile Risk Register

Maintained as the team's Agile Risk Board. Reviewed at the start of every
sprint planning session and updated during retrospectives.

## Scoring

- **Likelihood**: 1 (rare) – 5 (almost certain)
- **Impact**: 1 (negligible) – 5 (severe)
- **Score** = Likelihood × Impact
- **Status**: Open, Mitigating, Closed

## Register

| ID  | Risk                                                                   | L | I | Score | Owner         | Mitigation                                                                                          | Status     |
|-----|------------------------------------------------------------------------|---|---|-------|---------------|-----------------------------------------------------------------------------------------------------|------------|
| R01 | Scope creep from optional features distracts from MVP core             | 4 | 4 | 16    | MateiCosmin88 | Product Owner enforces MoSCoW; only Must stories accepted into a sprint until Sprint 3 review.      | Mitigating |
| R02 | Team member unavailable (illness / assessments) during a sprint        | 3 | 4 | 12    | Whole team    | Pair programming, small stories, shared responsibility labels rather than hard silos.               | Mitigating |
| R03 | Underestimating story points leads to sprint overflow                  | 4 | 3 | 12    | GMatei90      | Planning poker at start of sprint; velocity tracked in `docs/burndown.csv`; buffer of 20 %.         | Mitigating |
| R04 | Django email backend blocks development if SMTP is misconfigured       | 3 | 3 | 9     | 91Eduard      | Use `django.core.mail.backends.locmem.EmailBackend` in tests and console backend in development.    | Mitigating |
| R05 | UI implementation delayed because backend endpoints not ready          | 3 | 3 | 9     | MateiCosmin88 | Templates built against a fake context first; wire up when views land the same sprint.              | Mitigating |
| R06 | Merge conflicts on shared files (`settings.py`, `urls.py`)             | 4 | 2 | 8     | Whole team    | Small commits, frequent rebases, review PRs same day.                                               | Mitigating |
| R07 | Regression in earlier feature when a later sprint refactors code       | 3 | 3 | 9     | GMatei90      | High-coverage unit tests kept green; CI-like local check `python manage.py test` before every push. | Mitigating |
| R08 | Loss of local database during development                              | 2 | 2 | 4     | 91Eduard      | `db.sqlite3` git-ignored; fixtures kept in `events/fixtures/` for reload.                           | Open       |
| R09 | Assessor cannot reproduce the demo environment                         | 3 | 4 | 12    | MateiCosmin88 | README quickstart section; `requirements.txt` pinned; SQLite means no external services.            | Mitigating |
| R10 | Team over-reliant on one member's knowledge of Django auth             | 3 | 3 | 9     | 91Eduard      | Sprint 1 explicitly done together; brown-bag walkthrough of `django.contrib.auth`.                  | Closed     |

## Retrospective log for risk updates

Each retrospective adds a line here summarising any changes made to
the register.

- **Sprint 0 review (27 May)** – Register initialised with 10 risks.
