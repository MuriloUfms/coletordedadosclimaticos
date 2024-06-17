FROM python:3.12-slim

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

WORKDIR /app
COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi --without dev

EXPOSE 8000

CMD poetry run fastapi run src/main.py