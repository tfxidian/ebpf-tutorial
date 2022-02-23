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

���������ŰѰ汾��ȥ��������ʾ�ɹ���
![image.png](Ciliuminstalled.PNG)

���ǰ�װ�ܾ�֮��һֱ��ʾ
```
root@ubuntu-master:/home/master# kubectl get pods -n kube-system -o wide
NAME                                    READY   STATUS                  RESTARTS   AGE     IP               NODE            NOMINATED NODE   READINESS GATES
cilium-8xc8s                            0/1     Init:ImagePullBackOff   0          24m     192.168.25.152   ubuntu-node1    <none>           <none>
cilium-hr6zc                            0/1     Init:ImagePullBackOff   0          24m     192.168.25.153   ubuntu-node2    <none>           <none>
cilium-operator-795b8db95f-k9n57        0/1     ImagePullBackOff        0          24m     192.168.25.153   ubuntu-node2    <none>           <none>
cilium-operator-795b8db95f-xjfx6        0/1     ImagePullBackOff        0          24m     192.168.25.152   ubuntu-node1    <none>           <none>
cilium-x2nw6                            0/1     Init:ImagePullBackOff   0          24m     192.168.25.151   ubuntu-master   <none>           <none>
coredns-7ff77c879f-5sx6d                1/1     Running                 0          4h14m   10.244.0.3       ubuntu-master   <none>           <none>
coredns-7ff77c879f-bxbfh                1/1     Running                 0          4h14m   10.244.0.2       ubuntu-master   <none>           <none>
etcd-ubuntu-master                      1/1     Running                 0          4h15m   192.168.25.151   ubuntu-master   <none>           <none>
kube-apiserver-ubuntu-master            1/1     Running                 0          4h15m   192.168.25.151   ubuntu-master   <none>           <none>
```
�⻹��������ѽ��

������ɾ���˰ɣ�ִ������`helm -n kube-system uninstall cilium`��
```
root@ubuntu-master:/home/master# helm -n kube-system uninstall cilium
release "cilium" uninstalled
root@ubuntu-master:/home/master# kubectl get pods -n kube-system -o wide
NAME                                    READY   STATUS        RESTARTS   AGE     IP               NODE            NOMINATED NODE   READINESS GATES
cilium-operator-795b8db95f-k9n57        0/1     Terminating   0          24m     192.168.25.153   ubuntu-node2    <none>           <none>
cilium-operator-795b8db95f-xjfx6        0/1     Terminating   0          24m     192.168.25.152   ubuntu-node1    <none>           <none>
coredns-7ff77c879f-5sx6d                1/1     Running       0          4h15m   10.244.0.3       ubuntu-master   <none>           <none>
coredns-7ff77c879f-bxbfh                1/1     Running       0          4h15m   10.244.0.2       ubuntu-master   <none>           <none>
```
Ȼ��Ϳ���Cilium��ص�podsһ��������ʧ��


�ֿ���һ����װ����������Ҫ�Ȱ�װCilium CNI����װCilium CNI��Ҫж��Flannel CNI

```
# һ�����������ǲ������������ģ���Ϊһ���� cni ж�غ�����pod ������Ϊû�ж�Ӧcni ֧�֣�����pod �޷��������к�ͨ���쳣��
# ������������漰��Ҫ����cni ��һ�㲻���漰�������漰������cni�ģ�Ҳ������²���һ�׼�Ⱥ��Ȼ�����Ǩ�ƣ�
# ж��flannel cni �����
# ���ݲ���ʱ��¼��ȷ�ϰ汾��
[root@master ~]# kubectl delete -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
podsecuritypolicy.policy "psp.flannel.unprivileged" deleted
clusterrole.rbac.authorization.k8s.io "flannel" deleted
clusterrolebinding.rbac.authorization.k8s.io "flannel" deleted
serviceaccount "flannel" deleted
configmap "kube-flannel-cfg" deleted
daemonset.apps "kube-flannel-ds" deleted
[root@master ~]#

[root@master ~]# ll /var/lib/cni/
total 12
drwx------ 3 root root 4096 Oct 28 23:13 cache
drwx------ 2 root root 4096 Nov 17 22:11 flannel
drwxr-xr-x 3 root root 4096 Oct 28 23:13 networks
[root@master ~]# mv /var/lib/cni/ /var/lib/cni.bak
[root@master ~]# ll /var/lib/cni.bak/
cache/    flannel/  networks/
[root@master ~]# ll /etc/cni/net.d/
total 4
-rw-r--r-- 1 root root 292 Nov 17 21:15 10-flannel.conflist
[root@master ~]# mv /etc/cni/net.d/10-flannel.conflist /etc/cni/net.d/10-flannel.conflist.bak
[root@master ~]# systemctl restart kubelet
[root@master ~]#

```

## Install Cilium CNI
```
wget https://raw.githubusercontent.com/cilium/cilium/1.9.0/install/kubernetes/quick-install.yaml
kubectl create -f quick-install.yaml
```

cilium �ṩ��һ��kernel_check ��job ��

```
wget https://raw.githubusercontent.com/cilium/cilium/master/examples/kubernetes/kernel-check/kernel-check.yaml
kubectl apply -f kernel-check.yaml
```

## ���Ľ������
### ��װhelm

Every release of Helm provides binary releases for a variety of OSes. These binary versions can be manually downloaded and installed.

Download your desired version [helm](https://github.com/helm/helm/releases)
Unpack it (tar -zxvf helm-v3.0.0-linux-amd64.tar.gz)
Find the helm binary in the unpacked directory, and move it to its desired destination (mv linux-amd64/helm /usr/local/bin/helm)
From there, you should be able to run the client and add the stable repo: helm help.

### ��װ Cilium
���ǰ������ϵĽ̳�ָ���˰汾�ţ����
```
root@ubuntu-master:/home/master/linux-amd64# helm install cilium cilium/cilium --version 1.9.12 --namespace kube-system
Error: INSTALLATION FAILED: failed to download "cilium/cilium" at version "1.9.12"
```
Ȼ���ҿ��������и����õ���1.7.2���͸�Ϊ1.7.2�����Խ�����£�
```
root@ubuntu-master:/home/master#  helm install cilium cilium/cilium --version 1.7.2 --namespace kube-system
NAME: cilium
LAST DEPLOYED: Wed Feb 23 08:27:45 2022
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

���ź�����������ô�û��ǲ��ɹ�!!!
�ȷ����ˣ������������顣



## �ο�����
[��������֮Kubernetes Cilium CNI ���ٲ���ʵ��](https://blog.csdn.net/LL845876425/article/details/110410377)
