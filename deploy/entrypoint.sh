#!/bin/sh
set -e

echo "[entrypoint] applying database migrations…"
python manage.py migrate --noinput

echo "[entrypoint] collecting static files…"
python manage.py collectstatic --noinput

echo "[entrypoint] handing off to $*"
exec "$@"
