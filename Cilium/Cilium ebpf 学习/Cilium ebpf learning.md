# Cilium ebpf tutorial



这是一个纯go库，可以读取、修改和加载eBPF程序，并将它们attach到Linux内核中的各种钩子上。



This library includes the following packages:

- [asm](https://pkg.go.dev/github.com/cilium/ebpf/asm) contains a basic assembler, allowing you to write eBPF assembly instructions directly within your Go code. (You don't need to use this if you prefer to write your eBPF program in C.)
- [cmd/bpf2go](https://pkg.go.dev/github.com/cilium/ebpf/cmd/bpf2go) allows compiling and embedding eBPF programs written in C within Go code. As well as compiling the C code, it auto-generates Go code for loading and manipulating the eBPF program and map objects.
- [link](https://pkg.go.dev/github.com/cilium/ebpf/link) allows attaching eBPF to various hooks
- [perf](https://pkg.go.dev/github.com/cilium/ebpf/perf) allows reading from a `PERF_EVENT_ARRAY`
- [ringbuf](https://pkg.go.dev/github.com/cilium/ebpf/ringbuf) allows reading from a `BPF_MAP_TYPE_RINGBUF` map
- [features](https://pkg.go.dev/github.com/cilium/ebpf/features) implements the equivalent of `bpftool feature probe` for discovering BPF-related kernel features using native Go.
- [rlimit](https://pkg.go.dev/github.com/cilium/ebpf/rlimit) provides a convenient API to lift the `RLIMIT_MEMLOCK` constraint on kernels before 5.11.
