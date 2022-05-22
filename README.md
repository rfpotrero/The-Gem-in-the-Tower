## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Purpose of the project
* The Gem in the Tower is an old school adventure text base. 
* The purpose of the game is ascend the tower and reclaim the Gem from the final enemy.
## User stories
* A user wants to play the game 
* A user can progress via the game.
* A user can fight any creature that appear
* A user can keep track of their HP 
* A user will be able to rest to recover HP
## Features
* Playing a game 
* Select the type of attacks 
* Select the action after a fight happen
* Complete the game by defeating the final boss
## Future features
* Introduce different type of rooms 
## Wireframes
* Wireframes and diagrams here!
## Technology
* Python 
* Heroku 
## Test cases
* User starts a game
* User selects what happen after a fight
* User complete the game defeating the final boss
* The game end when the user Health Points reach zero

## Code validation
* Python Coding validation
## Fixed bugs
## Deployment
* Heroku Deployment 
## Credits