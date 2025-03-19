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
