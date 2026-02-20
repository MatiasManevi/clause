FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir .

COPY app ./app

ENV PYTHONPATH=/app

EXPOSE 8000
