# Acceptance Test-Driven Development (ATDD / BDD) examples

The team followed a light-weight BDD style: acceptance criteria for
every user story were written in Given/When/Then form on the sprint
board, and the corresponding Django `TestCase` was written to satisfy
those criteria. Below are three worked examples showing the mapping
between the story, the Gherkin-style criteria, and the automated test.

## US02 – Log in

### Gherkin

```
Feature: Returning user logs in
  As a returning user
  I want to log in with my credentials
  So that I can use my account

Scenario: Valid credentials
  Given I have an account with username "pat" and a strong password
  When I submit the login form with those credentials
  Then I am redirected to my home page
  And I am recognised as "pat" on the next page

Scenario: Wrong password
  Given I have an account with username "pat" and a strong password
  When I submit the login form with a different password
  Then the login form is shown again
  And I remain anonymous
```

### Django test that implements it

See `accounts/tests/test_auth.py::LoginTests::test_valid_login_redirects_to_home`
and `LoginTests::test_invalid_login_shows_error`.

## US09 – Join an event

### Gherkin

```
Feature: Join event
  As a logged-in user
  I want to RSVP to an upcoming event
  So the organiser knows I am attending

Scenario: First RSVP
  Given "Beach yoga" is scheduled for the future
  And I am logged in as "att"
  When I POST to the join URL of the event
  Then an RSVP for "att" against "Beach yoga" is stored
  And I receive an email confirmation at att@example.com
```

### Django test

See `events/tests/test_rsvp_views.py::RSVPViewTests::test_logged_in_user_can_join_event`
and `test_email_sent_on_rsvp`.

## US13 – 24-hour reminder banner

### Gherkin

```
Feature: Dashboard reminder banner
  As a user with events in the next 24 hours
  I want a visible reminder on my dashboard
  So that I do not miss the event

Scenario: Attending an event soon
  Given I have RSVP'd to "Soon session" starting in 6 hours
  When I visit my dashboard
  Then the reminder banner is present
  And it names "Soon session"

Scenario: Attending an event far in the future
  Given I have RSVP'd to "Next month session" starting in 40 days
  When I visit my dashboard
  Then the reminder banner is not present
```

### Django test

See `events/tests/test_reminders.py::DashboardRemindersTests`.

## Why this counts as ATDD

- The acceptance criteria are written **before** any code, at
  sprint-planning time.
- The Django tests are written in the same "arrange – act – assert"
  shape as the Given/When/Then above. Any failure points directly to
  the missing behaviour.
- No user story is accepted into "Done" until its Django acceptance
  test is green (see Definition of Done, section on TDD).
