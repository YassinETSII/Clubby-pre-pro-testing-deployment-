% Prepare to release
release: sh -c 'cd project && python manage.py migrate && python manage.py'
% Launch!
web: sh -c 'cd project && gunicorn clubby.wsgi --log-file -'
