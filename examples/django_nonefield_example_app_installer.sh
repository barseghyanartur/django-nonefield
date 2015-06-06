wget -O django_nonefield_example_app_installer.tar.gz https://github.com/barseghyanartur/django-nonefield/archive/stable.tar.gz
virtualenv nonefield
source nonefield/bin/activate
mkdir django_nonefield_example_app_installer/
tar -xvf django_nonefield_example_app_installer.tar.gz -C django_nonefield_example_app_installer
cd django_nonefield_example_app_installer/django-nonefield-stable/example/example/
pip install Django
pip install -r ../requirements.txt
pip install -e git+https://github.com/barseghyanartur/django-nonefield@stable#egg=django-nonefield
mkdir ../media/
mkdir ../media/static/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp local_settings.example local_settings.py
./manage.py syncdb --noinput --traceback -v 3
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py runserver 0.0.0.0:8001 --traceback -v 3