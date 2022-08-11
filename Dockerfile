FROM python:3.10.6-slim-bullseye AS final

WORKDIR /app

RUN pip install celery==5.2.3 redis==4.1.4

COPY ./ /app/
