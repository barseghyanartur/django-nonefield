from django.forms.widgets import Widget
from django.utils.safestring import mark_safe

__title__ = 'nonefield.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2020 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'NoneWidget',
)


class NoneWidget(Widget):
    """NoneWidget.

    To be used with content elements.
    """

    def render(self, name, value, attrs=None, **kwargs):
        """Render."""
        return mark_safe(value)
