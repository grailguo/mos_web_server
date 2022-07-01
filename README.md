# MOS Web Server

cd mos_web_server
python ../manage.py startapp erecto
python ../manage.py startapp reparo
python ../manage.py startapp accio
python ../manage.py startapp flagrate

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata --app users data
python manage.py runserver

python manage.py loaddata --app users data
python manage.py loaddata --app erecto data
python manage.py loaddata --app reparo data

python manage.py loaddata --app accio 101_cartridge.json
python manage.py loaddata --app accio 102_compound.json
python manage.py loaddata --app accio 103_compoundcodecounter.json
python manage.py loaddata --app accio 104_cartridge_compound.json
python manage.py loaddata --app accio 105_compoundtag.json
python manage.py loaddata --app accio 106_compound_compound_tag.json
python manage.py loaddata --app accio 107_experiment.json
python manage.py loaddata --app accio 108_spectrumtag.json
python manage.py loaddata --app accio 109_spectrum.json
python manage.py loaddata --app accio 110_spectrum_spectrum_tag.json
python manage.py loaddata --app accio 111_quantmethod.json
python manage.py loaddata --app accio 112_quantmethodcodecounter.json
python manage.py loaddata --app accio 113_cartridge_quant_method.json

python manage.py loaddata --app flagrate data


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy mos_web_server

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
