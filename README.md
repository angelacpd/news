## NEWS

News website made with Django Framework.

Characteristics:
- Authentication: Django authentication
- Frontend: Bootstrap
- Database: SQLite
- Email system: SendGrid

Project based on book *Django for Beginners* by William S. Vincent.


## Managing dependencies

This project uses pipenv.

* Install dependencies from Pipfile.lock

> pipenv install --ignore-pipfile

* Add new package

> pipenv install <package> --keep-outdated

## Email setup

* Create an account on SendGrid. Use a different email than createsuperuser.
* On SendGrid, go to *API Keys* and create a key. Copy the key.

## Environment variables

* Check `.env-example` to add the required configuration.
* Create file `.env` and add the variables of `.env-example`.

## Apply migrations

> python manage.py migrate

## Create superuser

> python manage.py cretesuperuser

## Run unit tests

> python manage.py test

## Run locally

> python manage.py runserver