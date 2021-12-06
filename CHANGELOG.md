# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.5.0) - 2021-12-06
-   Added `samples` options support.

## [0.4.5](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.5) - 2021-10-12
-   Fixed widget backward-compatibility with older django versions.

## [0.4.4](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.4) - 2021-10-08
-   Fixed widget backward-compatibility with older django versions.

## [0.4.3](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.3) - 2021-09-16
-   Fixed subclasses of `forms.Widget` must provide a `render()` method. #70

## [0.4.2](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.2) - 2021-07-12
-   Fixed disable colorfield in `ModelForm` (thanks to [@rcatajar](https://github.com/rcatajar)). #67 #69

## [0.4.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.1) - 2021-01-19
-   Fixed 500 error caused by palette `choices`. #65

## [0.4.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.4.0) - 2021-01-14
-   Added `hex` (default) and `hexa` color format support. #58 #59
-   Added palette support using field `choices`. #19
-   Updated `jscolor` library version to `2.4.5`.

## [0.3.2](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.3.2) - 2020-07-07
-   Used `load` event instead of `window.onload` callback.

## [0.3.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.3.1) - 2020-06-17
-   Updated jscolor to 2.1.1 version. #57
-   Fixed self invoking anonymous function expression.

## [0.3.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.3.0) - 2020-04-07
-   Fixed `default`, `blank` and `null` attrs support. #53 #54
-   Fixed `jscolor` not working on inlines added dynamically (only when `extra=0`)

## [0.2.2](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.2.2) - 2020-04-02
-   Fixed colopicker not working on inlines added dynamically (only when `jquery` is loaded by the browser after `colorfield`). #52

## [0.2.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.2.1) - 2020-02-21
-   Fixed colopicker not working on inlines added dynamically.
-   Fixed failed lookup for key [class]. #7

## [0.2.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.2.0) - 2020-02-17
-   Fixed whole inline model required. #7
-   Fixed `README.md` missing in package. #46
-   Refactored `ColorField` and `ColorWidget`. #39, #43
-   Updated `jscolor` version to `2.0.5`.
-   Bumped min `django` version to `1.7`.
-   Added test suite *(not tests)* with `tox` and `travis`.

## 0.1.16
-   Remove warnings about `ugettext_lazy` usage.

## 0.1.13
-   Use not minified jscolor when `DEBUG=true`
-   Fix rendering when `value is None`
-   Use `{required: false}` js color option when the form field is not required. This forces to stop using the `{hash: true}` option for jscolor. To make this change retrocompatible, anchor is appended at the `Widget` level.
