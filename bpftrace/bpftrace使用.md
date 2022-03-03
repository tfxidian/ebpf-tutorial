# bpfrace使用
如果使用ubuntu20.04（或者以上），安装bpftrace提供了snap安装方式：
```
tf@tf:~/test_cilium_ebpf/kprobe$ bpftrace
Command 'bpftrace' not found, but can be installed with:
sudo snap install bpftrace  # version 20210911-2290-v0.13.0, or
sudo apt  install bpftrace  # version 0.11.3-5
```

如果使用snap安装方式可能会遇到这个问题：

```
tf@tf:~/test_cilium_ebpf/kprobe$ sudo bpftrace -e 'BEGIN { printf("Hello, World!\n"); }'
Kernel lockdown is enabled and set to 'confidentiality'. Lockdown mode blocks
parts of BPF which makes it impossible for bpftrace to function. Please see
https://github.com/iovisor/bpftrace/blob/master/INSTALL.md#disable-lockdown
for more details on lockdown and how to disable it.

```
直接搜报错信息，发现怎么说的都有，然后看到报错信息最后一行就给了解决方法，在[disable-lockdown](https://github.com/iovisor/bpftrace/blob/master/INSTALL.md#disable-lockdown)页面发现几种解决方案，
```
1、Disable secure boot in UEFI.
2、Disable validation using mokutil, run the following command, reboot and follow the prompt.
$ sudo mokutil --disable-validation
3、Use the SysRQ+x key combination to temporarily lift lockdown (until next boot)
```
我试了第二种，提示
```
tf@tf:~/test_cilium_ebpf/kprobe$ sudo mokutil --disable-validation
EFI variables are not supported on this system

```
似乎不行，感觉尝试第一种也不会行。

然后看到最后一行
```
Note that you may encounter kernel lockdown error if you install bpftrace via snap incorrectly. Please refer to Ubuntu for more details regrading how to use snap to install bpftrace.
```
上面写了如果用snap安装可能会遇到kernel lockdown 错误！
然后我就把bpftrace 卸载`sudo snap remove bpftrace`
再用apt-get 方式安装`sudo apt-get install bpftrace`
接着执行就没问题了：
```
tf@tf:~/test_cilium_ebpf/kprobe$ sudo bpftrace -e 'BEGIN { printf("Hello, World!\n"); }'
Attaching 1 probe...
Hello, World!

```