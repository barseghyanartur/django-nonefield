pip install -r examples/requirements_django_1_6.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static
python examples/simple/manage.py collectstatic --noinput --traceback -v 3
python examples/simple/manage.py syncdb --noinput --traceback -v 3
python examples/simple/manage.py migrate --noinput --traceback -v 3