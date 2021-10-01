# ORIGIN #
This project is an exercise done as part of an OpenClassrooms training course for developers in the Python language.
It corresponds to project 13 of the training.

# GOAL OF THE PROJECT 13 #
The project 13 is free but it must meet a concrete need around you. It will put into practice what has been learned in previous projects.

# GOAL OF THE APPLICATION #
This application is intended to facilitate communication between the inhabitants of a condominium (union council, owners and tenants). Creating links between people has become a real challenge today!

# GUIDELINES #
* The theme of the project is free, but it must demonstrate a real social/societal impact.
* The project must be public, with open source code.
* The project must implement the 12 good practices of Xtreme programming.
* Use continuous integration (we choose Travis here)
* Use an agile project methodology to work in project mode.
* Code written entirely in English: functions, variables, comments, etc.

# DEPLOYMENT #
* PostGreSQL must be installed on the server.
* Create a "macopropriete" database and a user with password
* Creating a virtual environment with Python 3.8
* Clone the application
* Run the following command to install the necessary libraries :
  - pip install -r requirements.txt
* Create an .env file with these environment variables (replace the xxx with your values):
  - DJANGO_SETTINGS_MODULE=config.settings
  - SECRET_KEY=xxx
  - DB_NAME=xxx
  - DB_USER=xxx
  - DB_PASSWORD=xxx
  - DB_HOST=xxx
  - DB_PORT=xxx
* Generate the static files:
  - [python3] manage.py collectstatic
* Create the database tables:
  - [python3] manage.py migrate
* Run the application locally
  - [python3] manage.py runserver
* Run the tests
  - [python3] manage.py test tests