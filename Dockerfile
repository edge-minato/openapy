FROM python:3.9-slim-bullseye as builder
ENV PIP_DISABLE_PIP_VERSION_CHECK=true \
    PIP_NO_CACHE_DIR=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
WORKDIR /app
RUN pip install poetry
COPY . .
RUN poetry build
RUN pip install /app/dist/openapy-*-py3-none-any.whl
RUN which openapy

FROM python:3.9-slim-bullseye
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/openapy /usr/local/bin/openapy
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
