# Atelier Proto

Prototype of Palody Artwork Atelier.

## setup

### initial

```bash
$ git clone https://github.com/ohbarye/atelier-proto.git
$ cd atelier-proto
$ virtualenv env
$ source env/bin/activate
(env)$ pip install -e .

# if data file does not exist
(env)$ python manage.py migrate
# if data is not loaded
(env)$ python manage.py loaddata atelier/fixtures/init_data.json

(env)$ python manage.py runserver
```

### browse

```bash
# on other terminal
$ open http://localhost:8000/atelier/
$ open http://localhost:8000/atelier/class/
$ open http://localhost:8000/atelier/classList/
```

### sql

#### raw sql

```sql
$ sqlite3 db.sqlite3
sqlite> .tables
atelier_album               auth_user
atelier_albumartworkclass   auth_user_groups
atelier_artist              auth_user_user_permissions
atelier_artworkclass        django_admin_log
auth_group                  django_content_type
auth_group_permissions      django_migrations
auth_permission             django_session
sqlite>
sqlite> select * from atelier_album where name = 'The Bends';
459|The Bends|829||http://artwork-cdn.7static.com/static/img/sleeveart/00/000/008/0000000829_350.jpg|1662
```

#### sql from django models

```python
$ python manage.py shell
>>> from atelier.models import *
>>> Album.objects.all()
[<Album: The Show, The After Party, The Hotel>, <Album: Best Of Wishbone Ash>, '...(remaining elements truncated)...']
>>>
>>> Album.objects.get(id=12)
<Album: Wild Wood>
>>>
>>> Album.objects.filter(name='The Bends')
[<Album: The Bends>]
>>>
```




## deploy to heroku


### dump data

```bash
$ python manage.py dumpdata --format=json --indent=4 > atelier/fixtures/init_data.json

```

### create app - load data

```bash
$ heroku create atelier-proto
$ heroku run python manage.py migrate
$ heroku run python manage.py loaddata atelier/fixtures/init_data.json
```

### destroy app

```bash
$ heroku apps:destroy --app atelier-proto --confirm atelier-proto
```
