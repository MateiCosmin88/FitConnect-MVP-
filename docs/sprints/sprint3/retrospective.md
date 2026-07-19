# Sprint 3 Retrospective (8 Jul 2026)

## What went well

- The RSVP model uniqueness constraint was written test-first, and the
  join view's idempotency was designed around it – exactly the kind of
  small design decision TDD makes visible.
- Extracting `events/notifications.py` from the view kept the join view
  small and made the email content easy to change without touching URL
  or view code.
- 37 tests total; suite still runs in under a minute locally.

## What could be improved

- We nearly forgot to make the reminder query `distinct()`; without it,
  attending an event you also organise would appear twice. Caught by a
  manual dashboard check, not by a test. Retro action: add a test for
  the "organiser + attendee" case in Sprint 4 polish.
- The email confirmation body is plain text. HTML email is a nice-to-
  have that we won't do for the MVP but will note in the backlog.

## Actions for Sprint 4

- Add regression test for the duplicate-in-reminder scenario.
- Add landing-page test to catch template regressions during Bootstrap
  swap.

## Velocity

- Committed: 12; Completed: 12
- Rolling velocity (3 sprints): 11.3 points/sprint
