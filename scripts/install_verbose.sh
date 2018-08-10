pip install -r examples/requirements.txt
python setup.py install
mkdir examples/logs
mkdir examples/db
mkdir examples/media
mkdir examples/media/static
python examples/simple/manage.py collectstatic --noinput
python examples/simple/manage.py syncdb --noinput
python examples/simple/manage.py migrate --noinput