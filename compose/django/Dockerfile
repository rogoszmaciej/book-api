FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.0.5
ARG DEV=0

RUN apk update \
    && apk add --virtual .build-deps gcc python3-dev musl-dev libc-dev \
    && apk add libffi-dev py3-cryptography \
    && apk add postgresql-dev gettext \
    && pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && pip install psycopg2 \
    && apk del .build-deps

COPY pyproject.toml poetry.lock ./
RUN poetry update
RUN set -e && poetry export -f requirements.txt $( [[ $DEV == 1 ]] && echo "--dev") | pip install -r /dev/stdin

COPY ./compose/django/entrypoint /entrypoint
RUN sed -i "s/\r//" /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i "s/\r//" /start
RUN chmod +x /start

# Fix a case when container creates directories
# as root and host can"t acces them.
ARG USER_ID
ARG USER_GROUP
RUN addgroup -g $USER_ID app && \
    adduser -D -u $USER_GROUP -G app app

USER app

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
