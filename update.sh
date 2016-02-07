git pull
yes yes | /var/www/lancer/lancer-git/venv/bin/python ./manage.py collectstatic
kill -HUP `pgrep gunicorn`

