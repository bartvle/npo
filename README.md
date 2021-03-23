# Natuurpunt Oosterzele

Runs on Python 3.8 and Django 3.1!


## Installation

With conda

```
conda create -n npo python=3.8
conda activate npo
conda install django gunicorn
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
python manage.py migrate --database=postgres
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
