FROM python:3.12-slim

WORKDIR /app

ENV POETRY_NO_INTERACTION=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends make

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --no-root --no-interaction

COPY . .

ENV PYTHONPATH=/app

CMD ["python", "main.py"]
