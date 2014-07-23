**Notice:** I no longer use django on a day-to-day basis (actually, it's been several years), and am **not actively maintaining this module**. If you would like to take over, please let me know. If you find a bug and file a pull request, I'll happily accept it.

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
