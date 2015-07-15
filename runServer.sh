#!/bin/bash
watchmedo shell-command --patterns="*.py;*.html;*.css;*.js" --recursive --command='echo "${watch_src_path}" && kill -HUP `cat gunicorn.pid`' . &
# python manage.py run_gunicorn 127.0.0.1:80 --pid=gunicorn.pid
gunicorn app:app -b localhost:8000 --pid=gunicorn.pid
