# FitConnect production image — Django + gunicorn + WhiteNoise.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Non-root user for runtime.
RUN useradd --create-home --shell /bin/bash app \
    && mkdir -p /app/data /app/staticfiles \
    && chown -R app:app /app
USER app

EXPOSE 8000

# Entrypoint applies migrations, collects static, then hands off to gunicorn.
COPY --chown=app:app deploy/entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "fitconnect.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--access-logfile", "-"]
