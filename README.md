# K3s Microservice Test

## Download and install K3s with the following command:

```bash
curl -sfL https://get.k3s.io | sh -
```

## run dev version in a docker container

```bash
docker run -d --name k3s-server --privileged --restart=unless-stopped \
  -p 6443:6443 -p 80:80 -p 443:443 \
  rancher/k3s:v1.28.2-k3s1
```

## venv

create venv

```bash
python3.13 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```
