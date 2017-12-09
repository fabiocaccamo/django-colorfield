FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y git
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
WORKDIR /tmp
RUN git clone -b color-limits https://www.github.com/vsoch/django-colorfield.git colorfield
WORKDIR /tmp/colorfield
RUN python3 setup.py sdist
RUN python3 setup.py install
RUN pip install $(ls /tmp/colorfield/dist/*.tar.gz)
WORKDIR /code
