*********************
Features
*********************

 * Application

   * Create & edit new topics and entries
   * User registration with email verification & social(GitHub) login using django-allauth_
   * Bootstrap4_ & crispy-forms_ decorations
   * Customizable user profile pages with bio, profile pic, & `country flags`_
   * Image carousel
   * Pagination template
   * Centered account templates(login, registration, verification, etc.)
   * For links to additional packages used in this repository, see the :doc:`Package Index <package_index>`
 * Dev/testing

   * coverage_ reports are available in the `htmlcov` directory.
   * django-debug-toolbar_ available. See notes in `config/settings.py` for enabling.
   * Examples of using factories_ & pytest_ fixtures in account app testing.
   * shell_plus_ with IPython_ via the django-extensions_ package.
   * pre-commit_
   * nox_ testing sessions for latest Python 3.11, 3.12, 3.13.

     * Sphinx_ documentation generation
     * linting

       * ruff_
     * pip-audit_ (python package vulnerability testing)
     * pytest_ sessions with pytest-cov_ & pytest-django_
 * ``run`` command menu

The ``run`` file was adapted from Nick Janetakis\' helpful docker-django-example_ repository.

You can run ``./run`` to get a list of commands and each command has documentation within the run file itself. This comes in handy to run various Docker commands because sometimes these commands can be a bit long to type.

If you get tired of typing ``./run`` you can always create a shell alias with ``alias run=./run`` in your ``~/.bash_aliases`` or equivalent file. Then you'll be able to run ``run`` instead of ``./run``.

 .. _django-allauth: https://pypi.org/project/django-allauth/
 .. _Bootstrap4: https://pypi.org/project/django-bootstrap4/
 .. _crispy-forms: https://pypi.org/project/django-crispy-forms/
 .. _country flags: https://pypi.python.org/pypi/django-countries
 .. _coverage: https://kevinbowen777.github.io/learning-log
 .. _htmlcov:
 .. _django-debug-toolbar: https://pypi.org/project/django-debug-toolbar/
 .. _config/settings.py:
 .. _factories: https://pypi.org/project/factory-boy/
 .. _pytest: https://pypi.org/project/pytest/
 .. _shell_plus: https://django-extensions.readthedocs.io/en/latest/shell_plus.html
 .. _IPython: https://pypi.org/project/ipython/
 .. _django-extensions: https://pypi.python.org/pypi/django-extensions/
 .. _pre-commit: https://github.com/pre-commit/pre-commit
 .. _nox: https://pypi.org/project/nox/
 .. _Sphinx: https://pypi.org/project/Sphinx/
 .. _ruff: https://beta.ruff.rs/docs/
 .. _pip-audit: https://pypi.org/project/pip-audit/
 .. _pytest-cov: https://pypi.org/project/pytest-cov/
 .. _pytest-django: https://pypi.org/project/pytest-django/
 .. _docker-django-example: https://github.com/nickjj/docker-django-example/
