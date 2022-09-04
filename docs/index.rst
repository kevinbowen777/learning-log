learning_log - A Django poll application
========================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

This repository runs a Django 4.1 polling application.

Learning Log is an online journal system that lets you keep track of information you’ve learned about particular topics.

It allows users to log the topics they’re interested in and to make journal entries as
they learn about each topic. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.

Features
--------

 * User registration with email verification & social(GitHub) login
 * Bootstrap4 & crispy-forms decorations
 * Customizable user profiles with bio, profile picture & country flags
 * Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

Installation
------------

To install the learning_log project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/learning_log.git
   $ cd learning_log

Local install:
--------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker install:
---------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run learning_log, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Live Application Demonstration on Heroku
----------------------------------------
`kbowen-django-learning-log <https://kbowen-django-learning-log.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the learning_log `Issues page <https://github.com/kevinbowen777/learning_log/issues>`_ on GitHub.
