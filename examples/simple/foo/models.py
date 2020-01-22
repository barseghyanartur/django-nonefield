from django.db import models

__all__ = (
    'Foo',
)


# class Foo(object):
#     def __init__(self, **kwargs):
#         for field in ('id', 'title', 'text'):
#             setattr(self, field, kwargs.get(field, None))
#
#     @property
#     def pk(self):
#         return self.id

class Foo(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
