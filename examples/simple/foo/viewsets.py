from rest_framework.viewsets import ModelViewSet

from .models import Foo
from .serializers import FooSerializer
from .data import data

__all__ = ('FooViewSet',)


class FooViewSet(ModelViewSet):

    serializer_class = FooSerializer
    queryset = [_d for _d in data.values()]

    def get_object(self):
        try:
            return self.queryset[int(self.kwargs.get('pk'))]
        except IndexError:
            pass
