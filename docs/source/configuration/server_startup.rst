Starting the Server
===================

After setting up the environment variable as outlined in :doc:`env_setup`, the
server should be ready to be started. Depending on how `.env` is set up, will
determine which method to use.

Running a local server
----------------------
.. note::
   The two commands below can also be run using the ``run`` file.
   See :doc:`../features/run_command_features`


- Running locally over http:

  - ``python manage.py runserver``
  - ``run start``

- Running locally over https:

  - ``python manage.py runserver_plus``
  - ``run start+`` (for use with a self-signed certificate)

Starting the Docker Container
-----------------------------

- Running a Docker container:

  - The default is to run over plain http:

    - ``docker compose up --build``
    - ``docker run``

  - Editing the ``docker-compose.yml`` file, the container can be run with
      Werkzeug & pyOpenSSL over https, or with gunicorn
