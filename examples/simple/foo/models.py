from copy import deepcopy
from django.db import models
from faker import Faker
from django.utils.functional import keep_lazy

__all__ = (
    'Foo',
    'Bar',
)


class Foo(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()


class BarManager(object):

    def __init__(self, num_records=50):
        self.faker = Faker()
        self._data = {}
        self.num_records = num_records

    @property
    def data(self):
        return deepcopy(self._data)

    def populate_data(self):
        if not self._data:
            for i in range(self.num_records):
                self._data.update({
                    i: Bar(
                        id=i,
                        title=self.faker.sentence(
                            nb_words=3,
                            variable_nb_words=False
                        ),
                        text=self.faker.text(),
                        context_text=self.faker.text()
                    ),
                })

    @keep_lazy(list)
    def all(self):
        self.populate_data()
        return [_d for _d in self.data.values()]

    def get(self, pk):
        self.populate_data()
        return deepcopy(self.data.get(pk, None))


class Bar(object):

    objects = BarManager()

    def __init__(self, **kwargs):
        for field in ('id', 'title', 'text'):
            setattr(self, field, kwargs.get(field, None))

    @property
    def pk(self):
        return self.id

    def refresh_from_db(self):
        obj = deepcopy(self.objects.data.get(self.id, None))
        if obj:
            self.__dict__ = obj.__dict__
