FROM python:3

LABEL maintainer "jee@brighthive.io, stanley@brighthive.io, aretha@brighthive.io"
WORKDIR app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8080
CMD gunicorn wsgi --bind 0.0.0.0:8080
