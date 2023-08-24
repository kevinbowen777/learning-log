# `python-base` sets up all our shared environment variables
FROM python:3.11-slim-bookworm AS python-base
LABEL maintainer="Kevin Bowen <kevin.bowen@gmail.com>"

ENV DEBUG="${DEBUG}" \
  PYTHONUNBUFFERED=true \
  PYTHONDONTWRITEBYTECODE=true \
  PYTHONFAULTHANDLER=true \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# location of poetry installation
ENV PATH="/root/.local/bin:$PATH"

FROM python-base as builder-base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

COPY poetry.lock pyproject.toml /code/
COPY bin/poetry-install /code/

ARG ENV
RUN chmod 0755 /code/poetry-install

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1 \
    && poetry config virtualenvs.create false \
    && /code/poetry-install
    # && poetry install --no-interaction --no-ansi

COPY . /code/
