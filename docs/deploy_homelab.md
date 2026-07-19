# Deploying FitConnect to a Proxmox home lab

This guide walks through running FitConnect on a Debian/Ubuntu LXC in
Proxmox. It uses Docker Compose (Django + gunicorn behind nginx) with
`unless-stopped` restart so the container survives reboots.

## 1. Create the LXC

In Proxmox:

- **Template:** Debian 12 or Ubuntu 22.04+ standard.
- **Disk:** 8 GB is plenty (SQLite database + static files).
- **Memory:** 512 MB is fine; 1 GB is more comfortable.
- **CPU:** 1 core.
- **Network:** DHCP or static — note the IP; you will need it.
- **Features:** enable **nesting** (Options → Features → Nesting) so
  Docker can run inside the LXC.

Start the container and log in as `root`.

## 2. Install Docker inside the LXC

```
apt update && apt install -y curl ca-certificates git
curl -fsSL https://get.docker.com | sh
systemctl enable --now docker
```

Verify:

```
docker --version
docker compose version
```

## 3. Clone the repository

```
mkdir -p /opt/fitconnect && cd /opt/fitconnect
git clone https://github.com/MateiCosmin88/FitConnect-MVP-.git .
```

## 4. Create the environment file

```
cp .env.example .env
nano .env
```

Fill in:

- **`DJANGO_SECRET_KEY`** – any long random string
  (`python -c "import secrets; print(secrets.token_urlsafe(50))"` gives
  one).
- **`DJANGO_ALLOWED_HOSTS`** – the LXC IP and any hostname you plan to
  use (comma separated, no spaces).
- **`DJANGO_CSRF_TRUSTED_ORIGINS`** – same host list but with `http://`
  prefix.

## 5. Build and start the stack

```
docker compose up -d --build
```

First start does:

1. Builds the Django image.
2. Applies migrations against SQLite in the `fitconnect_data` volume.
3. Runs `collectstatic` into the `fitconnect_static` volume.
4. Starts gunicorn (3 workers) and nginx.

Watch the logs while the first request comes in:

```
docker compose logs -f
```

## 6. Access the site

Open a browser on any device on your LAN and go to
`http://<LXC-IP>/`. You should see the FitConnect landing page.

## 7. Optional: create a superuser for /admin

```
docker compose exec web python manage.py createsuperuser
```

## 8. Optional: put a DNS name on it

If your home lab runs Adguard/Pihole/Unbound, add a record:

```
fitconnect.local  →  <LXC-IP>
```

Then add `fitconnect.local` to `DJANGO_ALLOWED_HOSTS` and
`http://fitconnect.local` to `DJANGO_CSRF_TRUSTED_ORIGINS` in `.env`,
then:

```
docker compose up -d
```

## 9. Optional: put HTTPS in front

The simplest route is a reverse proxy that already handles Let's
Encrypt (Nginx Proxy Manager, Traefik, Caddy). Point it at
`http://<LXC-IP>:80`, then set `DJANGO_SECURE_COOKIES=true` in `.env`
and restart.

## Updating

```
cd /opt/fitconnect
git pull
docker compose up -d --build
```

## Troubleshooting

- **`Bad Request (400)`** – you forgot to add the host to
  `DJANGO_ALLOWED_HOSTS`.
- **`CSRF verification failed`** – add the same host (with `http://`)
  to `DJANGO_CSRF_TRUSTED_ORIGINS`.
- **`502 Bad Gateway` from nginx** – gunicorn is not up yet; check
  `docker compose logs web`.
- **Docker won't start inside LXC** – nesting is not enabled;
  shut the LXC down, tick "Nesting" in Options → Features and start
  it again.
