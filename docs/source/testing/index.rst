Testing
=======

.. note::
   Assuming that this project has been installed with ``poetry``, most of the
   commands in this document should be prefaced with ``poetry run``.

Running tests against this project can be done in several ways:

  1. Running ``python manage.py test``
  2. Using ``coverage``
  3. Running the ``nox`` test suite

A number of the tests can be executed via the ``run`` file. See the contents of
this file for how these tests can be run.

If you would like to create "test" or "dummy" users, see the :doc:`create_new_users` sections for examples.

If you would like to create "test" or "dummy" topics, see the :doc:`create_new_topics` sections for examples.

Running the Tests
=================

Using ``coverage``
------------------

.. code-block:: console

   $ coverage run -m pytest
   $ coverage report
   $ coverage html (this will generate html reports available in the ``htmlcov`` directory)

Using the ``nox`` test suite
----------------------------

The following sessions are available to run via ``nox``:

::

    * coverage-3.12 -> Build JSON coverage report.
    * coverage-3.13 -> Build JSON coverage report.
    * coverage-3.14 -> Build JSON coverage report.
    - docs-3.12 -> Build the documentation.
    - docs-3.13 -> Build the documentation.
    - docs-3.14 -> Build the documentation.
    * lint-3.12 -> Lint using ruff.
    * lint-3.13 -> Lint using ruff.
    * lint-3.14 -> Lint using ruff.
    - pyright-3.12 -> Run pyright type checker.
    - pyright-3.13 -> Run pyright type checker.
    - pyright-3.14 -> Run pyright type checker.
    * audit-3.12 -> Scan dependencies for insecure packages.
    * audit-3.13 -> Scan dependencies for insecure packages.
    * audit-3.14 -> Scan dependencies for insecure packages.
    * tests-3.12 -> Run the test suite.
    * tests-3.13 -> Run the test suite.
    * tests-3.14 -> Run the test suite.

    sessions marked with * are selected, sessions marked with - are skipped.

The ``audit``, ``lint``, ``coverage``, and ``tests`` are enabled to be run with ``nox -s tests``. Generating documentation, (e.g. ``nox -s docs-3.14``) need to be run explicitly.

Below are some example of ``nox`` commands run locally:

.. code-block:: console

   $ nox --list-sessions
   $ nox
   $ nox -s docs-3.14
   $ nox -rs lint-3.13  (Use the 'r' flag to reuse existing session)
   $ nox -s coverage-3.12
   $ nox -s pyright-3.14
   $ nox -s audit  (will run tests against all available Python versions)
   $ nox -s tests

Below are examples of ``nox`` tests run against the Docker container:

.. code-block:: console

   $ docker compose exec web python manage.py test
   $ docker compose exec web nox --list-sessions
   $ docker compose exec web nox
   $ docker compose exec web nox -s coverage-3.12
   $ docker compose exec web nox -s docs-3.14
   $ docker compose exec web nox -rs lint-3.13  (Use the 'r' flag to reuse existing session)
   $ docker compose exec web nox -s audit  (will run tests against all Python versions)
   $ docker compose exec web nox -s tests
