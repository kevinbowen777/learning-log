The run command script
======================

The ``run`` [1]_ file is a convenience bash script that contains a collection of
functions that provide abbreviated commands for running frequently used
operations. For example, instead of issuing the command ``python manage.py
runserver`` to start the development web server, the command has been shorted so
that ``run start`` will begin the operation.

To get a list of all the commands available, execute  ``./run`` (without any arguments). This comes in handy to run various Docker commands because sometimes these commands can be a bit long to type. Additionally, each command has documentation within the file itself.

Command Summary
---------------

The ``run`` file currently has 34 tasks(i.e. functions) available for use.
Please see the comments provided within the file for additional details for each
command.

.. tip::
   If you get tired of typing ``./run`` you can always create a shell alias with ``alias run=./run`` in your ``~/.bash_aliases`` or equivalent file. Then you'll be able to run ``run`` instead of ``./run``.

* Docker

  * build:dev
  * build:prod
  * down
  * up

* Coverage

  * cov:test
  * cov:test-slow
  * cov:report
  * cov:html

* Miscellaneous

  * cmd
  * manage
  * secret

* Nox

  * nox:cov
  * nox:docs
  * nox:lint
  * nox:pyright
  * nox:audit
  * nox:test
  * nox:tests
  * nox:re-tests
  * nox:current
  * nox:re-current
  * nox:all
  * nox:re-all

* Poetry

  * poe:old
  * poe:up

* Requirements

  * reqs:dev
  * reqs:prod
  * reqs:all

* Ruff

  * ruff:check
  * ruff:fix

* Shell (and shell_plus)

  * sh
  * sh+

* Web Server

  * start
  * start+

The ``run`` file was adapted from Nick Janetakis\' helpful docker-django-example_ repository.


 .. _docker-django-example: https://github.com/nickjj/docker-django-example/
 .. [1] The companion ``drun`` file is used for running comparable commands when using Docker containers.
