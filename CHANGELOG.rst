.. _`changelog`:

=========
Changelog
=========

``learning-log`` issues are filed on `GitHub <https://github.com/kevinbowen777/learning-log/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

learning-log 0.3.5 (2026-08-14)
===============================

Improved documentation
----------------------

-  (`#591 <https://github.com/kevinbowen777/learning-log/591>`_): Add towncrier 25.8.0.


New features
------------

-  (`#615 <https://github.com/kevinbowen777/learning-log/615>`_): Upgrade to Django 6.0.8

learning-log 0.3.4 (2026-07-28)
===============================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#609 <https://github.com/kevinbowen777/learning-log/609>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#611 <https://github.com/kevinbowen777/learning-log/611>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#605 <https://github.com/kevinbowen777/learning-log/605>`_): Drop support for Python 3.11.


New features
------------

-  (`#573 <https://github.com/kevinbowen777/learning-log/573>`_): Upgrade Django to 6.0.7.

learning-log 0.3.3 (2025-05-01)
===============================

Contributor-facing changes
--------------------------

-  (`#510 <https://github.com/kevinbowen777/learning-log/510>`_): Upgrade PostgreSQL to 15.11.

-  (`#520 <https://github.com/kevinbowen777/learning-log/520>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#516 <https://github.com/kevinbowen777/learning-log/516>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#515 <https://github.com/kevinbowen777/learning-log/515>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#460 <https://github.com/kevinbowen777/learning-log/460>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#521 <https://github.com/kevinbowen777/learning-log/521>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#524 <https://github.com/kevinbowen777/learning-log/524>`_): Replace safety package with pip-audit.

learning-log 0.3.2 (2025-01-06)
===============================

Contributor-facing changes
--------------------------

-  (`#457 <https://github.com/kevinbowen777/learning-log/457>`_): Add support for Python 3.13

-  (`#498 <https://github.com/kevinbowen777/learning-log/498>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#490 <https://github.com/kevinbowen777/learning-log/490>`_): Upgrade Django to 5.1.4

learning-log 0.3.0 (2023-12-30)
===============================

Contributor-facing changes
--------------------------

- : Upgrade Poetry to 1.7.1.

-  (`#201 <https://github.com/kevinbowen777/learning-log/201>`_): Migrate to non-root Docker user & venv.

-  (`#214 <https://github.com/kevinbowen777/learning-log/214>`_): Update Python to 3.12.0.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#362 <https://github.com/kevinbowen777/learning-log/362>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#366 <https://github.com/kevinbowen777/learning-log/366>`_): Upgrade to Django 5.0.

learning-log 0.2.0 (2023-05-12)
===============================

Contributor-facing changes
--------------------------

-  (`#237 <https://github.com/kevinbowen777/learning-log/237>`_): Install ruff. Drop flake8-* packages.

learning-log 0.1.0 (2023-05-08)
===============================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#138 <https://github.com/kevinbowen777/learning-log/138>`_): Add support for Python 3.12.

-  (`#198 <https://github.com/kevinbowen777/learning-log/198>`_): Migrate from SQLite to PostgreSQL

-  (`#216 <https://github.com/kevinbowen777/learning-log/216>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#221 <https://github.com/kevinbowen777/learning-log/221>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

- : Add Sphinx for documentation


New features
------------

-  (`#238 <https://github.com/kevinbowen777/learning-log/238>`_): Upgrade to Django 4.2.

learning-log 0.0.1 (2021-11-26)
===============================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.4

-  (`#10 <https://github.com/kevinbowen777/learning-log/10>`_): Build Docker support for Heroku deployment.


Miscellaneous internal changes
------------------------------

- : Initial commit
