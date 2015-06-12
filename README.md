#

## deploy to heroku

```
python manage.py dumpdata --format=json --indent=4 > atelier/fixtures/init_data.json
```

```
heroku create atelier-proto
heroku run python manage.py migrate
heroku run python manage.py loaddata atelier/fixtures/init_data.json
```

```
heroku apps:destroy --app atelier-proto --confirm atelier-proto
```
