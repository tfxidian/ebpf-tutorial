# Cilium install 

## ��װhelm

Every release of Helm provides binary releases for a variety of OSes. These binary versions can be manually downloaded and installed.

Download your desired version [helm](https://github.com/helm/helm/releases)
Unpack it (tar -zxvf helm-v3.0.0-linux-amd64.tar.gz)
Find the helm binary in the unpacked directory, and move it to its desired destination (mv linux-amd64/helm /usr/local/bin/helm)
From there, you should be able to run the client and add the stable repo: helm help.

## ��װ Cilium
���ǰ������ϵĽ̳�ָ���˰汾�ţ����
```
root@ubuntu-master:/home/master/linux-amd64# helm install cilium cilium/cilium --version 1.9.12 --namespace kube-system
Error: INSTALLATION FAILED: failed to download "cilium/cilium" at version "1.9.12"
```

���������ŰѰ汾��ȥ�����ͳɹ���
![image.png](Ciliuminstalled.PNG)

