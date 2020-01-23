from django.forms.fields import Field

from .widgets import NoneWidget

__title__ = 'nonefield.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2020 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('NoneField',)


class NoneField(Field):
    """NoneField.

    To be used with content elements like text or images, that need to be
    present, for instance, in between form input elements.
    """
    widget = NoneWidget

    def bound_data(self, data, initial):
        """Bound data.

        Return the value that should be shown for this field on render of a
        bound form, given the submitted POST data for the field and the initial
        data, if any.

        For most fields, this will simply be data; FileFields need to handle it
        a bit differently.
        """
        return initial

    def validate(self, value):
        """Validate.

        Always return True (by definition).
        """
        return True

    def clean(self, value):
        return self.initial
