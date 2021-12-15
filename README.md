# Muon

Muon contains a database of URLS that are known to contain malware. The database can
be queried using a REST API

## Installation

Here are some examples to help you get started creating a container.

### docker-compose (recommended)

```yaml
---
version: "2.1"
services:
  muon:
    image: rogueranga/muon:latest
    container_name: muon
    ports:
      - 80:80
    restart: unless-stopped
```

### docker cli

```bash
docker run -d \
  --name=muon \
  -p 80:80 \
  --restart unless-stopped \
  rogueranga/muon:latest
```

## Usage

All responses will be in JSON. 


GET Request Parameters
| Name          | Value             | Required  |
| ------------- |-------------------|:---------:|
| version       | 1                 | Yes       |
| url           | base64 encoded url| Yes       |


Example request

```
$ curl -X GET http://muon.com/urlinfo/1/d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==
```

Response

```
{
    "base64_url":"d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==",
    "id":1,
    "verified":"True",
    "verified_at":"Tue, 14 Dec 2021 20:11:51 GMT"
}

```

POST Request Parameters
| Name          | Value              | Required  |
| ------------- |--------------------|:---------:|
| url           | base64 encoded url | Yes       |
| verified      | true/false         | Yes       |


Example request

```
$ curl -X POST http://muon.com/urlinfo/1/d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==?verified=True
```

response

```
{
    "base64_url":"d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==",
    "id":1,
    "verified":"True",
    "verified_at":"Tue, 14 Dec 2021 20:11:51 GMT"
}

```

## Contributing
Pull requests are welcome.

