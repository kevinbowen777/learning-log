Docker Installation
===================

This project was built using poetry_ as its Python dependency management tools.
The instructions provided within this documentation reflect that assumption. After cloning the project, move  the `env` file to `.env` and modify your environment variables as appropriate. Next, set up the virtual environment, install the required packages, and apply the database migrations.

Docker installation
-------------------

.. code-block:: console

   $ mv env .env
   $ docker compose up --build
   $ docker compose python manage.py migrate
   $ docker compose python manage.py createsuperuser

   Additional commands:
   $ docker compose exec web python manage.py shell_plus
     (loads Django shell autoloading the project models & classes)
   $ docker run -it learning-log-web bash
     (CLI access to container)

Pre-commit installation
-----------------------
To add the pre-commit_ hooks, run the following command in the poetry shell:

.. code-block:: console

   $ pre-commit install
   $ pre-commit autoupdate

After the repository has been successfully cloned and installed, see the :doc:`../configuration/index` section for instructions to set up your environment and start the application.

.. _poetry: https://python-poetry.org
.. _pre-commit: https://pre-commit.com/
