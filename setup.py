import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    readme = readme.replace('.. code-block:: none', '.. code-block::')
except:
    readme = ''

version = '0.4'

install_requires = [
    'django-nine>=0.1.13',
]

try:
    PY2 = sys.version_info[0] == 2
    LTE_PY26 = PY2 and (7 > sys.version_info[1])
    PY3 = sys.version_info[0] == 3
except:
    pass

setup(
    name='django-nonefield',
    version=version,
    description="A None field for Django.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords='forms, django, none field, django rest framework',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/django-nonefield/',
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/django-nonefield/",
        "Documentation": "https://django-nonefield.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/django-nonefield/",
        "Changelog": "https://django-nonefield.readthedocs.io/"
                     "en/latest/changelog.html",
    },
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL-2.0-only OR LGPL-2.1-or-later',
    install_requires=install_requires,
)
