================
django-nonefield
================
`django-nonefield` is a None field for Django.

Prerequisites
=============
- Django 1.5, 1.6, 1.7, 1.8
- Python 2.6.8+, 2.7, 3.3

Installation
============

1. Install latest stable version from PyPI::

    $ pip install django-nonefield

   Or latest stable version from GitHub::

    $ pip install -e git+https://github.com/barseghyanartur/django-nonefield@stable

   Or latest stable version from BitBucket::

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/django-nonefield@stable

2. Add `nonefield` to ``INSTALLED_APPS`` of the your projects' Django settings.

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
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>

Documentation
===============================================
Contents:

.. toctree::
   :maxdepth: 20

   nonefield

Indices and tables
===============================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

