factories
=========
Project dummy data (dynamic fixtures). Extremely useful if you want to test
your application on a large data set (which you don't have or difficult to
recreate each time for each developer).

Usage examples
--------------
**Create a single ``Foo`` instance**

.. code-block:: python

    import factories

    book = factories.FooFactory()

**Create many (100) ``Foo`` instances**

.. code-block:: python

    import factories

    foo = factories.FooFactory.create_batch(100)

**Create a single ``Foo`` instance with pre-defined attributes**

.. code-block:: python

    foo = factories.FooFactory(
        title="My book title",
        text="Lorem ipsum dolor sit amet",
    )
