Local Installation
==================

This project was built using poetry_ as its Python dependency management tools.
The instructions provided within this documentation reflect that assumption. After cloning the project, move  the `env` file to `.env` and modify your environment variables as appropriate. Next, set up the virtual environment, install the required packages, and apply the database migrations.

Local installation
------------------

.. code-block:: console

   $ mv env .env
   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser

Pre-commit installation
-----------------------

To add the pre-commit_ hooks, run the following command in the poetry shell:

.. code-block:: console

   $ pre-commit install
   $ pre-commit autoupdate

After the repository has been successfully cloned and installed, see the :doc:`../configuration/index` section for instructions to set up your environment and start the application.

.. _poetry: https://python-poetry.org
.. _pre-commit: https://pre-commit.com/
