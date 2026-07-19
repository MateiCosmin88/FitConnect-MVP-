# Testing strategy

This document explains the testing approach used on FitConnect and
where the evidence lives.

## The Testing Pyramid

The team followed the classical Testing Pyramid.

```
              /\
             /  \       Exploratory  (few, whole-app, manual)
            /----\
           /      \     Acceptance   (ATDD / BDD, end-to-end via test client)
          /--------\
         /          \   Unit         (many, fast, isolated)
        /____________\
```

- **Unit tests** (base of the pyramid) exercise a single object or
  function. Example: `events/tests/test_models.py::EventModelTests::
  test_upcoming_manager_returns_only_future_events`.
- **Acceptance tests** (middle) drive a full HTTP request through the
  Django test client and assert on the response. Example:
  `events/tests/test_rsvp_views.py::RSVPViewTests::
  test_email_sent_on_rsvp`. These are the ATDD tests written from the
  Gherkin scenarios in `docs/atdd_examples.md`.
- **Exploratory tests** (tip) are the 90-minute manual session in
  Sprint 4, documented in
  `docs/sprints/sprint4/exploratory_testing.md`.

## TDD cycle

Every user-facing feature was built following **Red-Green-Refactor**:

1. **Red** – write a failing test that expresses the next small piece
   of behaviour. Commit as `test:`.
2. **Green** – write the smallest production code that makes the test
   pass. Commit as `feat:` (or `fix:`).
3. **Refactor** – improve structure without changing behaviour. Commit
   as `refactor:` if the change is not trivial.

The red/green pairs are deliberately preserved in the commit history
so that a new team member (or a code reviewer) can walk from `test:`
to `feat:` and see the change grow.

## ATDD / BDD

Acceptance criteria for each story are written in Given / When / Then
form on the sprint board card before implementation. Three worked
examples are captured in `docs/atdd_examples.md` (US02 login,
US09 join event, US13 reminder banner) with the corresponding Django
tests referenced.

## Exploratory testing

At the start of Sprint 4 the whole team ran a 90-minute exploratory
session against the running site. Charter, findings and follow-up
actions live in
`docs/sprints/sprint4/exploratory_testing.md`. Six bugs were logged;
the two critical ones (B02 mobile overflow, B04 double-submit RSVP)
were fixed the same day.

## Continuous Integration

Every push to `main` or `develop` triggers `.github/workflows/ci.yml`,
which:

1. Runs the Django system check.
2. Runs `python manage.py test`.
3. Runs the same suite through `pytest` for a second, independent
   runner.

The workflow runs on Python 3.11 and 3.12 in a matrix. A green tick on
GitHub is the team's "trust signal" that the branch is safe to merge.

## Coverage target

The Definition of Done requires coverage of app code not to fall below
80 %. The team runs `coverage run --source=. manage.py test && coverage
report` before opening a PR when the story added non-trivial code
paths. Coverage numbers are recorded in the retrospective for the
sprint that shipped the code.

## Test counts at MVP hand-in

| Type                    | Location                                         | Count |
|-------------------------|--------------------------------------------------|-------|
| Unit + acceptance tests | `accounts/tests/`, `events/tests/`               | 40    |
| Exploratory session     | `docs/sprints/sprint4/exploratory_testing.md`    | 1     |
| CI runs per push        | `.github/workflows/ci.yml` (matrix: 2 versions)  | 2     |

Total runtime of the automated suite is approximately 35 seconds on a
laptop.
