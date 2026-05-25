# Definition of Done

A user story is considered "Done" when **all** of the following hold.

## Code

- Follows PEP 8 with 4-space indentation and 100-column soft limit.
- No commented-out code left in the repository.
- Public functions and Django views have short docstrings only where the
  intent is not obvious from the name.
- Feature branches are merged into `main` via pull request, never directly.

## Testing (TDD)

- A failing unit test was committed **before** the implementation
  (the "red" step). Reviewers may check `git log --oneline` for the
  `test:` commit preceding the `feat:` commit.
- After implementation the test passes locally
  (`python manage.py test`).
- Overall coverage of app code does not fall below 80 %.
- At least one acceptance-style test (an end-to-end request through the
  Django test client) exists per user-facing story.

## Documentation

- README section is updated if the story adds a new user-facing feature.
- New environment variables or settings are listed in `docs/setup.md`.

## Definition of Ready (reminder)

Stories entering the sprint must have acceptance criteria, an estimate
and no unresolved blockers. See `docs/product_backlog.md`.

## TDD cycle

The team follows the classical **red / green / refactor** cycle:

1. **Red** – write a failing test that expresses the next small piece of
   behaviour. Commit as `test: <what>`.
2. **Green** – write the smallest amount of production code that makes the
   test pass. Commit as `feat: <what>` (or `fix:` for bug fixes).
3. **Refactor** – improve the code without changing behaviour. Commit as
   `refactor: <what>` when the change is not trivial.

The commit history intentionally preserves the red / green pairs so that
Agile evidence of TDD is visible for the assessment.
