import unittest

from django import forms
from django.test import RequestFactory, TestCase
from nine.versions import DJANGO_GTE_1_11

from ..fields import NoneField
from .base import log_info
from .constants import (
    ENDPOINT_URL,
    INITIAL_NONEFIELD_VALUE,
    CHANGED_NONEFIELD_VALUE,
)

__all__ = ('NoneFieldTest',)
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'


class MyForm(forms.Form):
    """Test form."""

    name = forms.CharField(required=True)
    static_text = NoneField(initial=INITIAL_NONEFIELD_VALUE)


class NoneFieldTest(TestCase):
    """Test the django-nonefield package."""

    def setUp(self):
        """Set up.

        :return:
        """

    @log_info
    def test_01_nonefield(self):
        """Test `nonefield.fields.NoneField`."""
        request_factory = RequestFactory()
        request = request_factory.post(
            ENDPOINT_URL,
            data={
                'name': "John Doe",
                'static_text': CHANGED_NONEFIELD_VALUE
            }
        )

        form = MyForm(
            data=request.POST,
            initial={'static_text': INITIAL_NONEFIELD_VALUE}
        )

        self.assertTrue(form.is_valid())
        form_as_p = form.as_p()

        expected_output = """
        <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name" value="John Doe" required id="id_name">
        </p>
        <p>
        <label for="id_static_text">Static text:</label>
        Lorem ipsum
        </p>
        """

        if not DJANGO_GTE_1_11:
            expected_output = expected_output.replace('required', '')

        self.assertHTMLEqual(
            form_as_p,
            expected_output
        )

        self.assertEqual("John Doe", form.cleaned_data['name'])
        self.assertEqual(INITIAL_NONEFIELD_VALUE,
                         form.cleaned_data['static_text'])


if __name__ == '__main__':
    unittest.main()
