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
| R02 | Team member unavailable (illness / holiday) during a sprint             | 3 | 4 | 12    | Whole team    | Pair programming, small stories, shared responsibility labels rather than hard silos.               | Mitigating |
| R03 | Underestimating story points leads to sprint overflow                  | 4 | 3 | 12    | GMatei90      | Planning poker at start of sprint; velocity tracked in `docs/burndown.csv`; buffer of 20 %.         | Mitigating |
| R04 | Django email backend blocks development if SMTP is misconfigured       | 3 | 3 | 9     | 91Edward      | Use `django.core.mail.backends.locmem.EmailBackend` in tests and console backend in development.    | Mitigating |
| R05 | UI implementation delayed because backend endpoints not ready          | 3 | 3 | 9     | MateiCosmin88 | Templates built against a fake context first; wire up when views land the same sprint.              | Mitigating |
| R06 | Merge conflicts on shared files (`settings.py`, `urls.py`)             | 4 | 2 | 8     | Whole team    | Small commits, frequent rebases, review PRs same day.                                               | Mitigating |
| R07 | Regression in earlier feature when a later sprint refactors code       | 3 | 3 | 9     | GMatei90      | High-coverage unit tests kept green; CI-like local check `python manage.py test` before every push. | Mitigating |
| R08 | Loss of local database during development                              | 2 | 2 | 4     | 91Edward      | `db.sqlite3` git-ignored; fixtures kept in `events/fixtures/` for reload.                           | Open       |
| R09 | A new engineer cannot reproduce the demo environment                    | 3 | 4 | 12    | MateiCosmin88 | README quickstart section; `requirements.txt` pinned; SQLite means no external services.            | Mitigating |
| R10 | Team over-reliant on one member's knowledge of Django auth             | 3 | 3 | 9     | 91Edward      | Sprint 1 explicitly done together; brown-bag walkthrough of `django.contrib.auth`.                  | Closed     |

## Retrospective log for risk updates

Each retrospective adds a line here summarising any changes made to
the register.

- **Sprint 0 review (27 May)** – Register initialised with 10 risks.
- **Sprint 1 review (10 Jun)** – R10 closed (whole team touched auth).
- **Sprint 2 review (24 Jun)** – R03 status maintained after
  velocity data point.
- **Sprint 3 review (8 Jul)** – R04 closed (email backend swap
  proven safe).
- **Sprint 4 pre-mortem (9 Jul)** – see next section.

## Sprint 4 Pre-Mortem

The team ran a 20-minute **Pre-Mortem** at the start of Sprint 4 –
*"imagine the project has failed catastrophically; walk backwards and
list every reason why"*. The point is to surface risks that we might
not otherwise voice.

Voices captured:

| ID  | Pre-Mortem risk                                                          | Mitigation added                                              |
|-----|--------------------------------------------------------------------------|---------------------------------------------------------------|
| P01 | "The Bootstrap swap breaks all 40 tests and we panic the day before demo" | Do the swap on day one of Sprint 4, run the suite after every template. |
| P02 | "The email tests pass locally but the SMTP backend explodes during the client demo" | Keep the console email backend for the demo; add an override flag documented in the retrospective. |
| P03 | "Nobody can reproduce the running site because setup instructions are unclear" | Rewrite README quickstart, verify it works on a fresh machine. |
| P04 | "The three of us disagree on story points in Sprint 4 and delivery slips" | Fix Sprint 4 capacity at 9 points during planning; anything else deferred. |
| P05 | "CI is red on the demo day"                                              | Green CI status is now part of the Definition of Done. |

Each Pre-Mortem item was checked at the end of Sprint 4:

- **P01** – no test broke during the Bootstrap swap.
- **P02** – console backend used for the demo.
- **P03** – README rewrite committed on 16 Jul.
- **P04** – Sprint 4 delivered on scope with no overflow.
- **P05** – workflow badge green at hand-in.
