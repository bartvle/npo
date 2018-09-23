# Natuurpunt Oosterzele

Runs on Python 3.5 and Django 2.0!


## Installation

With conda

```
conda install -c conda-forge gunicorn django bokeh
```

With pip

```
pip install django-analytical
```


## Migration

First run locally

```
python manage.py makemigrations
```

then run on server

```
python manage.py migrate
```


## Translation

First run

```
python manage.py makemessages -l nl_BE
```

then translate and run

```
python manage.py compilemessages
```
