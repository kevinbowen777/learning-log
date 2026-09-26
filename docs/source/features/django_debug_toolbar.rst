django-debug-toolbar configuration
==================================

Resources
---------

-  `package source <https://github.com/jazzband/django-debug-toolbar>`__
-  `documentation <https://django-debug-toolbar.readthedocs.io/>`__

1. Add the package to the development group:
   ``poetry add -group dev django-debug-toolbar``

2. There are four separate configurations to set in our
   ``config/settings.py`` file:

   -  Add ``import socket`` statement
   -  INSTALLED_APPS
   -  MIDDLEWARE
   -  INTERNAL_IPS

   a. Add to the INSTALLED_APPS section:

   .. code:: text

      # config/settings.py
      INSTALLED_APPS = [
          'django.contrib.admin',
          ...
          'django.contrib.sites',

          # Third-party
          'debug_toolbar',

          # Local
          ...
      ]

   b. Add to MIDDLEWARE section:

   .. code:: text

      # config/settings.py
      MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      ...
      "debug_toolbar.middleware.DebugToolbarMiddleware",
      ]

   c. Add the following lines at the bottom of ``config/settings.py``.:

   .. code:: text

      # django-debug-toolbar
      # import socket
      # Use the following in Docker only:
      # hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
      # INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
      # The following is for use locally:
      INTERNAL_IPS = ["127.0.0.1"]

3. Update URLconf/``config/urls.py``:

   .. code:: text

      # config/urls.py
      from django.conf import settings
      ...
      if settings.DEBUG:
        import debug_toolbar  # noqa: F401

          urlpatterns = [
              path("__debug__/", include(debug_toolbar.urls)),
          ] + urlpatterns

   OR

   .. code:: text

      if settings.DEBUG:
      import debug_toolbar  # noqa: F401  # pragma: no cover

      urlpatterns += [  # pragma: no cover
          path("__debug__/", include(debug_toolbar.urls)),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Besides the request/response debug panels, Django Debug Toolbar provides
a management command to debug SQL for ORM calls. The management command
``debugsqlshell`` replicates the Django shell command but it outputs SQL
statements for queries performed with the Django ORM. Open the shell
with the following command: ``python manage.py debugshell``

You can use this command to test ORM queries before adding them to your
views. You can check the resulting SQL statement and the execution time
for each ORM call.

.. code:: text

       In [2]: from images.models import Image

       In [3]: Image.objects.get(id=1)
       SELECT "images_image"."id",
          "images_image"."user_id",
          "images_image"."title",
          "images_image"."slug",
          "images_image"."url",
          "images_image"."image",
          "images_image"."description",
          "images_image"."created",
          "images_image"."total_likes"
       FROM "images_image"
       WHERE "images_image"."id" = 1
       LIMIT 21 [2.26ms]
       Out[3]: Image: Throbbing Gristle's Greatest Hits

       In [4]: Image.objects.get(id=4)
       SELECT "images_image"."id",
          "images_image"."user_id",
          "images_image"."title",
          "images_image"."slug",
          "images_image"."url",
          "images_image"."image",
          "images_image"."description",
          "images_image"."created",
          "images_image"."total_likes"
       FROM "images_image"
       WHERE "images_image"."id" = 4
       LIMIT 21 [0.75ms]
       Out[4]: Image: Kinda Kinks — The Kinks
