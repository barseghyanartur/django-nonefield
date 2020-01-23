import six

from django.utils.safestring import mark_safe

from rest_framework.fields import empty, Field

__title__ = 'nonefield.contrib.drf_integration.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2020 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'NoneField',
)


class NoneField(Field):
    """NoneField."""

    default_error_messages = {}
    initial = ''
    default_empty_html = ''

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = kwargs.pop('trim_whitespace', True)
        self.raw_data = kwargs.pop('raw_data', {})
        kwargs.update({
            'required': False,
            'read_only': True,
        })
        super(NoneField, self).__init__(**kwargs)

    def run_validation(self, data=empty):
        return ''

    def to_internal_value(self, data):
        # We're lenient with allowing basic numerics to be coerced into
        # strings, but other types should fail. Eg. unclear if booleans
        # should represent as `true` or `True`, and composites such as lists
        # are likely user error.
        _not_isinstance_str_int_float = not isinstance(
            data, six.string_types + six.integer_types + (float,)
        )
        if isinstance(data, bool) or _not_isinstance_str_int_float:
            self.fail('invalid')
        value = six.text_type(data)
        return value.strip() if self.trim_whitespace else value

    def to_representation(self, value):
        return mark_safe(six.text_type(value))
