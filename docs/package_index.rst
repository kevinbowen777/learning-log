Package Index
=============

The following is a list of the primary Python packages being used for
the learning-log_ application.
For a complete list of packages explicitly added to the project, view the
pyproject.toml_ file. For a list of *all* of the package, see the requirements.txt_ file.

Production Packages
-------------------

django-allauth
^^^^^^^^^^^^^^

  * Documentation: https://django-allauth.readthedocs.io/en/latest/
  * Tutorial:
  * Repository: https://github.com/pennersr/django-allauth
  * PyPI package: https://pypi.org/project/django-allauth/
  * Notes:

django-bootstrap4
^^^^^^^^^^^^^^^^^

  * Documentation: https://django-bootstrap4.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/zostera/django-bootstrap4
  * PyPI package: https://pypi.org/project/django-bootstrap4/
  * Notes: This package is not currently being used. Bootstrap is loaded from
    templates/base.html

django-countries
^^^^^^^^^^^^^^^^

  * Documentation:
  * Tutorial:
  * Repository: https://github.com/SmileyChris/django-countries
  * PyPI package: https://pypi.python.org/pypi/django-countries
  * Notes: Used in user profiles

django-crispy-forms
^^^^^^^^^^^^^^^^^^^

  * Documentation: https://django-crispy-forms.readthedocs.io/en/latest/
  * Tutorial:
  * Repository: https://github.com/django-crispy-forms/django-crispy-forms
  * PyPI package: https://pypi.org/project/django-crispy-forms/
  * Notes:

django-extensions
^^^^^^^^^^^^^^^^^

  * Documentation: https://django-extensions.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/django-extensions/django-extensions
  * PyPI package: https://pypi.python.org/pypi/django-extensions/
  * Notes:

environs - environs[django]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * Documentation:
  * Tutorial:
  * Repository: https://github.com/sloria/environs
  * PyPI package: https://pypi.org/project/environs/
  * Notes: Allows for local management of environment variables

Development Packages
--------------------

Poetry
^^^^^^

  * Documentation: https://python-poetry.org/
  * Tutorial:
  * Repository: https://github.com/python-poetry/poetry
  * PyPI package:
  * Notes: Installed system-wide for project dependency management.

pyenv
^^^^^

  * Documentation: https://github.com/pyenv/pyenv
  * Tutorial: https://realpython.com/intro-to-pyenv/
  * Repository: https://github.com/pyenv/pyenv
  * PyPI package: https://pypi.org/project/pyenv/ (placeholder only)
  * Notes: Installed system-wide for multiple Python versions.

coverage
^^^^^^^^

  * Documentation: https://coverage.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/nedbat/coveragepy
  * PyPI package: https://pypi.org/project/coverage/
  * Notes:

djlint
^^^^^^

  * Documentation: https://www.djlint.com/
  * Tutorial:
  * Repository: https://github.com/Riverside-Healthcare/djlint
  * PyPI package: https://pypi.org/project/djlint/
  * Notes:

django-debug-toolbar
^^^^^^^^^^^^^^^^^^^^

  * Documentation: https://django-debug-toolbar.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/jazzband/django-debug-toolbar
  * PyPI package: https://pypi.org/project/django-debug-toolbar/
  * Notes: See config/settings.py for instructions to enable

django-types
^^^^^^^^^^^^

  * Documentation: https://github.com/sbdchd/django-types#readme
  * Tutorial:
  * Repository: https://github.com/sbdchd/django-types
  * PyPI package: https://pypi.org/project/django-types
  * Notes: Type stubs for Django

factory-boy
^^^^^^^^^^^

  * Documentation: https://factoryboy.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/FactoryBoy/factory_boy
  * PyPI package: https://pypi.org/project/factory-boy/
  * Notes:

nox
^^^

  * Documentation: https://nox.thea.codes/en/stable/index.html
  * Tutorial: https://nox.thea.codes/en/stable/tutorial.html
  * Repository: https://github.com/wntrblm/nox
  * PyPI package: https://pypi.org/project/nox/
  * Notes:

pytest
^^^^^^

  * Documentation: https://docs.pytest.org/en/latest/
  * Tutorial:
  * Repository: https://github.com/pytest-dev/pytest
  * PyPI package: https://pypi.org/project/pytest/
  * Notes:

pytest-cov
^^^^^^^^^^

  * Documentation: https://pytest-cov.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/pytest-dev/pytest-cov
  * PyPI package: https://pypi.org/project/pytest-cov/
  * Notes:

pytest-django
^^^^^^^^^^^^^

  * Documentation: https://pytest-django.readthedocs.io/
  * Tutorial: https://pytest-django.readthedocs.io/en/latest/tutorial.html
  * Repository: https://github.com/pytest-dev/pytest-django
  * PyPI package: https://pypi.org/project/pytest-django/
  * Notes:

ruff
^^^^

  * Documentation: https://beta.ruff.rs/docs/
  * Tutorial:: https://beta.ruff.rs/docs/tutorial/
  * Repository: https://github.com/astral-sh/ruff
  * PyPI package: https://pypi.org/project/ruff/
  * Notes:

Sphinx
^^^^^^

  * Documentation: https://www.sphinx-doc.org/en/master/index.html
  * Tutorial: https://www.sphinx-doc.org/en/master/tutorial/index.html
  * Repository: https://github.com/sphinx-doc/sphinx
  * PyPI package: https://pypi.org/project/Sphinx/
  * Notes:

safety
^^^^^^

  * Documentation: https://docs.pyup.io/docs/getting-started-with-safety-cli
  * Tutorial:
  * Repository: https://github.com/pyupio/safety
  * PyPI package: https://pypi.org/project/safety/
  * Notes:

ipython
^^^^^^^

  * Documentation: https://ipython.readthedocs.io/
  * Tutorial:
  * Repository: https://github.com/ipython/ipython
  * PyPI package: https://pypi.org/project/ipython/
  * Notes: for use with django-extensions shell_plus

rich
^^^^

  * Documentation: https://rich.readthedocs.io/en/latest/
  * Tutorial:
  * Repository: https://github.com/willmcgugan/rich
  * PyPI package: https://pypi.org/project/rich/
  * Notes: for use with django-extensions shell_plus

friendly
^^^^^^^^

  * Documentation: https://friendly-traceback.github.io/docs/index.html
  * Tutorial:
  * Repository: https://github.com/friendly-traceback/friendly
  * PyPI package: https://pypi.org/project/friendly/
  * Notes: for use with django-extensions shell_plus

TODO: Add link to local coverage reports

 .. _learning-log: https://github.com/kevinbowen777/learning-log/
 .. _pyproject.toml: https://github.com/kevinbowen777/learning-log/blob/master/pyproject.toml
 .. _requirements.txt: https://github.com/kevinbowen777/learning-log/blob/master/requirements.txt
