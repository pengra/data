. secrets.sh
cd $SERVER_LOCATION
source "env/bin/activate"
cd "src"
python manage.py collectstatic --no-input
gunicorn --workers=3 -b 127.0.0.1:9997 data.wsgi:application
