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
    image: rogueranga/muon:v1
    container_name: muon
    ports:
      - 5000:5000
    restart: unless-stopped
```

### docker cli

```bash
docker run -d \
  --name=muon \
  -p 5000:5000 \
  --restart unless-stopped \
  rogueranga/muon:v1
```

## Usage

All responses will be in JSON. 
Note: The url must be base64 encoded



### GET Request Parameters

| Name          | Value             | Required  |
| ------------- |-------------------|:---------:|
| version       | 1                 | Yes       |
| url           | base64 encoded url| Yes       |


Example request

```
$ curl -X GET http://muon.com:5000/urlinfo/1/d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==
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


### POST Request Parameters

| Name          | Value              | Required  |
| ------------- |--------------------|:---------:|
| url           | base64 encoded url | Yes       |
| verified      | true/false         | Yes       |


Example request

```
$ curl -X POST http://muon.com:5000/urlinfo/1/d3d3LmJhc2U2NGVuY29kZS5vcmc6NDQzLw==?verified=True
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

