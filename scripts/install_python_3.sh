pip install -r examples/requirements.txt
pip install -r examples/requirements3.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static
python examples/simple/manage.py collectstatic --noinput
python examples/simple/manage.py syncdb --noinput
python examples/simple/manage.py migrate --noinput