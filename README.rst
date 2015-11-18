Django Colorfield
---------------------

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Makes use of http://jscolor.com/.


Installation
============

Add `colorfield` to your `INSTALLED_APPS`.

Collect static files with ``./manage.py collectstatic``.

Then in your models, you can use it like this:

.. code-block:: python

    from django.db import models
    from colorfield.fields import ColorField

    class Show(ExtendedModel):
        title = models.CharField(u'Title', max_length=250)
        color = ColorField()

Maintainers:
============
- @gtnx
- @fabiocaccamo
