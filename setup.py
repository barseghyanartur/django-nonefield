import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    readme = readme.replace('.. code-block:: none', '.. code-block::')
except:
    readme = ''

version = '0.1'

install_requires = [
]

try:
    PY2 = sys.version_info[0] == 2
    LTE_PY26 = PY2 and (7 > sys.version_info[1])
    PY3 = sys.version_info[0] == 3
except:
    pass

setup(
    name = 'django-nonefield',
    version = version,
    description = ("A None field for Django."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    keywords = 'forms, django, none field, django none field',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/django-nonefield/',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires,
)
