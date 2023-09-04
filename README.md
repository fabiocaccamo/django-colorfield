[![](https://img.shields.io/pypi/pyversions/django-colorfield.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-colorfield?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-colorfield.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-colorfield/)
[![](https://pepy.tech/badge/django-colorfield/month)](https://pepy.tech/project/django-colorfield)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-colorfield?logo=github)](https://github.com/fabiocaccamo/django-colorfield/stargazers)
[![](https://img.shields.io/pypi/l/django-colorfield.svg?color=blue)](https://github.com/fabiocaccamo/django-colorfield/blob/main/LICENSE.txt)

[![](https://results.pre-commit.ci/badge/github/fabiocaccamo/django-colorfield/main.svg)](https://results.pre-commit.ci/latest/github/fabiocaccamo/django-colorfield/main)
[![](https://img.shields.io/github/actions/workflow/status/fabiocaccamo/django-colorfield/test-package.yml?branch=main&label=build&logo=github)](https://github.com/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-colorfield?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codacy/grade/194566618f424a819ce43450ea0af081?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-colorfield)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-colorfield?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-colorfield/)
[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# django-colorfield
simple color field for your models with a nice color-picker in the admin-interface.

![django-colorfield-hex](https://user-images.githubusercontent.com/7900305/104512324-51ed0f80-55ee-11eb-9144-de03d922c2ce.png)
![django-colorfield-hexa](https://user-images.githubusercontent.com/7900305/104512063-ec991e80-55ed-11eb-95b6-9174ac3f4f38.png)

---

## Installation
-   Run `pip install django-colorfield`
-   Add `colorfield` to `settings.INSTALLED_APPS`
-   Run `python manage.py collectstatic`
-   Restart your application server

---

## Usage

### Settings
This package doesn't need any setting.

### Models
Just add color field(s) to your models like this:

```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    color = ColorField(default='#FF0000')
```

### Field Options
These are the supported custom options: [`format`](#format), [`image_field`](#image_field), [`samples`](#samples)

#### format

The following formats are supported: `hex` *(default)*, `hexa`, `rgb`, `rgba`.

```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    color = ColorField(format="hexa")
```

#### image_field

It is possible to auto-populate the field value getting the color from an image using the `image_field` option.

The color will be calculated from the **top-left pixel** color of the image each time the model instance is saved.

```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to="images")
    color = ColorField(image_field="image")
```

#### samples

It is possible to provide a palette of colors to choose from to the widget using the `samples` option.

This option **is not restrictive** (on the contrary of `choices` option), it is also possible to choose another color from the spectrum.

![django-colorfield-samples](https://user-images.githubusercontent.com/7900305/104512178-194d3600-55ee-11eb-8cba-91cca156da06.png)

```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):

    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    # not restrictive, allows the selection of another color from the spectrum.
    color = ColorField(samples=COLOR_PALETTE)

    # restrictive, it is mandatory to choose a color from the palette
    color = ColorField(choices=COLOR_PALETTE)
```

### Admin
The admin will kindly provide a simple [color picker](http://jscolor.com/) for all color fields. :)

---

## Testing
```bash
# clone repository
git clone https://github.com/fabiocaccamo/django-colorfield.git && cd django-colorfield

# create virtualenv and activate it
python -m venv venv && . venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt -r requirements-test.txt

# install pre-commit to run formatters and linters
pre-commit install --install-hooks

# run tests
tox
# or
python runtests.py
# or
python -m django test --settings "tests.settings"
```
---

## Credits
Originally developed by [Jared Forsyth](https://github.com/jaredly)

---

## License
Released under [MIT License](LICENSE.txt).

---

## Supporting

- :star: Star this project on [GitHub](https://github.com/fabiocaccamo/django-colorfield)
- :octocat: Follow me on [GitHub](https://github.com/fabiocaccamo)
- :blue_heart: Follow me on [Twitter](https://twitter.com/fabiocaccamo)
- :moneybag: Sponsor me on [Github](https://github.com/sponsors/fabiocaccamo)

## See also

- [`django-admin-interface`](https://github.com/fabiocaccamo/django-admin-interface) - the default admin interface made customizable by the admin itself. popup windows replaced by modals. 🧙 ⚡

- [`django-extra-settings`](https://github.com/fabiocaccamo/django-extra-settings) - config and manage typed extra settings using just the django admin. ⚙️

- [`django-maintenance-mode`](https://github.com/fabiocaccamo/django-maintenance-mode) - shows a 503 error page when maintenance-mode is on. 🚧 🛠️

- [`django-redirects`](https://github.com/fabiocaccamo/django-redirects) - redirects with full control. ↪️

- [`django-treenode`](https://github.com/fabiocaccamo/django-treenode) - probably the best abstract model / admin for your tree based stuff. 🌳

- [`python-benedict`](https://github.com/fabiocaccamo/python-benedict) - dict subclass with keylist/keypath support, I/O shortcuts (base64, csv, json, pickle, plist, query-string, toml, xml, yaml) and many utilities. 📘

- [`python-codicefiscale`](https://github.com/fabiocaccamo/python-codicefiscale) - encode/decode Italian fiscal codes - codifica/decodifica del Codice Fiscale. 🇮🇹 💳

- [`python-fontbro`](https://github.com/fabiocaccamo/python-fontbro) - friendly font operations. 🧢

- [`python-fsutil`](https://github.com/fabiocaccamo/python-fsutil) - file-system utilities for lazy devs. 🧟‍♂️
