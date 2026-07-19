# Sprint 1 Retrospective (10 Jun 2026)

## What went well

- The team stuck to the red/green TDD cycle for every story. The commit
  history clearly shows `test:` commits preceding the `feat:` commits.
- Using Django's built-in `contrib.auth` views for login and logout
  removed a lot of low-value code; the only custom view we needed for
  Sprint 1 was `RegisterView` and the `profile` page.
- Pair reviews on GitHub pull requests were quick because commits were
  small and focused.

## What could be improved

- The first attempt at `RegisterView` used `CreateView.get_success_url`
  which broke because we redirected before `self.object` was set. We
  found the issue only when the test suite ran. Lesson: run the tests
  before opening a PR, not just before pushing.
- Documentation of accepted user story acceptance criteria was thin at
  the start of the sprint; retrospectives will now include a "criteria
  audit" step.

## Actions for Sprint 2

- Add a pre-push git hook that runs `python manage.py test`.
- Author writes acceptance criteria on the card before pulling it into
  the sprint.
- Continue rotating pair partners so the "profile" story next sprint is
  shared between different members.

## Velocity

- Committed points: 8
- Completed points: 8
- Velocity trend: baseline, first data point for the burndown.
