# Tronizer
## Introduction (DeFi + TRON Network)

**Tronizer** is a **DeFi**-native payment backend built on the **TRON Network** (TRC-20), optimized for stablecoin flows (e.g., **USDT-TRC20**). It compresses **settlement** from days to seconds and keeps **per-transaction costs** at cents or below (network-dependent). Tronizer targets teams that want borderless checkout, **24/7 settlement**, and programmable payment flows without the friction of card and wire rails.

### What Tronizer *is*
- A lightweight, Docker-ready **payment backend skeleton** for integrating crypto payments (e.g., stablecoins) into your app.
- **OpenAPI documented** by default (`/docs`), with clean local/dev workflows and a ready-to-use Nginx reverse-proxy example.
- Designed for **webhook/callback-friendly** flows, idempotent server logic, and easy extension.

### What Tronizer *is not*
- Not a custodian, exchange, or KYC/AML provider.
- Not a fiat on/off-ramp.
- Not tied to a specific chain or asset: you plug in the network(s) you need.

### Why TRON for payments
- **Fast finality**: TRON’s block time is short (≈ a few seconds), so transactions typically confirm within **seconds to minutes** (varies with network conditions and your confirmation policy).
- **Low, predictable fees**: TRON’s bandwidth/energy model yields **ultra-low fees**—often a small, mostly flat cost per transfer instead of a % fee on basket value.
- **Stablecoin liquidity**: **USDT-TRC20** is widely used with deep on-chain liquidity, making it practical for cross-border commerce and payouts.
- **Always on**: Settlement runs **24/7/365**—no business-day cutoffs, no weekend delays.

### Why it’s cheaper than legacy rails
- **Tiny network fees vs. % card fees**: Cards often charge **1.5–3.5% + fixed** per transaction; TRON transfers are typically **cents or sub-cent** (network-dependent). Savings compound on high-ticket and cross-border orders.
- **No chargebacks**: Finalized on-chain transfers are **irreversible**, eliminating chargeback fees/abuse.
- **No legacy fee stack**: No interchange/assessment layers, no cross-border card surcharges, fewer hidden spreads.

### Why it’s faster than bank rails
- **Seconds–minutes to usable funds** vs. cards (**T+1–T+3**) and wires (**1–3 business days**, longer cross-border).
- **Fewer intermediaries**: Payer → **TRON** → your wallet/gateway. Fewer hops = lower latency and simpler reconciliation.

### Cost & time at a glance *(illustrative)*
| Flow                              | Typical time to funds | Typical fee model                  |
|----------------------------------|------------------------|------------------------------------|
| Card (domestic)                  | T+1–T+3                | 1.5–3.5% + fixed per tx            |
| Wire (cross-border)              | 1–3 business days+     | Flat + FX spread                   |
| **TRON (USDT-TRC20 via Tronizer)** | **Seconds–minutes**     | **Cents / sub-cent (network-dep.)** |

> Treat the table as directional, not contractual. Precise figures depend on network load, wallet policy, and treasury ops.

### Merchant benefits
- **Better unit economics**: Low, flat network fees instead of % rake.
- **Faster cash flow**: Near-real-time settlement reduces working-capital needs.
- **Programmable by design**: Webhooks/callbacks, automated invoicing, dynamic discounts, time-locks, split payments.
- **Micropayment-friendly**: Ultra-low fees make pay-per-use/content viable.

### Customer benefits
- **Global checkout** without relying on local card/bank rails.
- **Lower effective costs**—especially for high-value and cross-border purchases.
- **Less card-data exposure** (no PAN/CVV), **on-chain receipts** for transparent audits.

> **Notes & assumptions**: Exact fees/finality depend on the chain, congestion, and your confirmation strategy. To minimize volatility, use **stablecoins** (e.g., USDT-TRC20). Compliance (KYC/AML), tax, and key/wallet management remain the merchant’s responsibility.


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
