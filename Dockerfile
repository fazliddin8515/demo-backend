FROM python:3.11

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY . .

RUN poetry install --no-root --only main && \
    chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
