Environment Variable Setup
==========================

After following the instructions as laid out in the :doc:`../installation/index` page, the
environmental variables and secrets need to be setup. This topic is covered here.

By reading through the ``env`` file, you should be able to set up the environment variables to suit your needs and the constraints of your local resources.

For clarity's sake, the following variables in the `.env` file need to be set manually:

 .. code-block:: console

    DJANGO_DEBUG=True (by default, set to TRUE)
    EMAIL_HOST_PASSWORD='<email_host_password>'
    # django-allauth SOCIALACCOUNT_PROVIDER client credentials
    GITHUB_SOCIALACCOUNT_APP_CLIENT_ID="<client_id_credential>"
    GITHUB_SOCIALACCOUNT_APP_SECRET="<app_secret>"
    export SECRET_KEY=<secret_key>
    # Uncomment the following three lines to run a sqlite3 db locally.
    # ENGINE_DB=django.db.backends.sqlite3
    # DATABASE_URL=sqlite:///learning-log.sqlite3
    # export POSTGRES_DB=learning-log.sqlite3
    DATABASE_URL=postgres://django_admin:<secret_key>@localhost:5432/learning-log
    export POSTGRES_USER=django_admin
    export POSTGRES_PASSWORD=<postgres_password>
    export POSTGRES_DB=learning-log
    # Use localhost for self-hosted PostgreSQL
    export POSTGRES_HOST=localhost
    # Use 'db' for Docker containers
    # export POSTGRES_HOST=db
    export POSTGRES_PORT=5432

By default, the `.env` file is set up to run the `learning-log` project locally
with a PostgreSQL database. These lines will need to be commented out if a
different configuration is being used.

.. note::
   One option for generating a secret is available as ``run secrets``. See
   :doc:`../features/run_command_features` for details.

When deploying the project to a production environment, along with changing the
variable `DJANGO_DEBUG=False`, the follwing lines in the `.env` file will need
to be uncommented:

 .. code-block:: console

    # Used in production deployment
    SECURE_SSL_REDIRECT=False
    SECURE_HSTS_SECONDS=0
    SECURE_HSTS_INCLUDE_SUBDOMAINS=False
    SECURE_HSTS_PRELOAD=False
    SESSION_COOKIE_SECURE=False
    CSRF_COOKIE_SECURE=False
