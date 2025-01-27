# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.12.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.12.0) - 2025-01-27
-   Support plain Django forms. #211
-   Bump requirements.
-   Bump `pre-commit` hooks.
-   Bump actions.

## [0.11.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.11.0) - 2023-12-05
-   Add `Python 3.12` support.
-   Add `Django 5.0` support.
-   Speed-up test workflow.
-   Bump requirements.
-   Bump `pre-commit` hooks.

## [0.10.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.10.1) - 2023-09-05
-   Fix crash when using `image_field` option with `RGB`/`RGBA` formats. #153 (by [@browniebroke](https://github.com/browniebroke) in #154)
-   Fix field `max_length` (increased from `18` to `25`).

## [0.10.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.10.0) - 2023-09-04
-   Add support for `RGB` and `RGBA` formats. (by [@browniebroke](https://github.com/browniebroke) in #151)
-   Fix typos in code snippets from `README`. (by [@browniebroke](https://github.com/browniebroke) in #152)
-   Fix warnings in browser console when using `ColorWidget` without specifying format. (by [@fallen](https://github.com/fallen) in #145)
-   Bump requirements.

## [0.9.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.9.0) - 2023-06-13
-   Add `Django 4.2` support.
-   Drop `Django 2.2` support.
-   Add `pyupgrade` and `django-upgrade` to `pre-commit` hooks.
-   Upgrade syntax for `Python >= 3.8`.
-   Set max line length to `88`.
-   Switch from `setup.py` to `pyproject.toml`.
-   Replace `flake8` with `Ruff`.
-   Add locales (`en` and `it`).
-   Add `metadata` module.
-   Set max line length to `88`.
-   Run `pre-commit` also with `tox`.
-   Bump requirements.
-   Pin test requirements.
-   Rename default branch from `master` to `main`.

## [0.8.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.8.0) - 2022-12-02
-   Drop `Python < 3.8` and `Django < 2.2` support.

## [0.7.3](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.7.3) - 2022-12-02
-   Handle possible corrupted image when opening image. #98

## [0.7.2](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.7.2) - 2022-07-19
-   Fixed options not working when not using `palette` (choices/samples). #80 (by [@jan-szejko-steelseries](https://github.com/jan-szejko-steelseries) in #81)

## [0.7.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.7.1) - 2022-06-08
-   Fixed `ColorField` widget classes. #43 #78 (thanks to [@N1K1TAS95](https://github.com/N1K1TAS95))

## [0.7.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.7.0) - 2022-05-13
-   Added `ColorField` serializer. #77 (thanks to [@hugofer93](https://github.com/hugofer93))

## [0.6.3](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.6.3) - 2022-01-03
-   Fixed django < 2.0 compatibility.

## [0.6.2](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.6.2) - 2022-01-03
-   Fixed possible memory leak.

## [0.6.1](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.6.1) - 2022-01-03
-   Fixed `ValueError: seek of closed file`. #75

## [0.6.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.6.0) - 2021-12-22
-   Added `image_field` option.
-   Added `python 3.10` / `django 4.0` support.
-   Added more tests and increased coverage.
-   Fixed tests warnings.
-   Replaced Travis CI with GitHub actions workflow.

## [0.5.0](https://github.com/fabiocaccamo/django-colorfield/releases/tag/0.5.0) - 2021-12-06
-   Added `samples` option support.

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
