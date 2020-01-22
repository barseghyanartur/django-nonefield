from django import forms

from nonefield.fields import NoneField
from nonefield.widgets import NoneWidget

from foo.constants import INITIAL_VALUE


class MyForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    value = NoneField(initial=INITIAL_VALUE)
