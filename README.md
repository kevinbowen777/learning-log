## Learning Log

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/learning-log.svg)](https://github.com/kevinbowen777/learning-log/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

Learning Log is an online journal system that lets you keep track of information you’ve learned about particular topics.
<p>
It allows users to log the topics they’re interested in and to make journal entries as
they learn about each topic. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.</p>

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features

 - Application
     - Create & edit new tops and entries
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generation
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

---

### Installation
 - `git clone https://github.com/kevinbowen777/learning_log.git`
 - `cd learning_log`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---
### Application Demo
A live application demonstration hosted at Heroku
- https://kbowen-django-learning-log.herokuapp.com/

---

### Screenshots
Home Page
![Home Page](https://github.com/kevinbowen777/learning-log/blob/master/images/learning_log_home.png)

Topic List
![Topic List](https://github.com/kevinbowen777/learning-log/blob/master/images/learning_log_topics.png)

Topic Details
![Topic List](https://github.com/kevinbowen777/learning-log/blob/master/images/learning_log_topic_details.png)

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/learning-log/issues)
      to view currently open bug reports or open a new issue.
