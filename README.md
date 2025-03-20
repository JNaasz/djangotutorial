## Overview
Application made following the official [djangoproject tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

## Set Up

### Installing django
To install django, you will need to install it locally to your project using a virtual environment.

In the main project folder, create a virtual environment by runing the following command:
`python3 -m venv venv`

Then activate the virtual environment:
`source venv/bin/activate` (For macOS/Linux)

Now install Django using pip within the virtual environment:
`pip install django`

Use the following command to confirm installation:
`python -m django --version`

To deactivate the environment when you are done:
`deactivate`

### Running The Development Server
To run the development server, run the following command in the projects root directory (where manage.py is located):
`python manage.py runserver`

### Creating a new python package
To create a new django package, run the following command in the projects root directory (where manage.py is located) while the virtual environment is activated:
`python manage.py startapp new_package_name`

### Creating the initial database tables
When first runnign the project, you will need to set up the initial database tables. The following command will create the tables based off the installed applications configured in 'mysite/settings.py':
`python manage.py migrate`

#### Verifying table creation
Open terminal and navigate to the folder that contains the db.sqlite3 file. Enter `sqlite3 db.slite3` to open a SQLite shell. Once the shell is open, enter `.tables` to see the tables listed.

#### Adding a new table or updating model
Run `python manage.py makemigrations app_name` to generate new tables based off of the new package's config. You will also need to have the app/package listed in installedApps in the settings.py file before running the command. See oplls.apps.pollsConfig as an example.
If you need to update your apps model at any time run `python manage.py makemigrations` to 'migrate' your app to the new table/database schema. After running the migrations command run `python manage.py migrate` to apply those changes to the database.