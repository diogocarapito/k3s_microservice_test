# K3s Microservice Test

## venv

create venv

```bash
python3.13 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```

## deploy to VPS

download and install k3s on your VPS

```bash
curl -sfL https://get.k3s.io | sh -
```

verify k3s is running

```bash
sudo k3s kubectl get nodes
```

create a Personal Access Token (PAT) on GitHub with `read:packages` and `repo` scope and create a secret on your k3s cluster to pull images from GitHub Container Registry (GHCR)

```bash
sudo k3s kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=diogocarapito \
  --docker-password=<your-personal-access-token> \
  --docker-email=<your-email>
```

apply the manifest files

```bash
sudo k3s kubectl apply -f ~/k8s/
```

verify the pods, services, and deployments are running

```bash
sudo k3s kubectl get pods
sudo k3s kubectl get services
sudo k3s kubectl get deployments
```
