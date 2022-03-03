# Cilium ebpf tutorial

## ����Ŀ¼
����һ����go�⣬���Զ�ȡ���޸ĺͼ���eBPF���򣬲�������attach��Linux�ں��еĸ��ֹ����ϡ�

This library includes the following packages:

- [asm](https://pkg.go.dev/github.com/cilium/ebpf/asm) contains a basic assembler, allowing you to write eBPF assembly instructions directly within your Go code. (You don't need to use this if you prefer to write your eBPF program in C.)
- [cmd/bpf2go](https://pkg.go.dev/github.com/cilium/ebpf/cmd/bpf2go) allows compiling and embedding eBPF programs written in C within Go code. As well as compiling the C code, it auto-generates Go code for loading and manipulating the eBPF program and map objects.
- [link](https://pkg.go.dev/github.com/cilium/ebpf/link) allows attaching eBPF to various hooks
- [perf](https://pkg.go.dev/github.com/cilium/ebpf/perf) allows reading from a `PERF_EVENT_ARRAY`
- [ringbuf](https://pkg.go.dev/github.com/cilium/ebpf/ringbuf) allows reading from a `BPF_MAP_TYPE_RINGBUF` map
- [features](https://pkg.go.dev/github.com/cilium/ebpf/features) implements the equivalent of `bpftool feature probe` for discovering BPF-related kernel features using native Go.
- [rlimit](https://pkg.go.dev/github.com/cilium/ebpf/rlimit) provides a convenient API to lift the `RLIMIT_MEMLOCK` constraint on kernels before 5.11.

## ʹ��go����ebpf����
���������ο�[cilium ebpf��ʹ��go����ebpf����](https://zhuanlan.zhihu.com/p/466893888)���ҵĻ������ڴ[ehids](https://github.com/ehids/ehids-agent)ʱ�Ͳ�����ˣ����ﲻ���ظ���
����ο�һ��֪���ϵ����������

```
apt install clang llvm
export BPF_CLANG=clang
ִ��git clone https://github.com/cilium/ebpf.git������Ŀ¼ebpf/examples�£��½�Ŀ¼test
����ebpf/examples/headers��test/headers
�½�test/kprobe����ebpf/examples/krope�е�kprobe.c��main.go��test/kprobe��
����ebpf/examples/go.mod��test/go.mod��ִ��go mod tidy
����test/kprobe������go generate���Զ�����bpf_bpfeb.gobpf_bpfeb.obpf_bpfel.gobpf_bpfel.o�ĸ��ļ�
ִ��`go run -exec sudo  .`��������Ӿ�����������
```
����Ч����
```
tf@tf:~/test_cilium_ebpf/kprobe$ go run -exec sudo .
2022/03/03 01:34:30 Waiting for events..
2022/03/03 01:34:31 sys_execve called 4 times
2022/03/03 01:34:32 sys_execve called 4 times
2022/03/03 01:34:33 sys_execve called 4 times
2022/03/03 01:34:34 sys_execve called 4 times
2022/03/03 01:34:35 sys_execve called 4 times
```


## �ο�����
[Linux HIDS����֮eBPFӦ��](https://www.njcx.bid/posts/S6.html) ��ƪ���а���Ҫ�úÿ�����

