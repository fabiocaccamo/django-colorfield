# django-colorfield-example

You can use the app and corresponding Dockerfile to preview Django Colorfield.
To build and run the image:

```
docker-compose build
docker-compose up -d
```

This is the example Django polls app with fields that demonstrate the colorfield.
Open to your browser at [127.0.0.1:8000](http://127.0.0.1:8000), and click the
button to create the example polls:

**note** I can't seem to get colorfield to install cleanly, meaning having all templates and static files found by Django. If Django needs custom configuration, this needs to be documented. It's also not clear how to interact with the field in the form, or how to grab the color after getting it.
