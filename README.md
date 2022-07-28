## Learning Log

Learning Log is a demo application taken from the book _Python Crash Course_.
It is written in Python using the Django web framework. It is an  online journal system that lets you keep track of information you’ve learned about particular topics.
<p>
It allows users to log the topics they’re interested in and to make journal entries as
they learn about each topic. Once logged in, a user can create new topics, add new entries, and read
and edit existing entries.</p>

## Installation
 - `git clone https://github.com/kevinbowen777/learning_log.git`
 - `cd learning_log`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---
### Live Demo on Heroku:
- https://kbowen-django-learning-log.herokuapp.com/

---
### Screenshots
Home Page
![Home Page](https://github.com/kevinbowen777/learning_log/blob/master/images/learning_log_home.png)

Topic List
![Topic List](https://github.com/kevinbowen777/learning_log/blob/master/images/learning_log_topics.png)

Topic Details
![Topic List](https://github.com/kevinbowen777/learning_log/blob/master/images/learning_log_topic_details.png)


[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/learning_log/blob/master/LICENSE)


### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/learning_log/issues)
      to view currently open bug reports or open a new issue.
