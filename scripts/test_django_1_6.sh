reset
./scripts/uninstall.sh
./scripts/install_django_1_6.sh
python examples/simple/manage.py test nonefield --traceback -v 3