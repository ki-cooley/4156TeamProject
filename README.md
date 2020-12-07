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
$ mysql -u root -p
mysql> CREATE DATABASE pomodoro_db;
mysql> quit
```
5. Modify pomodoro/pomodoro/pomodoro/settings.py to replace 'fn37v9xn396jj' in DATABASES['default']['password'] with your local mysql password
6. Install virtualenv and create and activate a virtual environment:
```
$ pip install virtualenv
$ python -m venv env
$ source env/bin/activate
```
7. Install the requirements:
```
$ pip install -r requirements.txt
```
8. Run the server:
```
$ python manage.py runserver
```
9. Navigate to http://127.0.0.1:8000 in your browser
