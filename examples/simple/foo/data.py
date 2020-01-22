from faker import Faker
from .models import Foo

faker = Faker()

__all__ = ('data',)

data = {}

for i in range(50):
    data.update({
        i: Foo(
            id=i,
            title=faker.sentence(nb_words=3, variable_nb_words=False),
            text=faker.text(),
            context_text=faker.text()
        ),
    })
