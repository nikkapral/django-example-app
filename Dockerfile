FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update
RUN apk add --no-cache python3-dev
RUN apk add gcc musl-dev libpq-dev nmap
RUN pip install --upgrade pip
RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

RUN chmod +x entrypoint.sh
