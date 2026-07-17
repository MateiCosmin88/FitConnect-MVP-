# Definition of Done

A user story is considered "Done" when **all** of the following hold.
This DoD is the team's contract at the start of the project and is
reviewed in every sprint retrospective.

## Code

- Follows PEP 8 with 4-space indentation and 100-column soft limit.
- No commented-out code left in the repository.
- Public functions and Django views have short docstrings only where
  the intent is not obvious from the name — "**code is the best medium
  for communication**" (Robert Martin).
- Feature branches are merged into `main` via pull request, never
  directly.
- **Boy Scout Rule** – leave the code a little cleaner than you found
  it. Any file you touched for the story should not be worse in
  style, cohesion or naming after the change.

## Testing (TDD → Testing Pyramid)

- A failing unit test was committed **before** the implementation
  (the "red" step of the Red-Green-Refactor cycle). Reviewers may
  check `git log --oneline` for the `test:` commit preceding the
  `feat:` commit.
- After implementation the test passes locally (`python manage.py
  test`).
- Overall coverage of app code does not fall below 80 %.
- Every user-facing story has at least one acceptance test that goes
  through the Django test client, in line with the Testing Pyramid.

## Documentation ("Living Documentation")

- README section is updated if the story adds a new user-facing
  feature.
- New environment variables or settings are listed in the README.
- Sprint board card carries the Gherkin acceptance criteria that
  matches the automated test.

## Continuous integration

- The CI workflow (`.github/workflows/ci.yml`) is green on the branch
  before the PR is merged.

## Definition of Ready (reminder)

Stories entering the sprint must have acceptance criteria, an estimate
and no unresolved blockers. See `docs/product_backlog.md`.

## TDD cycle referenced across the project

The classical **Red / Green / Refactor** cycle:

1. **Red** – write a failing test that expresses the next small piece
   of behaviour. Commit as `test: <what>`.
2. **Green** – write the smallest amount of production code that makes
   the test pass. Commit as `feat: <what>` (or `fix:` for bug fixes).
3. **Refactor** – improve the code without changing behaviour. Commit
   as `refactor: <what>` when the change is not trivial.

The commit history intentionally preserves the red / green pairs so
that TDD activity is visible to any reader of the log.

## Avoiding Muda (Lean waste)

At every retrospective the team asks: *"did we build anything nobody
needed?"* Any story that would take us past the MoSCoW **Must**
threshold without direct client value is considered **gold-plating**
and is deferred to the post-MVP backlog. Examples of waste avoided:

- HTML alternate email body (functionality already delivered by plain
  text).
- Custom user model (Django's `contrib.auth.User` was enough for the
  MVP).
- Sport dropdown ordered by popularity (nice-to-have; deferred).
