FROM python:slim

LABEL maintainer "jee@brighthive.io, stanley@brighthive.io, aretha@brighthive.io"
WORKDIR app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD gunicorn wsgi --bind 0.0.0.0:8080
