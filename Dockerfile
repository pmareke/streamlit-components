FROM python:3.12-slim

ENV PYTHONPATH=.

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# hadolint ignore=DL3013
RUN pip install --no-cache-dir poetry

COPY pyproject.toml /code

RUN poetry install --no-root --without test

COPY . /code

EXPOSE 8501

ENTRYPOINT ["poetry", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

