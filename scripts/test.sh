reset
./scripts/uninstall.sh
./scripts/install.sh
python examples/simple/manage.py test nonefield --settings=settings_test
