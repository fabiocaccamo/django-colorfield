[![PyPI version](https://badge.fury.io/py/django-colorfield.svg)](https://badge.fury.io/py/django-colorfield)

# django-colorfield

This module fills the need of having a **colorfield** that's usable in both
django models and forms.

![django-colorfield](https://cloud.githubusercontent.com/assets/1035294/11273806/a015270a-8ed5-11e5-8546-1fd4cc241266.png)

Makes use of [spectrum](https://bgrins.github.io/spectrum/), and previous versions used [jscolor](http://jscolor.com/).

## Installation
- Run ``pip install django-colorfield``
- Add ``colorfield`` to your ``INSTALLED_APPS``
- Collect static files with ``./manage.py collectstatic``

## Usage
In your models, you can use it like this:

```python
from django.db import models
from colorfield.fields import ColorField

class MyModel(model.Model):
    
    color = ColorField(default='#FF0000')
```

In your `settings.py`, you can optionally set a pre-determined list of colors, or change the default:

```
COLORFIELD_DEFAULT = "darkturquoise"
COLORFIELD_PALETTE = ["blue", "green", "yellow","orange", "magenta", "red"]
```

To see an example application with and without these settings, [follow the instructions here](example/README.md).


## Maintainers
- [@gtnx](https://github.com/gtnx)
- [@fabiocaccamo](https://github.com/fabiocaccamo)
- See the [CONTRIBUTORS.md](CONTRIBUTORS.md) for additional contributors


## License

The MIT License (MIT)

Copyright (c) 2013-2015 Jared Forsyth <jared@jaredforsyth.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
