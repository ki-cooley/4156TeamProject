[![Build Status](https://travis-ci.com/ki-cooley/4156TeamProject.svg?branch=main)](https://travis-ci.com/ki-cooley/4156TeamProject)

# 4156TeamProject
A productivity web app combining a pomodoro timer with website blocking and activity tracking.

## Setup
1. Ensure you are using python 3.7
2. Clone this repo
3. Ensure you have MYSQL installed, and start the server:
```
$ mysql.server start
```
4. Access using your local mysql password and set up the database:
```
For Windows Users, you have to add the following line (The path to mysqld may vary depending on the install location of MySQL on your system):
C:\> cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"

$ mysql -u root -p
mysql> CREATE DATABASE pomodoro_db;
mysql> quit
```
5. Modify pomodoro/pomodoro/settings.py to replace 'fn37v9xn396jj' in DATABASES['default']['password'] with your local mysql password
6. Install virtualenv and create and activate a virtual environment:
```
$ pip install virtualenv
$ python -m venv env

For Windows Users (you have to be in the same directory as the env folder):
$ env\Scripts\activate

For Mac Users:
$ source env/bin/activate
```
7. Install the requirements:
```
$ pip install -r requirements.txt
$ pip install djangorestframework
$ pip install markdown       # Markdown support for the browsable API.
$ pip install django-filter    # Filtering support
$ pip install django-crispy-forms
$ pip install google-apis-oauth-django google-api-python-client  #for OAuth functionality
```
8. Run the server:
```
$ cd pomodoro
$ python manage.py runserver
```
9. Navigate to http://127.0.0.1:8000 in your browser

10. To use blocker/tracker:
```
$$ for TESTING purpose:
modify blocker_gui.py at line 81, change block_time to a shorter time (in minute)

$ open a new terminal window

For mac/linux users:
$ sudo python local_login_gui.py

For windows users:
$ do a RUN AS ADMINISTRATOR before running the script
```
11. To run front-end tests: 
```
$ cd pomodoro/timer
$ jest
```
12. To run back-end tests: 
```
$ py.test
``` 
Note: 
```
$ Make sure to close the chrome browser before running the local application 
$ Run local_login_gui.py in terminal to login locally
$ Make sure to run blocker_gui.py in terminal to login as admin user
```

    
