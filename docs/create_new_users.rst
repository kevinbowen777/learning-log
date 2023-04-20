Create new users
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample user list
----------------

.. code-block:: console

    User = get_user_model()
    User.objects.create_user(
        username = "john",
        name = "John Doe",
        first_name = "John",
        last_name = "Doe",
        email = "john@example.com",
        age = "69",
        password="P@s5WoRd!",
    )
    User.objects.create_user(
        username = "susan",
        name = "Susan Sontag",
        first_name = "Susan",
        last_name = "Sontag",
        email = "susan@example.com",
        age = "71",
        password="P@s5WoRd!",
    )
    User.objects.create_user(
        username = "mary",
        name = "Mary Shelley",
        first_name = "Mary",
        last_name = "Shelley",
        email = "mary@example.com",
        age = "53",
        password="P@s5WoRd!",
    )
    User.objects.create_user(
        username = "david",
        name = "David Hockney",
        first_name = "David",
        last_name = "Hockney",
        email = "david@example.com",
        age = "84",
        password="P@s5WoRd!",
    )
    User.objects.create_user(
        username = "alice",
        name = "Alice Coltrane",
        first_name = "Alice",
        last_name = "Coltrane",
        email = "alice@example.com",
        age = "69",
        password="P@s5WoRd!",
    )
    User.objects.create_user(
        username = "testuser",
        name = "Test User",
        first_name = "Test",
        last_name = "User",
        email = "testuser@example.com",
        age = "23",
        password="P@s5WoRd!",
        is_staff=True,
    )
