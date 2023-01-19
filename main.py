from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(context="developer")

v1 = client.CoreV1Api()
print("Listing nodes with their IPs:")
ret = v1.list_node(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.addresses[0].address, i.metadata.name, i.status.node_info.kubelet_version))
