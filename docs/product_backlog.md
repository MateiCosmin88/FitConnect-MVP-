# FitConnect Product Backlog

Prioritised list of user stories for the FitConnect MVP. Story points use a
modified Fibonacci scale (1, 2, 3, 5, 8). Priority is MoSCoW
(Must, Should, Could, Won't for now).

## Epics

- **E1** – Accounts (authentication)
- **E2** – Events (create, edit, browse)
- **E3** – RSVP (participation)
- **E4** – Notifications
- **E5** – Cross-cutting UI/UX and polish

## User stories

| ID   | Epic | Story                                                                                                                              | Priority | Points | Sprint |
|------|------|------------------------------------------------------------------------------------------------------------------------------------|----------|--------|--------|
| US01 | E1   | As a visitor, I want to register with an email and password so that I can access the platform.                                     | Must     | 3      | 1      |
| US02 | E1   | As a returning user, I want to log in so that I can use my account.                                                                | Must     | 2      | 1      |
| US03 | E1   | As a logged-in user, I want to log out so that my account is not left open on shared devices.                                      | Must     | 1      | 1      |
| US04 | E1   | As a user, I want a simple profile page so I can see my details.                                                                    | Should   | 2      | 1      |
| US05 | E2   | As an organiser, I want to create a new event with title, description, date, location and sport so that others can join.           | Must     | 5      | 2      |
| US06 | E2   | As an organiser, I want to edit or delete my own events so I can correct mistakes.                                                 | Must     | 3      | 2      |
| US07 | E2   | As a user, I want to browse a list of upcoming events so I can find sessions that interest me.                                     | Must     | 3      | 2      |
| US08 | E2   | As a user, I want a personal dashboard showing my upcoming sessions so I can plan my week.                                         | Must     | 3      | 2      |
| US09 | E3   | As a user, I want to RSVP (join) to an event so the organiser knows I am attending.                                                | Must     | 3      | 3      |
| US10 | E3   | As a user, I want to cancel my RSVP so I can free my slot if plans change.                                                         | Must     | 2      | 3      |
| US11 | E3   | As an organiser, I want to see the attendee list for my event so I can plan capacity.                                              | Should   | 2      | 3      |
| US12 | E4   | As a user, I want an email confirmation when I RSVP so I have a record of the booking.                                             | Must     | 3      | 3      |
| US13 | E4   | As a user, I want an in-app reminder banner on the dashboard for events in the next 24 hours so I do not miss them.                | Should   | 2      | 3      |
| US14 | E5   | As a user, I want the site to look clean and responsive on mobile so it feels trustworthy.                                         | Should   | 3      | 4      |
| US15 | E5   | As a user, I want error messages to be clear so I can fix my input.                                                                | Should   | 2      | 4      |
| US16 | E5   | As a user, I want a public landing page explaining what FitConnect is so I understand the value before registering.                | Should   | 2      | 4      |

## Out of scope for the MVP

- Payments / paid events
- Private groups and invitations
- Chat between users
- Native mobile apps
- Third-party OAuth login

## Definition of ready

A story is ready to be pulled into a sprint when it has:

- Acceptance criteria written
- Estimated in story points by the whole team
- No unresolved dependencies on other stories
- Agreement from the Product Owner on scope
