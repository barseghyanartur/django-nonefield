from rest_framework.viewsets import ModelViewSet

from .models import Foo, Bar
from .serializers import FooSerializer, BarSerializer

__all__ = (
    'FooViewSet',
    'BarViewSet',
)


class FooViewSet(ModelViewSet):

    serializer_class = FooSerializer
    queryset = Foo.objects.all()


class BarViewSet(ModelViewSet):

    serializer_class = BarSerializer
    queryset = Bar.objects.all()

    def get_object(self):
        try:
            return Bar.objects.get(pk=int(self.kwargs.get('pk')))
        except IndexError:
            pass
