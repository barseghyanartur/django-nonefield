================
django-nonefield
================
``django-nonefield`` is a None field for Django.

A typical use case: allow presentational (non-input, non-field) form
elements (text, image, embed video, etc). This could be very useful if your
forms are dynamic (as in form-builders/generators). Django REST Framework
integration is implemented as well.

.. image:: https://img.shields.io/pypi/v/django-nonefield.svg
   :target: https://pypi.python.org/pypi/django-nonefield
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/django-nonefield.svg
    :target: https://pypi.python.org/pypi/django-nonefield/
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/barseghyanartur/django-nonefield/master.svg
   :target: http://travis-ci.org/barseghyanartur/django-nonefield
   :alt: Build Status

.. image:: https://readthedocs.org/projects/django-nonefield/badge/?version=latest
    :target: http://django-nonefield.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/django-nonefield/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/django-nonefield/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/barseghyanartur/django-nonefield?branch=master
    :alt: Coverage

Prerequisites
=============
- Django 1.8, 1.11, 2.0, 2.1, 2.2, 3.0.
- Python 2.7, 3.5, 3.6, 3.7, 3.8

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
In forms you could use it as follows:

.. code-block:: python

    from django import forms
    from nonefield.fields import NoneField

    class MyForm(forms.Form):

        name = forms.CharField(max_length=255)
        some_text = NoneField(initial='Lorem ipsum')

See `this snippet <https://gist.github.com/barseghyanartur/c6e0123dd961fbac1b39>`__
as an example of how to allow to use paragraphs in the `django-forms-builder`.

serializers.py
--------------
You can also use it in Django REST Framework.

.. code-block:: python

    from rest_framework import serializers
    from nonefield.contrib.drf_integration.fields import NoneField


    class ContentTextField(NoneField):
        """Content text field."""

    class BarSerializer(serializers.Serializer):

        title = serializers.CharField(max_length=256)
        text = serializers.CharField()
        context_text = ContentTextField(label='', default='Haha')

See `how it's used in django-fobi
<https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/plugins/form_elements/content/content_text/fobi_form_elements.py>`__
to allow to use content/presentational elements (text, image, embed video, etc.)
in the Django REST Framework schema.

Examples
========
- `django-forms-builder example <https://gist.github.com/barseghyanartur/c6e0123dd961fbac1b39>`_
- `django-fobi form elements example <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/content>`__
- `django-fobi DRF integration example
  <https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/plugins/form_elements/content/content_text/fobi_form_elements.py>`_

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>

Project documentation
=====================
Contents:

.. toctree::
   :maxdepth: 20

   index
   changelog
   nonefield

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

