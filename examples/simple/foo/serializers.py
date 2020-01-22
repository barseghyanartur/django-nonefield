from rest_framework import serializers

from nonefield.contrib.drf_integration.fields import NoneField

from .models import Foo, Bar


__all__ = (
    'FooSerializer',
    'BarSerializer',
)


class ContentTextField(NoneField):
    """Content text field."""


class FooSerializer(serializers.ModelSerializer):

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
        fields = '__all__'


class BarSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    text = serializers.CharField()
    context_text = ContentTextField(label='', default='Haha')
    url = serializers.HyperlinkedIdentityField(
        view_name='barapi-detail',
        read_only=True
    )

    class Meta:

        model = Bar

    def pk(self):
        return self.id

    def create(self, validated_data):
        print(validated_data)
        return Bar(id=None, **validated_data)

    def update(self, instance, validated_data):
        # import ipdb; ipdb.set_trace()
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
