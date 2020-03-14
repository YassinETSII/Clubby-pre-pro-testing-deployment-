% Prepare to release
release: sh -c 'cd djangoapp && python manage.py migrate'
% Launch
web: sh -c 'cd djangoapp && gunicorn clubby.wsgi --log-file -'
