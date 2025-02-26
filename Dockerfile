FROM python:3.11-slim

RUN apt update && apt install -y curl gcc libpq-dev

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
