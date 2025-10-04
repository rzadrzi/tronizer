# Tronizer
## DeFi App
A production‑lean FastAPI DeFi skeleton with Docker, Compose & Nginx — tuned for a clean local DX and a minimal, secure prod deploy.

## Why Tronizer?

Batteries‑included: local dev script, Dockerfile, Compose, and Nginx reverse‑proxy example.

Zero‑to‑prod runbook: copy‑paste blocks for local/dev, container, and server deploy.

Self‑documenting: OpenAPI/Swagger at /docs out of the box.


### Table of content
- [Local Usage](#local-usage)

- [Deployment](#deployment)

-----
<a name="local-usage"/>

### Local Usage
first install python from `https://www.python.org/`

Create virtual environment in `python`:
```commandline
python3 -m venv venv
```
use virtual environment:
```commandline
source venv/bin/activated
```
install packages from `requirements.txt`:
```commandline
pip install -r requirements.txt
```
Then use bash code
```commandline
bash start.sh
```
go to `127.0.0.1:8000/docs` and see the `fastapi` document 

------

<a name="deployment"/>


### Deployment

`nginx` configuration: 

`/etc/nginx/sites-available/YOUR-DOMAIN-NAME`
```nginx
server {

        server_name <YOUR-DOMAIN-NAME>;

        location / {
                proxy_pass http://localhost:8000/;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
        }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/<YOUR-DOMAIN-NAME>/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/<YOUR-DOMAIN-NAME>/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = YOUR-DOMAIN-NAME) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

        listen 80;

        server_name <YOUR-DOMAIN-NAME>;
    return 404; # managed by Certbot
}
```
