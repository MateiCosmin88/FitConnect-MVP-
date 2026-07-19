# Ethics and professional conduct

The team agreed to work in line with the **BCS Code of Conduct** for
the duration of the project. This short note documents how the code
was applied during FitConnect.

## The four sections of the BCS Code of Conduct

### 1. Public interest

- User data collected on FitConnect is limited to what the feature
  needs: username, password (hashed by Django's default hasher), email
  (optional). No location tracking, no third-party analytics, no
  behavioural profiling.
- Events are public by design (browse without login); attendee lists
  are only visible to the organiser, protecting attendee privacy from
  other users.

### 2. Professional competence and integrity

- Every team member wrote tests and production code; nobody claimed
  credit for someone else's commit (verifiable via `git shortlog`).
- Decisions we did not know how to make well were escalated for input
  from a senior engineer rather than guessed.

### 3. Duty to relevant authority

- No proprietary code, images or copy from other projects was used.
- Third-party dependencies are open-source and pinned in
  `requirements.txt`; their licences (BSD, MIT) are compatible with
  the project's intended distribution.

### 4. Duty to the profession

- The commit history is truthful — no back-filled commits; the dates
  and authors correspond to real work by real team members.
- The retrospectives record failures as well as successes so that
  future teams can learn.

## Algorithmic ethics reflection

FitConnect currently uses **no ranking, recommendation or matching
algorithm**. Events are shown in simple chronological order and RSVP
does not use any scoring. This was a deliberate design choice for the
MVP: a naive ranking (e.g. by proximity or by user attribute) would
introduce fairness risks that the team is not equipped to audit inside
an 8-week delivery. Any post-MVP ranking feature is flagged in the
backlog with a note that it requires an ethics review before build.
