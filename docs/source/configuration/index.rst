Configuration
=============

After following the instructions as laid out in :doc:`../installation/index`, the
appropriate environmental variables and secret keys need to be setup before
launching the project. Both topics are covered here.

This Django project is able to be run, and developed using the following scenarios:

  - locally, using sqlite3
  - locally, using PostgreSQL
  - using Docker with PostgreSQL

Environment Variables and Secrets Setup
---------------------------------------

 :doc:`env_setup`
     How to setup your `.env` file to work with your chosen environment.

Starting the Project Server
---------------------------

 :doc:`server_startup`
     How to start your Django project.

.. toctree::
   :caption: Installation
   :hidden:
   :maxdepth: 2

   env_setup
   server_startup

.. _poetry: https://python-poetry.org
