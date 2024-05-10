# homelab/kubernetes

> ☸️ Kubernetes orchestration in my `homelab`.

## Clusters

| Name | Number of nodes | Nodes | Distribution | IngressController |
| ---- | --------------- | ----- | ------------ | ----------------- |
| k3s-test-a | 3 | ubt-01,ubt-02,ubt-03 | k3s | traefik |

### k3s-test-a

This is my first k3s cluster, made with the goal to get a basic understanding of how kubernetes (k3s) works and to learn kubernetes in general.

K3s comes with some pre-deployed applications that are deployed with [helm](https://helm.sh) charts, their configuration files are located in `/var/lib/rancher/k3s/server/manifests/`.

#### Ingress Controller (Traefik)

[k3s.io ingress controller documentation](https://docs.k3s.io/networking#traefik-ingress-controller)

The `IngressController` of this cluster is `traefik`.
Traefik listens on ports `80` and `443` on all the nodes and then routes incoming traffic based on predefined routes.

A load balancer external to the cluster *(can be on a completely different machine than the nodes)* is required to balance requests *(on the traefik ports)* between the nodes. In this setup i'm using HAProxy on a pfsense firewall to balance requests between the nodes and to route requests based on hostnames.

Technically all the traffic that comes to the cluster could only come from one of the three nodes (e.g. `ubt-01` on port `80`/`443`), the internal load balancer would balance that correctly inside the cluster, but what happens if that single node where all the traffic is coming goes down? And how would host based routing be handled if there is no external balancer?

Morale of the story, you need both balancers: external (e.g. HAProxy on pfsense) and internal.

#### LoadBalancer controller / Service Load Balancer (ServiceLB)

[k3s.io service load balancer documentation](https://docs.k3s.io/networking#service-load-balancer)

K3s provides a default load balancer which is `ServiceLB`. Its job is creating a `DaemonSet` for each `LoadBalancer` service (in `kube-system` namespace). The `DaemonSet` then creates a pod on each node with an `svc-` prefix. These pods use `iptables` to forward traffic from the pod's `NodePort` to the `Service`'s `ClusterIP` address and port.

#### Installation

`ubt-01`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-test-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --cluster-init
```

`ubt-02`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-test-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --server https://192.168.1.253:6443
```

`ubt-03`
```sh
curl -sfL https://get.k3s.io | sh -s - server \
        --token=<token> \
        --tls-san k3s-test-a.l.47fc5c.com --tls-san 192.168.1.1 \
        --server https://192.168.1.253:6443
```

