# bcc install 

bcc安装过程折腾了我不少时间，这里记录一下我测试成功的步骤：



安装依赖：

`$ sudo apt-get install bpfcc-tools linux-headers-$(uname -r)`

安装流程

```shell
# 安装编译相关工具
$ sudo apt install -y bison build-essential cmake flex git libedit-dev \
  libllvm7 llvm-7-dev libclang-7-dev python zlib1g-dev libelf-dev libfl-dev python3-distutils
  
$ git clone https://github.com/iovisor/bcc.git
$ git checkout v0.23.0 -b branch_v0.23.0
$ git submodule update
$ mkdir bcc/build; cd bcc/build
$ cmake ..
$ make

# 需要特权模式
$ sudo make install  
```

简单看一下目录：

```shell
ftang@ftang-virtual-machine:~/bcc/build$ ls /usr/share/bcc/
examples  introspection  man  tools
ftang@ftang-virtual-machine:/usr/share/bcc/tools$ ls
argdist       dbslower      funcslower      netqtop      pythoncalls  sslsniff    tcpsynbl
bashreadline  dbstat        gethostlatency  netqtop.c    pythonflow   stackcount  tcptop
bindsnoop     dcsnoop       hardirqs        nfsdist      pythongc     statsnoop 
...
cpuunclaimed  funcinterval  mountsnoop      pidpersec    softirqs     tcpstates
criticalstat  funclatency   mysqld_qslower  profile      solisten     tcpsubnet
```

测试一下tcptop，执行`sduo ./tcptop`

![](assets\tcptop.PNG)



## 配置

```
bcctools=/usr/share/bcc/tools
bccexamples=/usr/share/bcc/examples
export PATH=$bcctools:$bccexamples:$PATH
```

让配置生效：

```
source ~/.bashrc 
```

测试一下hello.py：

```
root@ftang-virtual-machine:/usr/share/bcc/tools# hello_world.py
  NetworkManager-781     [000] d...  2016.754075: bpf_trace_printk: Hello, World!
```



## 参考文章

[eBPF 与 Go，超能力组合](https://www.ebpf.top/post/ebpf_and_go/)

[bcc配置路径](https://github.com/iovisor/bcc/blob/master/INSTALL.md#:~:text=add%20bcc%20directory%20to%20your%20%24PATH)