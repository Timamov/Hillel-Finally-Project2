FROM python:3.12-slim

WORKDIR /app

ENV POETRY_NO_INTERACTION=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-ansi --no-root --no-interaction

COPY . /app

EXPOSE 9999