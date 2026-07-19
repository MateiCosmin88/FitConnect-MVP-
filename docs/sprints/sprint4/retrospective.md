# Sprint 4 Retrospective (16 Jul 2026)

## What went well

- Bootstrap swap was almost transparent: 40 tests already existed and
  all remained green after the template refactor, which gave the team
  confidence to reshape the UI.
- The exploratory-testing session found real interaction bugs (B04
  double-submit, B02 mobile overflow) that no unit test would have
  caught.
- Whole team stayed under committed velocity every sprint; nothing
  spilled over.

## What could be improved

- The team never automated a browser test (Playwright / Selenium).
  Would catch layout regressions during future refactors.
- Email confirmation is plain text only; HTML alternative was added to
  the post-MVP backlog.
- We ran the server locally for demos rather than deploying to a
  staging environment. For a future release, a small Heroku or Fly.io
  deploy would help the client sponsor demo without needing the code.

## Delivery summary

- 16 out of 16 committed stories delivered.
- Total automated tests: 40 (unit + acceptance) plus one exploratory
  session.
- Test suite runs in ~35 seconds locally.
- Rolling velocity across sprints: 11 points/sprint.

## Post-MVP backlog seeds

- HTML email confirmation
- Playwright-based acceptance tests
- Sport dropdown ordered by popularity
- Deploy pipeline (staging + production)
- Private groups, chat, paid events (from original scope-out list)
