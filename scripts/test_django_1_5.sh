reset
./scripts/uninstall.sh
./scripts/install_django_1_5.sh
python examples/simple/manage.py test nonefield --traceback -v 3