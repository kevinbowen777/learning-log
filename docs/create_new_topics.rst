Add topics/entries
==================

Template for adding a list of topics & entries to learning-log Django application

.. code-block:: console

    book = Topic.objects.create(
        owner="",
        text="",
        )

Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample book list
^^^^^^^^^^^^^^^^

.. code-block:: console

    Topic.objects.create(
        owner = User.objects.first(),
        text = "Test Topic 1",
    )
    Topic.objects.create(
        owner = User.objects.get(username="kbowen"),
        text = "Test Topic 2",
    )
    Topic.objects.create(
        owner = User.objects.get(username="kbowen"),
        text = "Test Topic 3",
    )
    Topic.objects.create(
        owner = User.objects.get(username="susan"),
        text = "21 life skills to learn",
    )
    Topic.objects.create(
        owner = User.objects.get(username="david"),
        text = "21 life skills to learn",
    )
    Topic.objects.create(
        owner = User.objects.get(username="kbowen"),
        text = "21 life skills to learn",
    )
    Topic.objects.create(
        owner = User.objects.get(username="kbowen"),
        text = "Learn Python",
    )
    Topic.objects.create(
        owner = User.objects.get(username="kbowen"),
        text = "Learn Django",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=1),
        text = "Test entry 1 for Test Topic 1",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=1),
        text = "Test entry 2 for Topic 1",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=2),
        text = "Test entry 1 for Test Topic 2.",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=3),
        text = "Test entry 1 for Test Topic 3.",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Plan an invasion",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Change a diaper",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Butcher a hog",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Conn a ship",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Design a building",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Write a sonnet",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Balance accounts",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Build a wall",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Set a broken bone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Comfort the dying",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Take orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Give orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Cooperate",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Act alone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Solve equations",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Analyze a new problem",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Pitch manure",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Program a computer",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Cook a tasty meal",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Fight efficiently",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=4),
        text = "Die gallantly",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Plan an invasion",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Change a diaper",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Butcher a hog",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Conn a ship",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Design a building",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Write a sonnet",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Balance accounts",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Build a wall",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Set a broken bone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Comfort the dying",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Take orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Give orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Cooperate",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Act alone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Solve equations",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Analyze a new problem",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Pitch manure",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Program a computer",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Cook a tasty meal",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Fight efficiently",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=5),
        text = "Die gallantly",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Plan an invasion",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Change a diaper",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Butcher a hog",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Conn a ship",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Design a building",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Write a sonnet",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Balance accounts",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Build a wall",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Set a broken bone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Comfort the dying",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Take orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Give orders",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Cooperate",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Act alone",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Solve equations",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Analyze a new problem",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Pitch manure",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Program a computer",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Cook a tasty meal",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Fight efficiently",
    )
    Entry.objects.create(
        topic = Topic.objects.get(id=6),
        text = "Die gallantly",
    )

Miscellaneous notes
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    In [37]: owner = CustomUser.objects.get(username="kbowen")

    In [38]: for topic in Topics.objects.all():
        ...:     topic.owner = owner
        ...:     topic.save()
        ...:

    In [39]: for topic in Topics.objects.all():
        ...:     print(topic, topic.owner)
        ...:

