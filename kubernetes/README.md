# homelab/kubernetes

> ☸️ Kubernetes orchestration in my `homelab`.

## Clusters

| Cluster Name | N. of Nodes | Nodes | Distribution | Version | IngressController |
| ------------ | ----------- | ----- | ------------ | ------- | ----------------- |
| `k3s-prod-a` | 3 | `deb-01`,`deb-02`,`deb-03` | [k3s](https://k3s.io/) | `v1.32.1+k3s1` | [traefik](https://doc.traefik.io/traefik) |

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

> [!WARNING]
> I'm working on a solution to automatically update this table to match the kubernetes manifests in this repository. The workloads listed below and their versions are not up-to-date.

| Application | Container Image | Image Version | Manifest Digest (SHA256) |
| ----------- | --------------- | ------------- | ------------------- |
| cert-manager-controller | [quay.io/jetstack/cert-manager-controller](https://quay.io/jetstack/cert-manager-controller) | `v1.16.3` | `17c8f2d46fd16087c9ee92688304b3e38b32cbcb1f5885412e5a35e8852bc029` |
| cert-manager-cainjector | [quay.io/jetstack/cert-manager-cainjector](https://quay.io/jetstack/cert-manager-cainjector) | `v1.16.3` | `e25e5f62648966d9c442c38ef3004efb60072069d91cf6f1a9a480c16550d09e` |
| cert-manager-webhook | [quay.io/jetstack/cert-manager-webhook](https://quay.io/jetstack/cert-manager-webhook) | `v1.16.3` | `0eb32021bf2f30d923c439fd79b1b2fd3d8cf877e3c915f8a34c12803138a145` |
| changedetection.io | [docker.io/linuxserver/changedetection.io](https://hub.docker.com/r/linuxserver/changedetection.io) | `0.49.1` | `7392e8f9486a93e83f83281e56aa452c35040c655f3f888c6e7f02c1c2b79e58` |
| firefly | [docker.io/fireflyiii/core](https://hub.docker.com/r/fireflyiii/core) | `version-6.2.5` | `b54629671aa2727eb82c94115ab6301015af59a054cc7149f5aefed44bf05f68` |
| freshrss | [docker.io/freshrss/freshrss](https://hub.docker.com/r/freshrss/freshrss) | `1.25.0` | `e7897e90c1e0ab4a68cb643ff509dec4e3b85bbe42e2688ed9f95eb190bcb2b1` |
| gotify | [docker.io/gotify/server](https://hub.docker.com/r/gotify/server) | `2.6.1` | `04f4c4bb7cdde8c84e5a89d1287bd1f766c02c1cd477dc01c47acae80bff3c77` |
| grafana | [docker.io/grafana/grafana-oss](https://hub.docker.com/r/grafana/grafana-oss) | `11.5.1` | `5781759b3d27734d4d548fcbaf60b1180dbf4290e708f01f292faa6ae764c5e6` |
| homeassistant | [docker.io/linuxserver/homeassistant](https://hub.docker.com/r/linuxserver/homeassistant) | `2025.2.2` | `6e7637f2dfa51b6724611abe6c2ec15d0dd648bcbd4a2b173cd60833b022f41e` |
| homepage | [ghcr.io/gethomepage/homepage](https://github.com/gethomepage/homepage/pkgs/container/homepage) | `v0.10.9` | `825395081356da24a5cf250de14498cf0fffe0e9a2a743ac8b7e7fe95040113a` |
| immich-machine-learning | [ghcr.io/immich-app/immich-machine-learning](https://github.com/immich-app/immich/pkgs/container/immich-machine-learning) | `v1.126.1` | `eaff41f58cedc4b35f6d1bc9cb840647e1afdac9ef341957adce8717133dd9af` |
| immich-pgvectors | [docker.io/tensorchord/pgvecto-rs](https://hub.docker.com/r/tensorchord/pgvecto-rs) | `pg14-v0.2.0` | `90724186f0a3517cf6914295b5ab410db9ce23190a2d9d0b9dd6463e3fa298f0` |
| immich-server | [ghcr.io/immich-app/immich-server](https://github.com/immich-app/immich/pkgs/container/immich-server) | `v1.126.1` | `5ee24916149dff3e52fbc6edb69528d74e8a131d08b687a9d422ecf8bed1e7f0` |
| jellyfin | [docker.io/jellyfin/jellyfin](https://hub.docker.com/r/jellyfin/jellyfin) | `10.10.5` | `0ff2f1533e53e7811a04e6cfaf38ce5f467079271e7ed6155bdf36b60423095b` |
| kavita | [docker.io/jvmilazz0/kavita](https://hub.docker.com/r/jvmilazz0/kavita) | `0.8.4` | `07393ed7d6860e7312c0197b8c1ebcd4d53c52b7cabd542db08613410ff22c69` |
| kube-vip | [ghcr.io/kube-vip/kube-vip](https://github.com/kube-vip/kube-vip/pkgs/container/kube-vip) | `v0.8.9` | `0b4d9e0f17b00bb7514ab19ea268cec1c80529b4a81931acb5c5729dcf094345` |
| lidarr | [docker.io/linuxserver/lidarr](https://hub.docker.com/r/linuxserver/lidarr) | `2.9.6` | `4f31ca3afa04ad6ad643a5e27cd6a68c2cde581483f7117dd4baae0b33cd1e71` |
| linkding | [docker.io/sissbruecker/linkding](https://hub.docker.com/r/sissbruecker/linkding) | `1.38.0` | `09e1a54b083832b93a67c08d2302149027f713fc0052d8d8859205e3aa2bfcfe` |
| mariadb | [docker.io/library/mariadb](https://hub.docker.com/_/mariadb) | `11.5.2` | `6683de3c6fc21fb7edcd4d3abcfc591329faeec3fc933fbc4260a2db7a60fed5` |
| mosquitto | [docker.io/library/eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto) | `2.0.20` | `21421af7b32bf9ce508e9090c8eb13bb81f410ca778dc205506180a6f862d0eb` |
| navidrome | [docker.io/deluan/navidrome](https://hub.docker.com/r/deluan/navidrome) | `0.54.4` | `04c25ef91c169bde5d449f65a81af546a564656bbefc139fa2b0064b7dda0480` |
| nextcloud | [docker.io/library/nextcloud](https://hub.docker.com/_/nextcloud) | `30.0.5` | `a52af642fd0f5e4957ce42fa27b77dd0c898223e32dbf8266664bf2613d882c2` |
| nfs-fast-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| nfs-slow-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| node-exporter | [docker.io/prom/node-exporter](https://hub.docker.com/r/prom/node-exporter) | `v1.8.2` | `4032c6d5bfd752342c3e631c2f1de93ba6b86c41db6b167b9a35372c139e7706` |
| owntracks-frontend | [docker.io/owntracks/frontend](https://hub.docker.com/r/owntracks/frontend) | `2.15.3` | `efa313bdec583939f6edc70eb148670a8bba1a5aed0508a326f5b2f2751d0861` |
| owntracks-recorder | [docker.io/owntracks/recorder](https://hub.docker.com/r/owntracks/recorder) | `0.9.9` | `897bf5a2e84c64ddc334e4f82e3f8a9330e54bbeba8174767652f2b879e6d0db` |
| pihole | [docker.io/pihole/pihole](https://hub.docker.com/r/pihole/pihole) | `2024.07.0` | `e53305e9e00d7ac283763ca9f323cc95a47d0113a1e02eb9c6849f309d6202dd` |
| postgres | [docker.io/library/postgres](https://hub.docker.com/_/postgres) | `14.15` | `f104f501cd403abdc56cd17fab81fad0b15754e8dce818e20300a17a3628700f` |
| prometheus | [docker.io/prom/prometheus](https://hub.docker.com/r/prom/prometheus) | `v2.55.1` | `b1935d181b6dd8e9c827705e89438815337e1b10ae35605126f05f44e5c6940f` |
| prowlarr | [docker.io/linuxserver/prowlarr](https://hub.docker.com/r/linuxserver/prowlarr) | `1.30.2` | `53e8a473db4fb811a54bce1cf9fe3c2962752e40e4696e04974b804d1333d4fa` |
| qbittorrent | [docker.io/linuxserver/qbittorrent](https://hub.docker.com/r/linuxserver/qbittorrent) | `5.0.0` | `525262e8916d4d112d73427a841dcae3464f7fe3234e1c859c6d0b03245f98ae` |
| radarr | [docker.io/linuxserver/radarr](https://hub.docker.com/r/linuxserver/radarr) | `5.18.4` | `06551a0e67bd46d857434f6a695adb9104819376b6dff19e64402384935dcd36` |
| readarr | [docker.io/linuxserver/readarr](https://hub.docker.com/r/linuxserver/readarr) | `0.4.10-nightly` | `59fc952ec6aa2d7b5070672d86e5554f7649aae545526c8d1d6f5a82b2a270c2` |
| redis | [docker.io/library/redis](https://hub.docker.com/_/redis) | `7.4.1` | `18077322db9506f5df37db3e0f7080574853d593bcd23a4d42d551a3127b55fd` |
| romm | [docker.io/rommapp/romm](https://hub.docker.com/r/rommapp/romm) | `3.7.3` | `61bc20fca829c71946639323204dc6059fbf570db3cd6e17afb5b11631dc33a6` |
| sealed-secrets-controller | [docker.io/bitnami/sealed-secrets-controller](https://hub.docker.com/r/bitnami/sealed-secrets-controller) | `0.28.0` | `8fecbbd6db6838b8754def3d850a2de8189ee96dfee61d6ed0c2424739771bd7` |
| sonarr | [docker.io/linuxserver/sonarr](https://hub.docker.com/r/linuxserver/sonarr) | `4.0.12` | `0b45e56ad4acd89072b96702e4cc1088fb31235d6fa8458c738e250ebb7acaa4` |

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
