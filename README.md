Welcome to ToyNet Django!

MacOS local setup
```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd engine
python3 ./manage.py run
export SECRET_KEY='iamnotaverysecretkey'
```

Local admin access at http://127.0.0.1:8000/admin/
```
python3 ./manage.py createsuperuser

python3 ./manage.py runserver
> Username (leave blank to use 'tay'): admin
> Email address: admin@admin.com
> Password: xxx
```

The `data/` [path](https://github.com/Project-Reclass/toynet-django/blob/54ca2b394b2b1eb0b265635d2235c563edb0015c/engine/engine/urls.py#L24) points to [viewsets](https://github.com/Project-Reclass/toynet-django/blob/54ca2b394b2b1eb0b265635d2235c563edb0015c/engine/api/viewset/router.py)

http://127.0.0.1:8000/data/toynetsession
http://127.0.0.1:8000/data/toynetconfig

side notes:
```
python manage.py migrate
```
