# Sprint 2 Retrospective (24 Jun 2026)

## What went well

- 24 automated tests across the suite; every user-facing story is
  exercised end-to-end via the Django test client.
- The `Event.objects.upcoming()` custom manager kept both the list view
  and the dashboard trivial, and made the "only future events" behaviour
  testable in isolation.
- The pre-push hook agreed in Sprint 1 was in place; nobody pushed a
  failing test.

## What could be improved

- The `EventForm` needed a manual `input_formats` fix because
  `datetime-local` HTML inputs use ISO-8601 without seconds. That cost
  ~30 minutes and would have been caught earlier if we had done a manual
  sanity check in the browser before opening the PR.
- The dashboard story shipped a Sprint-2-only version (organiser-only);
  we need to remember to extend it during Sprint 3 to include attended
  events.

## Actions for Sprint 3

- Add an acceptance check on the sprint board: "manually clicked the
  golden path in a browser" before the story moves to Done.
- Add pytest so the team can use either `python manage.py test` or
  `pytest` locally (some members prefer pytest's output).

## Velocity

- Committed: 14 points
- Completed: 14 points
- Rolling velocity (2 sprints): 11 points/sprint
