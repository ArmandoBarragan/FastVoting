# Fast Voting
We want an application so anyone who comes to the site can join a group where polls are published 
periodically.
---
## Use cases
### Auth
1. A user wants to create an account.
2. A user wants to log in.
3. A user wants to log out.
4. A user wants to delete his account.
5. A user wants to change their personal info.
### Groups
1. A user wants to create a group.
2. A user wants to join a group.
3. A user wants to invite someone to a group.
4. A user wants to leave a group.
5. A user wants to change the group's info.
### Polls
1. A user wants to create, edit or delete a poll.
2. A user wants to answer a poll.

## Non supported cases
1. A user wants to edit or delete, a poll they did not create.
2. A user wants to edit or delete a group they did not create.
3. A user wants to edit or delete someone else's user.
4. A user wants to create a user with an already existing email.
---
## Architecture
The application will be monolithic (for now), but the database will
be apart from the application.
### Data modeling
#### User:
1. *Id.
2. *Name.
3. *Lastname.
4. *Email.
5. *Password.
#### Group:
1. *Id.
2. *Name.
3. *Private (default=False).
#### Poll:
1. *Id.
2. *Title.
3. Description.
4. Expiring Date.
5. Author.
6. Group.
#### Option:
1. *Id.
2. *Name.
3. *Votes (default=0).
4. *Poll.
#### Relation UserGroup:
1. *User.
2. *Group.
