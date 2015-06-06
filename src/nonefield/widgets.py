__title__ = 'nonefield.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('NoneWidget',)

from django.forms.widgets import Widget
from django.utils.safestring import mark_safe

class NoneWidget(Widget):
    """
    To be used with content elements.
    """
    def render(self, name, value, attrs=None):
        """
        """
        return mark_safe(value)
