FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y git
WORKDIR /tmp
RUN git clone -b color-limits https://www.github.com/vsoch/django-colorfield.git
WORKDIR /tmp/django-colorfield
RUN python3 setup.py install
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

