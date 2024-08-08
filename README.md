# Tronizer

### New DeFi App

- [Local Usage] (#local-usage)
### Local Usage
first install python from `https://www.python.org/`

```commandline
python3 -m venv venv
```
```commandline
source venv/bin/activated
```

### Deployment
`nginx` configuration: 
`/etc/`
```nginx
http {
    server {
        listen 80;
        server_name <YOUR DOMINE NAME> ;

        location / {
            proxy_pass http://app:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Redirect all HTTP requests to HTTPS
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name <YOUR DOMINE NAME>;

        ssl_certificate /etc/letsencrypt/live/<YOUR DOMINE NAME>/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/<YOUR DOMINE NAME>/privkey.pem;

        location / {
            proxy_pass http://app:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```