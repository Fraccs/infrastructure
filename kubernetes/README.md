# homelab/kubernetes

> ☸️ Kubernetes orchestration in my `homelab`.

## Clusters

| Cluster Name | N. of Nodes | Nodes | Distribution | Version | IngressController |
| ------------ | ----------- | ----- | ------------ | ------- | ----------------- |
| `k3s-prod-a` | 3 | `deb-01`,`deb-02`,`deb-03` | [k3s](https://k3s.io/) | `v1.32.0+k3s1` | [traefik](https://doc.traefik.io/traefik) |

#### Manual installation

`deb-01`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com \
        --tls-san 192.168.1.250 \
        --embedded-registry \
        --etcd-expose-metrics \
        --disable=local-storage \
        --cluster-init
```

`deb-02`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com \
        --tls-san 192.168.1.250 \
        --embedded-registry \
        --etcd-expose-metrics \
        --disable=local-storage \
        --server https://192.168.1.250:6443
```

`deb-03`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com \
        --tls-san 192.168.1.250 \
        --embedded-registry \
        --etcd-expose-metrics \
        --disable=local-storage \
        --server https://192.168.1.250:6443
```

#### Workloads

| Application | Container Image | Image Version | Manifest Digest (SHA256) |
| ----------- | --------------- | ------------- | ------------------- |
| cert-manager-controller | [quay.io/jetstack/cert-manager-controller](https://quay.io/jetstack/cert-manager-controller) | `v1.16.3` | `17c8f2d46fd16087c9ee92688304b3e38b32cbcb1f5885412e5a35e8852bc029` |
| cert-manager-cainjector | [quay.io/jetstack/cert-manager-cainjector](https://quay.io/jetstack/cert-manager-cainjector) | `v1.16.3` | `e25e5f62648966d9c442c38ef3004efb60072069d91cf6f1a9a480c16550d09e` |
| cert-manager-webhook | [quay.io/jetstack/cert-manager-webhook](https://quay.io/jetstack/cert-manager-webhook) | `v1.16.3` | `0eb32021bf2f30d923c439fd79b1b2fd3d8cf877e3c915f8a34c12803138a145` |
| changedetection.io | [docker.io/linuxserver/changedetection.io](https://hub.docker.com/r/linuxserver/changedetection.io) | `0.49.0` | `1502a132c0259aa75b2043cfb39ba37f09d4558bce52936795832f846c56d014` |
| firefly | [docker.io/fireflyiii/core](https://hub.docker.com/r/fireflyiii/core) | `version-6.1.21` | `68b79eeb4d54060d715f4c3ea1f6e11e633b3446f6cf705034320ed1b9bea935` |
| freshrss | [docker.io/freshrss/freshrss](https://hub.docker.com/r/freshrss/freshrss) | `1.25.0` | `0e780fff57060cb8e0694b371e1dd4b5b8f175c5b662d7da3f34c115d5aa4ff9` |
| gotify | [docker.io/gotify/server](https://hub.docker.com/r/gotify/server) | `2.6.1` | `fc6ea284ee82af1fbd3a3cde407fd540bd3ee5407ac440f642de42b803e73b11` |
| grafana | [docker.io/grafana/grafana-oss](https://hub.docker.com/r/grafana/grafana-oss) | `11.2.2` | `bc4bf0f6981764044ec565fac1c85c53d947be3a9bd2300824a243e87412cce4` |
| homeassistant | [docker.io/linuxserver/homeassistant](https://hub.docker.com/r/linuxserver/homeassistant) | `2025.1.4` | `8a3d58bbfe3f75ed7330722ef59ace7935da6b7f9791542186997986570281e7` |
| homepage | [ghcr.io/gethomepage/homepage](https://github.com/gethomepage/homepage/pkgs/container/homepage) | `v0.10.9` | `825395081356da24a5cf250de14498cf0fffe0e9a2a743ac8b7e7fe95040113a` |
| immich-machine-learning | [ghcr.io/immich-app/immich-machine-learning](https://github.com/immich-app/immich/pkgs/container/immich-machine-learning) | `v1.125.3` | `6f5cce23383f057438fc9214a42f0f9528e3a736f4a9745cd3eecd887074cb7d` |
| immich-pgvectors | [docker.io/tensorchord/pgvecto-rs](https://hub.docker.com/r/tensorchord/pgvecto-rs) | `pg14-v0.2.0` | `90724186f0a3517cf6914295b5ab410db9ce23190a2d9d0b9dd6463e3fa298f0` |
| immich-server | [ghcr.io/immich-app/immich-server](https://github.com/immich-app/immich/pkgs/container/immich-server) | `v1.125.3` | `436ebe8fd4010e4a2d8ebcdb9bd43e1b1280f3d95434a6fd46ec01105532c223` |
| jellyfin | [docker.io/jellyfin/jellyfin](https://hub.docker.com/r/jellyfin/jellyfin) | `10.10.5` | `0ff2f1533e53e7811a04e6cfaf38ce5f467079271e7ed6155bdf36b60423095b` |
| kavita | [docker.io/jvmilazz0/kavita](https://hub.docker.com/r/jvmilazz0/kavita) | `0.8.4` | `7f4d5de5f9a5a842a83324429d59730b761dca422b8aa2caf28155aa42996421` |
| kube-vip | [ghcr.io/kube-vip/kube-vip](https://github.com/kube-vip/kube-vip/pkgs/container/kube-vip) | `v0.8.9` | `0b4d9e0f17b00bb7514ab19ea268cec1c80529b4a81931acb5c5729dcf094345` |
| lidarr | [docker.io/linuxserver/lidarr](https://hub.docker.com/r/linuxserver/lidarr) | `2.8.2` | `e15772e07979510d40f7300c325a3e14dbe5b9b0cfaac8eefa4f93826809dc02` |
| linkding | [docker.io/sissbruecker/linkding](https://hub.docker.com/r/sissbruecker/linkding) | `1.37.0` | `d1fad175e708a72f735848a6bde660df9b624cf225ee97ea4dc00ae4a3485919` |
| mariadb | [docker.io/library/mariadb](https://hub.docker.com/_/mariadb) | `11.5.2` | `6683de3c6fc21fb7edcd4d3abcfc591329faeec3fc933fbc4260a2db7a60fed5` |
| mosquitto | [docker.io/library/eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto) | `2.0.20` | `c16ebb350bd1509a33ee09edb5bafe4579fe53ae189b756362701bfdc2c0f931` |
| navidrome | [docker.io/deluan/navidrome](https://hub.docker.com/r/deluan/navidrome) | `0.54.4` | `04c25ef91c169bde5d449f65a81af546a564656bbefc139fa2b0064b7dda0480` |
| nextcloud | [docker.io/library/nextcloud](https://hub.docker.com/_/nextcloud) | `30.0.5` | `765abbfbcd410978e133c89599fd7d80ab33263515147ffcc13a8c4a9dfb25e7` |
| nfs-fast-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| nfs-slow-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| node-exporter | [docker.io/prom/node-exporter](https://hub.docker.com/r/prom/node-exporter) | `v1.8.2` | `065914c03336590ebed517e7df38520f0efb44465fde4123c3f6b7328f5a9396` |
| owntracks-frontend | [docker.io/owntracks/frontend](https://hub.docker.com/r/owntracks/frontend) | `2.15.3` | `45000a65ed59b2d148822dcfa98f1065945bbe38ebbebfe9bf2e43509fce41cc` |
| owntracks-recorder | [docker.io/owntracks/recorder](https://hub.docker.com/r/owntracks/recorder) | `0.9.9` | `35d717a7cd18f9c41c01404a809f3e722c828bc6137d4c06c2f15f4046fa7a44` |
| pihole | [docker.io/pihole/pihole](https://hub.docker.com/r/pihole/pihole) | `2024.07.0` | `e53305e9e00d7ac283763ca9f323cc95a47d0113a1e02eb9c6849f309d6202dd` |
| postgres | [docker.io/library/postgres](https://hub.docker.com/_/postgres) | `14.15` | `f104f501cd403abdc56cd17fab81fad0b15754e8dce818e20300a17a3628700f` |
| prometheus | [docker.io/prom/prometheus](https://hub.docker.com/r/prom/prometheus) | `v2.54.1` | `69961df6ffa67598048a31aa2822d61f3c93b91d7db24e44d9bb03f99d520da9` |
| prowlarr | [docker.io/linuxserver/prowlarr](https://hub.docker.com/r/linuxserver/prowlarr) | `1.30.2` | `a8f6136e9b40016a5585a169f05884efc74d999b594421aefeed73d4ad57bc4c` |
| qbittorrent | [docker.io/linuxserver/qbittorrent](https://hub.docker.com/r/linuxserver/qbittorrent) | `5.0.0` | `758c19794b7da7f6c39d9d35d4b07693dac41e0f727b7622fce116ee79375e5c` |
| radarr | [docker.io/linuxserver/radarr](https://hub.docker.com/r/linuxserver/radarr) | `5.17.2` | `03f527a304676d75350fa0c013c13e42668c4d36cc00639a4ad9a1ff558f923c` |
| readarr | [docker.io/linuxserver/readarr](https://hub.docker.com/r/linuxserver/readarr) | `0.4.10-nightly` | `59fc952ec6aa2d7b5070672d86e5554f7649aae545526c8d1d6f5a82b2a270c2` |
| redis | [docker.io/library/redis](https://hub.docker.com/_/redis) | `7.4.1` | `126cc4da63a39000ce527ae644b880d26608d27d8b7d35b3ee37670f5ee55eea` |
| romm | [docker.io/rommapp/romm](https://hub.docker.com/r/rommapp/romm) | `3.7.3` | `61bc20fca829c71946639323204dc6059fbf570db3cd6e17afb5b11631dc33a6` |
| sealed-secrets-controller | [docker.io/bitnami/sealed-secrets-controller](https://hub.docker.com/r/bitnami/sealed-secrets-controller) | `0.28.0` | `e7caa0351663f4c7e6cb531732625e390c163dec7793272ec65d78e5926a5c37` |
| sonarr | [docker.io/linuxserver/sonarr](https://hub.docker.com/r/linuxserver/sonarr) | `4.0.12` | `4092d2141b796ef01f3c7b0d3390910fb71a11b2e9acdbd9427aa9a8864d6139` |

## Useful commands

### k3s

#### Manual upgrade of k3s

> Use the same command that was used for installation and pass the `INSTALL_K3S_VERSION` env variable.

```sh
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=vX.Y.Z+k3s1 sh -s - server \
        <exact_same_flags_that_were_used_at_installation>
```

### Nextcloud

#### Spawn a shell as `www-data` user (for `occ` maintenance)

```sh
kubectl exec -it <nextcloud_pod> -n <nextcloud_namespace> -- su -s /bin/bash - www-data
```

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
