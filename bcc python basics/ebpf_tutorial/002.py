from bcc import BPF

# define BPF program

prog = """
int kprobe__sys_sync(void *ctx) {
	bpf_trace_printk("Hello, sys sync!\\n");
	return 0;
}
"""

b = BPF(text=prog).trace_print()
