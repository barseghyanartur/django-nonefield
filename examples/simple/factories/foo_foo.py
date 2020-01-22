from factory import DjangoModelFactory, Faker

from foo.models import Foo

__all__ = (
    'FooFactory',
)


class BaseFooFactory(DjangoModelFactory):
    """Base foo factory."""

    title = Faker('paragraph')
    text = Faker('text')

    class Meta(object):
        """Meta class."""

        model = Foo
        abstract = True


class FooFactory(BaseFooFactory):
    """Author factory."""
