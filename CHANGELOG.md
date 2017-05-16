# Changelog

## 0.1.13

- Use not minified jscolor when `DEBUG=true`
- Fix rendering when `value is None`
- Use `{required: false}` js color option when the form field is not required. This forces to stop using the `{hash: true}` option for jscolor. To make this change retrocompatible, anchor is appended at the `Widget` level. 
