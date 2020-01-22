from django.urls import reverse
from rest_framework import serializers

from nonefield.contrib.drf_integration.fields import NoneField

from .models import Foo


__all__ = ('FooSerializer',)


class ContentTextField(NoneField):
    """Content text field."""


class FooSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    text = serializers.CharField()
    context_text = ContentTextField(label='', default='Haha')
    url = serializers.HyperlinkedIdentityField(
        view_name='fooapi-detail',
        read_only=True
    )

    class Meta:

        model = Foo

    def pk(self):
        return self.id

    def create(self, validated_data):
        print(validated_data)
        return Foo(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
