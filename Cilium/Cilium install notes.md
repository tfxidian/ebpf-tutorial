# Cilium install 

## 安装helm

Every release of Helm provides binary releases for a variety of OSes. These binary versions can be manually downloaded and installed.

Download your desired version [helm](https://github.com/helm/helm/releases)
Unpack it (tar -zxvf helm-v3.0.0-linux-amd64.tar.gz)
Find the helm binary in the unpacked directory, and move it to its desired destination (mv linux-amd64/helm /usr/local/bin/helm)
From there, you should be able to run the client and add the stable repo: helm help.

## 安装 Cilium
先是按照网上的教程指定了版本号，结果
```
root@ubuntu-master:/home/master/linux-amd64# helm install cilium cilium/cilium --version 1.9.12 --namespace kube-system
Error: INSTALLATION FAILED: failed to download "cilium/cilium" at version "1.9.12"
```

接着我试着把版本号去掉，就成功了
```
root@ubuntu-master:/home/master/linux-amd64# helm install cilium cilium/cilium  --namespace kube-system
NAME: cilium
LAST DEPLOYED: Wed Feb 23 06:35:54 2022
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
You have successfully installed Cilium with Hubble.

Your release version is 1.11.1.

For any further help, visit https://docs.cilium.io/en/v1.11/gettinghelp
```