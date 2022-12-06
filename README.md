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
     - Create & edit new topics and entries
     - User registration with email verification & social(GitHub) login using [django-allauth](https://pypi.org/project/django-allauth/)
     - [Bootstrap4](https://pypi.org/project/django-bootstrap4/) & [crispy-forms](https://pypi.org/project/django-crispy-forms/) decorations
     - Customizable user profile pages with bio, profile pic, & [country flags](https://pypi.python.org/pypi/django-countries)
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)
 - Dev/testing
     - Basic module testing templates
     - [Coverage](https://pypi.org/project/coverage/) reports in `htmlcov` directory
     - [Debug-toolbar](https://pypi.org/project/django-debug-toolbar/) available. See notes in `config/settings.py` for enabling.
     - Examples of using [Factories](https://pypi.org/project/factory-boy/) & [pytest](https://pypi.org/project/pytest/) fixtures in account app testing
     - [shell_plus](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) with [IPython](https://pypi.org/project/ipython/) via [django-extensions](https://pypi.python.org/pypi/django-extensions/) package
     - [Nox](https://pypi.org/project/nox/) testing sessions for latest Python 3.9, 3.10, 3.11, and 3.12 
         - [black](https://pypi.org/project/black/) (`nox -s black`)
         - [Sphinx](https://pypi.org/project/Sphinx/) documentaion generation (`nox -s lint`)
         - linting
             - [flake8](https://pypi.org/project/flake8/)
             - [flake8-bandit](https://pypi.org/project/flake8-bandit/)
             - [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
             - [flake8-import-order](https://pypi.org/project/flake8-import-order/)
         - [safety](https://pypi.org/project/safety/)(python package vulnerability testing) (`nox -s safety`)
         - [pytest](https://docs.pytest.org/en/latest/) sessions with
           [pytest-cov](https://pypi.org/project/pytest-cov/) &
           [pytest-django](https://pypi.org/project/pytest-django/) (`coverage run -m pytest`) 

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
     - testing supported for Python 3.9, 3.10, 3.11, 3.12
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`
       - `nox`
       - `nox -s black-3.12`
       - `nox -s docs-3.11`
       - `nox -rs lint-3.9` (Use the 'r' flag to reuse existing session)
       - `nox -s safety` (will run tests against all Python versions)
       - `nox -s tests`

---
### Application Demo
A live application demonstration:

TBD

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
