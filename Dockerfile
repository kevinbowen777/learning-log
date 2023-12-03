# syntax=docker/dockerfile:1
# Enable Docker BuildKit
# https://docs.docker.com/build/dockerfile/frontend/

# `python-base` sets up all our shared environment variables
FROM python:3.12-slim-bookworm AS python-base
LABEL maintainer="Kevin Bowen <kevin.bowen@gmail.com>"

ARG UID=1001
ARG GID=1001

ENV DEBUG="${DEBUG}" \
  # Python
  # https://docs.python.org/3/using/cmdline.html#environment-variables
  # Prevents Python from creating .pyc files
  PYTHONDONTWRITEBYTECODE=true \
  PYTHONFAULTHANDLER=true \
  PYTHONHASHSEED=random \
  PYTHONUNBUFFERED=true \
  # pip
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIP_NO_CACHE_DIR=no \
  # Poetry
  # https://python-poetry.org/docs/configuration/#using-environment-variables
  POETRY_HOME="/opt/poetry" \
  # No interactive questions
  POETRY_NO_INTERACTION=true \
  POETRY_VERSION="1.7.1" \
  # Use a manually prepared venv
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  # Suppress messages about installing plugins in future releases
  POETRY_WARNINGS_EXPORT=false \
  PYSETUP_PATH="/opt/pysetup" \
  VENV_PATH="/opt/pysetup/.venv"

# Prepend Poetry and virtual environment to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:/code:$PATH"

FROM python-base as builder-base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" django \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" django \
  && mkdir /opt/poetry \
  && chown django:django /opt/poetry

RUN curl -sSL https://install.python-poetry.org | python3 - \
    # In response to https://python-poetry.org/docs/plugins/#using-plugins
    && poetry self add poetry-plugin-export

WORKDIR $PYSETUP_PATH

# Install dependencies
COPY poetry.lock pyproject.toml ./
COPY bin/poetry-install ./

RUN ./poetry-install

COPY bin/docker-entrypoint.sh /docker-entrypoint.sh
# Activate virtual environment
RUN chmod +x /docker-entrypoint.sh

FROM builder-base as runtime

WORKDIR /code

COPY . /code/

USER django

EXPOSE 8000
ENTRYPOINT /docker-entrypoint.sh $0 $@
