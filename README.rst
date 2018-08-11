================
django-nonefield
================
``django-nonefield`` is a None field for Django.

Prerequisites
=============
- Django 1.8, 1.9, 1.10, 1.11, 2.0, 2.1.
- Python 2.7, 3.5, 3.6, 3.7

Installation
============

(1) Install latest stable version from PyPI:

    .. code-block:: sh

        pip install django-nonefield

    Or latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/django-nonefield/archive/stable.tar.gz

    Or latest stable version from BitBucket:

    .. code-block:: sh

        pip install https://bitbucket.org/barseghyanartur/django-fobi/get/stable.tar.gz

(2) Add ``nonefield`` to ``INSTALLED_APPS`` of the your projects' Django
    settings.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            # None field
            'nonefield',
            # ...
        )

Usage
=====
forms.py
--------
.. code-block:: python

    from django import forms
    from nonefield.fields import NoneField

    class MyForm(forms.Form):

        name = forms.CharField(max_length=255)
        some_text = NoneField(initial='Lorem ipsum')

Examples
========
- `example 1 <https://gist.github.com/barseghyanartur/c6e0123dd961fbac1b39>`_
- `example 2
  <https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/plugins/form_elements/content/content_text/fobi_form_elements.py>`_

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
