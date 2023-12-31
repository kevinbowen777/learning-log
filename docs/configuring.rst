Configuration
=============


Setting up your local environment
---------------------------------

After cloning the project and setting up the virtual environment(preferrably
through Poetry), copy the ``env`` file to ``.env`` and modify your environment
variables as appropriate.

This Django project is able to be run, and developed using the following scenarios:

  - locally, using sqlite3
  - locally, using PostgreSQL
  - using Docker with PostgreSQL

By reading through the ``env`` file, you should be able to set up the environment variables to suit your needs and the constraints of your local resources.

Starting the server
-------------------

  - Running locally over http:

    - ``python manage.py runserver``

  - Running locally over https:

    - ``python manage.py runserver_plus``
  - Running a Docker container:

    - The default is to run over plain http:

      - ``docker compose up --build``
      - ``docker run``

    - Editing the ``docker-compose.yml`` file, the container can be run with
      Werkzeug & pyOpenSSL over https, or with gunicorn
