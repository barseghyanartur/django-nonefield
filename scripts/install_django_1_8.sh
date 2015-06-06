pip uninstall south -y
pip install -r examples/requirements_django_1_8.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static
python examples/simple/manage.py collectstatic --noinput --settings=settings_django_1_8 --traceback -v 3
python examples/simple/manage.py syncdb --noinput --settings=settings_django_1_8 --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings_django_1_8 --traceback -v 3