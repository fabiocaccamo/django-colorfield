# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.16
-   Remove warnings about `ugettext_lazy` usage.

## 0.1.13
-   Use not minified jscolor when `DEBUG=true`
-   Fix rendering when `value is None`
-   Use `{required: false}` js color option when the form field is not required. This forces to stop using the `{hash: true}` option for jscolor. To make this change retrocompatible, anchor is appended at the `Widget` level.
