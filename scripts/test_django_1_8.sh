reset
./scripts/uninstall.sh
./scripts/install_django_1_8.sh
python examples/simple/manage.py test nonefield --settings=settings_django_1_8 --traceback -v 3