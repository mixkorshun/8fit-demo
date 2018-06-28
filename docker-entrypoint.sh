#!/usr/bin/env bash

command=$1

function url_scheme() {
    python -c "from urllib.parse import urlparse; print(urlparse('${1}').scheme)"
}

function url_host() {
    python -c "from urllib.parse import urlparse; print(urlparse('${1}').hostname)"
}

function url_port() {
    python -c "from urllib.parse import urlparse; print(urlparse('${1}').port)"
}

function wait_host_available() {
    host=$1
    port=$2

    while ! nc -z ${host} ${port}; do
      sleep 1
    done
}

case ${command} in
'')
    echo "Usage: $0 (start|migrate)"
    ;;
start)
    gunicorn eightfit.wsgi:application --bind 0.0.0.0:8000 --workers 4 --log-file -
    ;;
createsuperuser)
    python manage.py createsuperuser
    ;;
migrate)
    db_scheme=$(url_scheme ${DATABASE_URL})
    db_host=$(url_host ${DATABASE_URL})
    db_port=$(url_port ${DATABASE_URL})

    if [ ${db_host} ]; then
        if [ ${db_scheme} == 'postgres' ]; then
            if [ -z ${db_port} ]; then
                db_port=5432
            fi

            wait_host_available ${db_host} ${db_port}
        elif [ ${db_scheme} == 'mysql' ]; then
            if [ -z ${db_port} ]; then
                db_port=5432
            fi

            wait_host_available ${db_host} ${db_port}
        fi
    fi

    python manage.py migrate --no-input
  ;;
*)
  echo "Command `${command}` not found."
  ;;
esac
