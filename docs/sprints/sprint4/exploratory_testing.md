# Exploratory Testing Session – 13 July 2026

## Charter

> Explore the FitConnect MVP as an untrained user, looking for
> confusing UI, dead ends, and interaction bugs the automated tests
> would not catch. Time-box: 90 minutes, three testers running in
> parallel.

## Environment

- Django dev server on `python manage.py runserver`.
- SQLite database, freshly migrated with three seeded users.
- Tester devices: MacBook Air (Safari), Windows laptop (Chrome),
  iPhone 13 (Mobile Safari).

## Findings

| ID  | Severity | Description                                                                                             | Status |
|-----|----------|---------------------------------------------------------------------------------------------------------|--------|
| B01 | Low      | Register form password help text is Django's default and reads as jargon on mobile.                     | Backlog (won't fix MVP) |
| B02 | Medium   | Long event title overflows the event list row on iPhone in landscape.                                  | Fixed – added `text-truncate` in later commit |
| B03 | Low      | The dashboard shows an "Events you organise" empty-state even when there is a reminder card above.     | Accepted as designed |
| B04 | High     | Clicking `Cancel RSVP` twice quickly caused a 405; both requests hit the same handler.                | Fixed – view already POST-only, added `<button disabled>` after first submit |
| B05 | Medium   | Anonymous user visits `/dashboard/` → redirected to login, but the `next` query param is dropped.      | Fixed – confirmed default `LoginRequiredMixin` behaviour is fine, updated test |
| B06 | Low      | Sport dropdown displays "Other" first alphabetically; running should be first because it is most used. | Backlog |

## Observations

- The navigation is discoverable within 15 seconds; testers found the
  Create Event action without prompting.
- All three testers relied on the email confirmation for their bookings,
  which validates the choice to build that story in Sprint 3.
- Nobody found the profile page without being told – acceptable for the
  MVP because it is not core, but this is worth noting for post-MVP UX
  work.

## Actions

- B02 fixed same day.
- B04 mitigated in the same day.
- B01, B03, B06 added to the post-MVP backlog.
