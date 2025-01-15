FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    curl \
    && apt-get clean

WORKDIR /app

RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app
CMD ["poetry", "run", "python", "-m", "backend.app"]
