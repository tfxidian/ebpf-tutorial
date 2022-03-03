# Cilium ebpf tutorial

## 基本目录
这是一个纯go库，可以读取、修改和加载eBPF程序，并将它们attach到Linux内核中的各种钩子上。

This library includes the following packages:

- [asm](https://pkg.go.dev/github.com/cilium/ebpf/asm) contains a basic assembler, allowing you to write eBPF assembly instructions directly within your Go code. (You don't need to use this if you prefer to write your eBPF program in C.)
- [cmd/bpf2go](https://pkg.go.dev/github.com/cilium/ebpf/cmd/bpf2go) allows compiling and embedding eBPF programs written in C within Go code. As well as compiling the C code, it auto-generates Go code for loading and manipulating the eBPF program and map objects.
- [link](https://pkg.go.dev/github.com/cilium/ebpf/link) allows attaching eBPF to various hooks
- [perf](https://pkg.go.dev/github.com/cilium/ebpf/perf) allows reading from a `PERF_EVENT_ARRAY`
- [ringbuf](https://pkg.go.dev/github.com/cilium/ebpf/ringbuf) allows reading from a `BPF_MAP_TYPE_RINGBUF` map
- [features](https://pkg.go.dev/github.com/cilium/ebpf/features) implements the equivalent of `bpftool feature probe` for discovering BPF-related kernel features using native Go.
- [rlimit](https://pkg.go.dev/github.com/cilium/ebpf/rlimit) provides a convenient API to lift the `RLIMIT_MEMLOCK` constraint on kernels before 5.11.

## 使用go开发ebpf程序
开发环境参考[cilium ebpf：使用go开发ebpf程序](https://zhuanlan.zhihu.com/p/466893888)，我的环境是在搭建[ehids](https://github.com/ehids/ehids-agent)时就部署好了，这里不再重复。
这里参考一下知乎上的这个方法：

```
apt install clang llvm
export BPF_CLANG=clang
执行git clone https://github.com/cilium/ebpf.git，进入目录ebpf/examples下，新建目录test
复制ebpf/examples/headers到test/headers
新建test/kprobe复制ebpf/examples/krope中的kprobe.c和main.go到test/kprobe中
复制ebpf/examples/go.mod到test/go.mod，执行go mod tidy
进入test/kprobe，运行go generate，自动生成bpf_bpfeb.gobpf_bpfeb.obpf_bpfel.gobpf_bpfel.o四个文件
执行`go run -exec sudo  .`，这个例子就运行起来了
```
运行效果：
```
tf@tf:~/test_cilium_ebpf/kprobe$ go run -exec sudo .
2022/03/03 01:34:30 Waiting for events..
2022/03/03 01:34:31 sys_execve called 4 times
2022/03/03 01:34:32 sys_execve called 4 times
2022/03/03 01:34:33 sys_execve called 4 times
2022/03/03 01:34:34 sys_execve called 4 times
2022/03/03 01:34:35 sys_execve called 4 times
```


## 参考链接
[Linux HIDS开发之eBPF应用](https://www.njcx.bid/posts/S6.html) 这篇很有帮助要好好看看！

