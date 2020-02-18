[![](https://img.shields.io/pypi/pyversions/django-colorfield.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-colorfield?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-colorfield.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-colorfield/)
[![](https://pepy.tech/badge/django-colorfield)](https://pepy.tech/project/django-colorfield)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-colorfield?logo=github)](https://github.com/fabiocaccamo/django-colorfield/)
[![](https://img.shields.io/pypi/l/django-colorfield.svg?color=blue)](https://github.com/fabiocaccamo/django-colorfield/blob/master/LICENSE.txt)

[![](https://img.shields.io/travis/fabiocaccamo/django-colorfield?logo=travis&label=build)](https://travis-ci.org/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-colorfield?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codacy/grade/194566618f424a819ce43450ea0af081?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-colorfield?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-colorfield/)
[![](https://requires.io/github/fabiocaccamo/django-colorfield/requirements.svg?branch=master)](https://requires.io/github/fabiocaccamo/django-colorfield/requirements/?branch=master)

# django-colorfield
simple color field for your models with a nice color-picker in the admin-interface.

![django-colorfield](https://user-images.githubusercontent.com/1035294/74674565-f33ace00-51b1-11ea-8669-4b952f2b8e56.png)

## Installation
-   Run `pip install django-colorfield`
-   Add `colorfield` to `settings.INSTALLED_APPS`
-   Run `python manage.py collectstatic`
-   Restart your application server

## Usage

### Settings
This package doesn't need any setting.

### Models
Just add color field(s) to your models like this:

```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(model.Model):
    color = ColorField(default='#FF0000')
```

### Admin
The admin will kindly provide a simple [color picker](http://jscolor.com/) for all color fields. :)

## Testing
```bash
# create python 3.8 virtual environment
virtualenv testing_django_colorfield -p "python3.8" --no-site-packages

# activate virtualenv
cd testing_django_colorfield && . bin/activate

# clone repo
git clone https://github.com/fabiocaccamo/django-colorfield.git src && cd src

# install dev requirements
pip install tox

# run tests
tox
# or
python setup.py test
# or
python manage.py test --settings "tests.settings"
```

## Credits
Originally developed by [Jared Forsyth](https://github.com/jaredly)

---

## License
Released under [MIT License](LICENSE.txt).
