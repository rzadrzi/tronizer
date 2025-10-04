# Tronizer
## Introduction

**Tronizer** is a minimal, production-lean FastAPI template for **on-chain payments** that aims to compress **settlement** from days to seconds and drive **per-transaction costs** down to cents (network-dependent). It’s built for teams that want borderless checkout, **24/7 settlement**, and programmatic payment flows—without the legacy friction of card and wire rails.

### What Tronizer *is*
- A lightweight, Docker-ready **payment backend skeleton** for integrating crypto payments (e.g., stablecoins) into your app.
- **OpenAPI documented** by default (`/docs`), with clean local/dev workflows and a ready-to-use Nginx reverse-proxy example.
- Designed for **webhook/callback-friendly** flows, idempotent server logic, and easy extension.

### What Tronizer *is not*
- Not a custodian, exchange, or KYC/AML provider.
- Not a fiat on/off-ramp.
- Not tied to a specific chain or asset: you plug in the network(s) you need.

---

### Why it outperforms bank rails

- **Finality in seconds–minutes**  
  Public low-fee networks confirm transactions after a small number of blocks; economic finality typically lands within seconds to a few minutes (varies by network and load).

- **Always-on settlement (24/7/365)**  
  No business-day cutoffs. Unlike card settlements (often **T+1–T+3**) or wires (**1–3 business days**, longer cross-border), on-chain settlement runs continuously.

- **Fewer intermediaries, less latency**  
  Payer → network → your wallet/gateway. Fewer hops means faster funds availability and simpler reconciliation.

---

### Why it’s cheaper for merchants *and* customers

- **Tiny, mostly flat network fees**  
  Many networks charge a small flat fee instead of a % of basket value (vs. **1.5–3.5% + fixed** for cards). Savings compound on high-ticket items and cross-border orders.

- **No legacy fee stack**  
  No interchange/assessment layers, cross-border card surcharges, or **chargeback** fees. Cost becomes more predictable.

- **Global by default**  
  With dollar-pegged stablecoins, you can avoid FX spreads and bank transfer fees for international buyers.

---

### Cost & time at a glance *(illustrative)*

| Flow                           | Typical time to funds | Typical fee model           |
|--------------------------------|-----------------------|-----------------------------|
| Card (domestic)                | T+1–T+3               | 1.5–3.5% + fixed per tx     |
| Wire (domestic)                | Same day–T+1          | Flat bank fee               |
| Wire (cross-border)            | 1–3 business days+    | Flat + FX spread            |
| **On-chain (via Tronizer)**    | **Seconds–minutes**   | **Cents (network-dependent)** |

> Numbers vary by provider, card network, issuing country, bank, and chosen blockchain. Treat the table as directional, not contractual.

---

### Quick math (directional)

For a basket of **$100.00**:

- **Cards @ 2.9% + $0.30** → ~$3.20 in fees  
- **On-chain @ ~$0.00x** (network-dependent) → fractions of a cent to a few cents

> Even if you add a conservative buffer (e.g., treasury ops, FX, custody), the unit economics often remain materially better—especially for high-ticket or cross-border sales.

---

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
