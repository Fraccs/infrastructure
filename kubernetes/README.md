# homelab/kubernetes

> ☸️ Kubernetes orchestration in my `homelab`.

## Clusters

| Cluster Name | N. of Nodes | Nodes | Distribution | Version | IngressController |
| ------------ | ----------- | ----- | ------------ | ------- | ----------------- |
| `k3s-prod-a` | 3 | `deb-01`,`deb-02`,`deb-03` | [k3s](https://k3s.io/) | `v1.30.5+k3s1` | [traefik](https://doc.traefik.io/traefik) |

### k3s-prod-a

This is my first k3s cluster, made with the goal to get a basic understanding of how kubernetes (k3s) works and to learn kubernetes in general.

K3s comes with some pre-deployed applications that are deployed with [helm](https://helm.sh) charts, their configuration files are located in `/var/lib/rancher/k3s/server/manifests/`.

#### IngressController (Traefik)

[k3s.io ingress controller documentation](https://docs.k3s.io/networking#traefik-ingress-controller)

The `IngressController` of this cluster is `traefik`.
Traefik listens on ports `80` and `443` on all the nodes and then routes incoming traffic based on predefined routes.

A load balancer external to the cluster *(can be on a completely different machine than the nodes)* is required to balance requests *(on the traefik ports)* between the nodes. In this setup i'm using [HAProxy](https://www.haproxy.org) on a [pfSense](https://www.pfsense.org) firewall to balance requests between the nodes and to route requests based on hostnames.

Technically all the traffic that comes to the cluster could only come from one of the three nodes (e.g. `deb-01` on port `80`/`443`), the internal load balancer would balance that correctly inside the cluster, but what happens if that single node where all the traffic is coming goes down? And how would host based routing be handled if there is no external balancer?

Morale of the story, you need both balancers: external (e.g. HAProxy on pfSense) and internal.

#### LoadBalancer controller / Service Load Balancer (ServiceLB)

[k3s.io service load balancer documentation](https://docs.k3s.io/networking#service-load-balancer)

K3s provides a default load balancer which is `ServiceLB`. Its job is creating a `DaemonSet` for each `LoadBalancer` service (in `kube-system` namespace). The `DaemonSet` then creates a pod on each node with an `svc-` prefix. These pods use `iptables` to forward traffic from the pod's `NodePort` to the `Service`'s `ClusterIP` address and port.

#### Manual installation

`deb-01`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --cluster-init
```

`deb-02`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --server https://192.168.1.251:6443
```

`deb-03`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --server https://192.168.1.251:6443
```

#### Workloads

| Application | Container Image | Image Version | Manifest Digest (SHA256) |
| ----------- | --------------- | ------------- | ------------------- |
| firefly | [docker.io/fireflyiii/core](https://hub.docker.com/r/fireflyiii/core) | `version-6.1.21` | `68b79eeb4d54060d715f4c3ea1f6e11e633b3446f6cf705034320ed1b9bea935` |
| grafana | [docker.io/grafana/grafana-oss](https://hub.docker.com/r/grafana/grafana-oss) | `11.2.2` | `bc4bf0f6981764044ec565fac1c85c53d947be3a9bd2300824a243e87412cce4` |
| homeassistant | [docker.io/linuxserver/homeassistant](https://hub.docker.com/r/linuxserver/homeassistant) | `2024.10.2` | `b8997c5e7989f9cd8a59ffadb9dadd724373b763d8ddc1c80ef618e0e4601eb4` |
| homepage | [ghcr.io/gethomepage/homepage](https://github.com/gethomepage/homepage/pkgs/container/homepage) | `v0.9.11` | `bc737801896bb823f67135d16ae7be2b94a95da5c67243162196a2a0ea8ea281` |
| jellyfin | [docker.io/jellyfin/jellyfin](https://hub.docker.com/r/jellyfin/jellyfin) | `10.9.11` | `efc2f4ebef76f0e8d3ea49c87b4c61c7d8847e496dc1fd5a91ce6652e33c116f` |
| lidarr | [docker.io/linuxserver/lidarr](https://hub.docker.com/r/linuxserver/lidarr) | `2.7.1` | `46b8237b38950dcad3dc24ca5f5aaa68359c78e024ccc792192263004173a86a` |
| linkding | [docker.io/sissbruecker/linkding](https://hub.docker.com/r/sissbruecker/linkding) | `1.36.0` | `019a5d00596ed762f0001ebcc6a0aa2263dbf8a01ec0f3ae5add24cb68caea8b` |
| navidrome | [docker.io/deluan/navidrome](https://hub.docker.com/r/deluan/navidrome) | `0.53.3` | `6b9e2f5fb7f03dbc116d86ad5fc614c312b326e46638c0438bb14c91a0a49b59` |
| nextcloud | [docker.io/library/nextcloud](https://hub.docker.com/_/nextcloud) | `30.0.0` | `c293951861b5036eb8ec48a14584348fc6699e2e718d785ae8f7551f3befe5d2` |
| node-exporter | [docker.io/prom/node-exporter](https://hub.docker.com/r/prom/node-exporter) | `v1.8.2` | `065914c03336590ebed517e7df38520f0efb44465fde4123c3f6b7328f5a9396` |
| owntracks-recorder | [docker.io/owntracks/recorder](https://hub.docker.com/r/owntracks/recorder) | `0.9.9` | `35d717a7cd18f9c41c01404a809f3e722c828bc6137d4c06c2f15f4046fa7a44` |
| photoprism | [docker.io/photoprism/photoprism](https://hub.docker.com/r/photoprism/photoprism) | `240915` | `32da029428be9335889ab13f03ea839201af49c2a1699c8f7c4de5b5911e2e1a` |
| pihole | [docker.io/pihole/pihole](https://hub.docker.com/r/pihole/pihole) | `2024.07.0` | `e53305e9e00d7ac283763ca9f323cc95a47d0113a1e02eb9c6849f309d6202dd` |
| prometheus | [docker.io/prom/prometheus](https://hub.docker.com/r/prom/prometheus) | `v2.54.1` | `69961df6ffa67598048a31aa2822d61f3c93b91d7db24e44d9bb03f99d520da9` |
| prowlarr | [docker.io/linuxserver/prowlarr](https://hub.docker.com/r/linuxserver/prowlarr) | `1.25.4` | `e6d760f17399cd40093ed7e40af7160bc638e6a9690a9c8d024699b5129c1aaa` |
| qbittorrent | [docker.io/linuxserver/qbittorrent](https://hub.docker.com/r/linuxserver/qbittorrent) | `5.0.0` | `758c19794b7da7f6c39d9d35d4b07693dac41e0f727b7622fce116ee79375e5c` |
| romm | [docker.io/rommapp/romm](https://hub.docker.com/r/rommapp/romm) | `3.5.1` | `abd6aaa499e8632e98001e04dfff46acf986083065a7be9f79157bf1c2c2936` |
| sealed-secrets-controller | [docker.io/bitnami/sealed-secrets-controller](https://hub.docker.com/r/bitnami/sealed-secrets-controller) | `0.27.1` | `18024029150211e677b79d1ed61cc2e6ac7b2cf2479a76fd5a98bb38d29ed06c` |

## Useful commands

### Sealed secrets

#### Extract `sealed-secrets-controller` keys (backup for disaster recovery)

```sh
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > sealed-secrets-controller.key
```

#### Create a `SealedSecret` resource starting from a `Secret`

```sh
kubeseal -f <input-secret>.yml -w <output-sealed-secret>.yml
```

#### Unseal a `SealedSecret` resource

```sh
kubeseal < <input-sealed-secret>.yml --recovery-unseal --recovery-private-key <sealed-secrets-controller-secret-key>.key -o yaml > <output-secret>.yml
```
