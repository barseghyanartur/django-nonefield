Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.4
---
2020-01-23 (not yet released)

- Added Django REST Framework contrib.
- Tested against Django 2.2 and 3.0.
- Tested against Python 3.8.

0.3
---
2018-08-11

- Django 2.1 (and below) support.

0.2
---
2016-05-17

- Add ``NoneField`` for Django REST framework.

0.1
---
2015-06-07

- Initial release.
