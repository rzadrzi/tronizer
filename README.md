# Tronizer
## Introduction
**Tronizer** is a **DeFi App** for payment/collection layer built on digital assets that aims to push **settlement time** down to seconds and keep **per-transaction cost** to just a few cents (or less, depending on the network). It is designed for businesses that need borderless checkout, micropayments, and **24/7 settlement** without the friction of traditional banking.

### Why is it faster than bank transactions?
- **Finality in seconds to minutes**: On low-fee public networks, transactions reach probabilistic or economic finality after a small number of confirmations—typically within seconds to a few minutes (network and load dependent).
- **True 24/7 settlement**: No business-day or cut-off constraints. Unlike card settlement (often T+1 to T+3) or wire transfers (commonly 1–3 business days, longer cross-border), on-chain settlement runs continuously.
- **Fewer intermediaries**: The hop count is shorter (payer → network → your wallet/gateway), reducing round-trip latency and reconciliation delays.

### Why is it cheaper for both merchant and customer?
- **Tiny, mostly flat network fees**: Many networks charge a small flat fee instead of a percentage of basket value (vs. 1.5–3.5% + fixed for cards). The difference compounds for high-ticket sales.
- **No legacy fee layers**: No interchange/assessment stacks, cross-border card fees, or chargeback fees. The cost structure is simpler and more predictable.
- **Cross-border without hidden spreads**: Paying with dollar-pegged stablecoins can eliminate FX conversion markups and bank transfer fees for international buyers.

A production‑lean FastAPI DeFi skeleton with Docker, Compose & Nginx — tuned for a clean local DX and a minimal, secure prod deploy.

## Why Tronizer?

**Batteries‑included:** local dev script, Dockerfile, Compose, and Nginx reverse‑proxy example.

**Zero‑to‑prod runbook:** copy‑paste blocks for local/dev, container, and server deploy.

**Self‑documenting:** OpenAPI/Swagger at /docs out of the box.


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
