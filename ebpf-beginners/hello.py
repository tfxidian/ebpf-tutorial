#!/usr/bin/python
from bcc import BPF

prog = """
int helloworld(void *ctx){
    bpf_trace_printk("Hello world\\n");
    return 0;
    }
"""

b = BPF(text=prog)
clone = b.get_syscall_fnname("clone")
b.attach_kprobe(event=clone, fn_name="helloworld")

b.trace_print()
