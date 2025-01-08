# homelab/kubernetes

> ☸️ Kubernetes orchestration in my `homelab`.

## Clusters

| Cluster Name | N. of Nodes | Nodes | Distribution | Version | IngressController |
| ------------ | ----------- | ----- | ------------ | ------- | ----------------- |
| `k3s-prod-a` | 3 | `deb-01`,`deb-02`,`deb-03` | [k3s](https://k3s.io/) | `v1.30.6+k3s1` | [traefik](https://doc.traefik.io/traefik) |

#### Manual installation

`deb-01`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-prod-a.l.47fc5c.com \
        --tls-san 192.168.1.250 \
        --embedded-registry \
        --etcd-expose-metrics \
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
        --server https://192.168.1.250:6443
```

#### Workloads

| Application | Container Image | Image Version | Manifest Digest (SHA256) |
| ----------- | --------------- | ------------- | ------------------- |
| cert-manager | [quay.io/jetstack/cert-manager-controller](https://quay.io/jetstack/cert-manager-controller) | `v1.16.2` | `de97c3767802e33d3096ad9b276598ceee3ed92a0c67907221581b36c8ad055f` |
| cert-manager-cainjector | [quay.io/jetstack/cert-manager-cainjector](https://quay.io/jetstack/cert-manager-cainjector) | `v1.16.2` | `0a1f62ea3390a73239c0b4214e0ada1fb89c52d30677aebcdc3ca54508996511` |
| cert-manager-webhook | [quay.io/jetstack/cert-manager-webhook](https://quay.io/jetstack/cert-manager-webhook) | `v1.16.2` | `25d87dff68f00587a3e76a1e5d530d40b6f0f7872e6d634db01a593047849109` |
| changedetection.io | [docker.io/linuxserver/changedetection.io](https://hub.docker.com/r/linuxserver/changedetection.io) | `0.48.05` | `9b6a05a7ae2896a746ad9b55a56918b242d1768293c3cdbbdf7d179620514c88` |
| firefly | [docker.io/fireflyiii/core](https://hub.docker.com/r/fireflyiii/core) | `version-6.1.21` | `68b79eeb4d54060d715f4c3ea1f6e11e633b3446f6cf705034320ed1b9bea935` |
| grafana | [docker.io/grafana/grafana-oss](https://hub.docker.com/r/grafana/grafana-oss) | `11.2.2` | `bc4bf0f6981764044ec565fac1c85c53d947be3a9bd2300824a243e87412cce4` |
| homeassistant | [docker.io/linuxserver/homeassistant](https://hub.docker.com/r/linuxserver/homeassistant) | `2025.1.1` | `a969b677cba8da29db03b81643d092bc4b8fa067a19268d9de0fe84a028c2020` |
| homepage | [ghcr.io/gethomepage/homepage](https://github.com/gethomepage/homepage/pkgs/container/homepage) | `v0.10.9` | `825395081356da24a5cf250de14498cf0fffe0e9a2a743ac8b7e7fe95040113a` |
| jellyfin | [docker.io/jellyfin/jellyfin](https://hub.docker.com/r/jellyfin/jellyfin) | `10.9.11` | `efc2f4ebef76f0e8d3ea49c87b4c61c7d8847e496dc1fd5a91ce6652e33c116f` |
| kavita | [docker.io/jvmilazz0/kavita](https://hub.docker.com/r/jvmilazz0/kavita) | `0.8.4` | `7f4d5de5f9a5a842a83324429d59730b761dca422b8aa2caf28155aa42996421` |
| kube-vip | [ghcr.io/kube-vip/kube-vip](https://github.com/kube-vip/kube-vip/pkgs/container/kube-vip) | `v0.8.8` | `-` |
| lidarr | [docker.io/linuxserver/lidarr](https://hub.docker.com/r/linuxserver/lidarr) | `2.7.1` | `46b8237b38950dcad3dc24ca5f5aaa68359c78e024ccc792192263004173a86a` |
| linkding | [docker.io/sissbruecker/linkding](https://hub.docker.com/r/sissbruecker/linkding) | `1.36.0` | `019a5d00596ed762f0001ebcc6a0aa2263dbf8a01ec0f3ae5add24cb68caea8b` |
| mariadb | [docker.io/library/mariadb](https://hub.docker.com/_/mariadb) | `11.5.2` | `6683de3c6fc21fb7edcd4d3abcfc591329faeec3fc933fbc4260a2db7a60fed5` |
| mosquitto | [docker.io/library/eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto) | `2.0.20` | `c16ebb350bd1509a33ee09edb5bafe4579fe53ae189b756362701bfdc2c0f931` |
| navidrome | [docker.io/deluan/navidrome](https://hub.docker.com/r/deluan/navidrome) | `0.54.3` | `f1f78eb4a144865b9c6cac58c5b06a551e1bd46e6bc38955666aee68e3a2be8e` |
| nextcloud | [docker.io/library/nextcloud](https://hub.docker.com/_/nextcloud) | `30.0.3` | `97bfb8ad50609d7b63fa66e2aceddf13ba35b98f693b8dac8f172b5e262c6f08` |
| nfs-fast-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| nfs-slow-subdir-external-provisioner | [registry.k8s.io/sig-storage/nfs-subdir-external-provisioner](registry.k8s.io/sig-storage/nfs-subdir-external-provisioner) | `v4.0.2` | `374f80dde8bbd498b1083348dd076b8d8d9f9b35386a793f102d5deebe593626` |
| node-exporter | [docker.io/prom/node-exporter](https://hub.docker.com/r/prom/node-exporter) | `v1.8.2` | `065914c03336590ebed517e7df38520f0efb44465fde4123c3f6b7328f5a9396` |
| owntracks-recorder | [docker.io/owntracks/recorder](https://hub.docker.com/r/owntracks/recorder) | `0.9.9` | `35d717a7cd18f9c41c01404a809f3e722c828bc6137d4c06c2f15f4046fa7a44` |
| photoprism | [docker.io/photoprism/photoprism](https://hub.docker.com/r/photoprism/photoprism) | `240915` | `32da029428be9335889ab13f03ea839201af49c2a1699c8f7c4de5b5911e2e1a` |
| pihole | [docker.io/pihole/pihole](https://hub.docker.com/r/pihole/pihole) | `2024.07.0` | `e53305e9e00d7ac283763ca9f323cc95a47d0113a1e02eb9c6849f309d6202dd` |
| postgres | [docker.io/library/postgres](https://hub.docker.com/_/postgres) | `14.15` | `f104f501cd403abdc56cd17fab81fad0b15754e8dce818e20300a17a3628700f` |
| prometheus | [docker.io/prom/prometheus](https://hub.docker.com/r/prom/prometheus) | `v2.54.1` | `69961df6ffa67598048a31aa2822d61f3c93b91d7db24e44d9bb03f99d520da9` |
| prowlarr | [docker.io/linuxserver/prowlarr](https://hub.docker.com/r/linuxserver/prowlarr) | `1.25.4` | `e6d760f17399cd40093ed7e40af7160bc638e6a9690a9c8d024699b5129c1aaa` |
| qbittorrent | [docker.io/linuxserver/qbittorrent](https://hub.docker.com/r/linuxserver/qbittorrent) | `5.0.0` | `758c19794b7da7f6c39d9d35d4b07693dac41e0f727b7622fce116ee79375e5c` |
| radarr | [docker.io/linuxserver/radarr](https://hub.docker.com/r/linuxserver/radarr) | `5.15.1` | `8144ce04ec85cc838f3a4a5ca944947095b7df11db0a3e34074d0c8505861f83` |
| readarr | [docker.io/linuxserver/readarr](https://hub.docker.com/r/linuxserver/readarr) | `0.4.4-nightly` | `c97e38836da9e8b28f40e2d529f4b336b5187dbd7032ff5d0d58e5fe578e82f7` |
| redis | [docker.io/library/redis](https://hub.docker.com/_/redis) | `7.4.1` | `126cc4da63a39000ce527ae644b880d26608d27d8b7d35b3ee37670f5ee55eea` |
| romm | [docker.io/rommapp/romm](https://hub.docker.com/r/rommapp/romm) | `3.7.0` | `594f26adc063a13c8e578489e8c60fbf9c4db1e15a2330d6ed9a6ee12758b911` |
| sealed-secrets-controller | [docker.io/bitnami/sealed-secrets-controller](https://hub.docker.com/r/bitnami/sealed-secrets-controller) | `0.27.1` | `18024029150211e677b79d1ed61cc2e6ac7b2cf2479a76fd5a98bb38d29ed06c` |
| sonarr | [docker.io/linuxserver/sonarr](https://hub.docker.com/r/linuxserver/sonarr) | `4.0.10` | `d5a4e51ac29de5d896ec739cb727f3d80cac16d821315c7f2302a3e69832d9ca` |

## Useful commands

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
