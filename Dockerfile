# Pull base image
FROM python:3.10

ARG LEARNING_LOG

# Set environment variables
ENV LEARNING_LOG=${LEARNING_LOG} \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

# System dependencies
RUN pip install "poetry==$POETRY_VERSION"

# Set work directory
WORKDIR /code

# Install dependencies
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install

# Copy project
COPY . /code/
