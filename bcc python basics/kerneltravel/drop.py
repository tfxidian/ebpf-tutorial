#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
from bcc import BPF
from time import sleep
# define BPF program

bpf_program = """
#include <uapi/linux/ptrace.h>
struct key_t{
	u64 pid;
};
BPF_HASH(counts, struct key_t);
int trace_kfree_skb(struct pt_regs *ctx) {
	u64 zero = 0, *val, pid;
	pid = bpf_get_current_pid_tgid() >> 32;
	struct key_t key  = {};
	key.pid = pid;
    val = counts.lookup_or_try_init(&key, &zero);
    if (val) {
      (*val)++;
    }
    return 0;
}
"""

def pid_to_comm(pid):
    try:
        comm = open("/proc/%s/comm" % pid, "r").read().rstrip()
        return comm
    except IOError:
        return str(pid)

# load BPF

b = BPF(text=bpf_program)
b.attach_kprobe(event="kfree_skb", fn_name="trace_kfree_skb")

# header
print("Tracing kfree_skb... Ctrl-C to end.")
print("%-10s %-12s %-10s" % ("PID", "COMM", "DROP_COUNTS"))

while 1:
	sleep(1)
	for k, v in sorted(b["counts"].items(),key = lambda counts: counts[1].value):
	  	print("%-10d %-12s %-10d" % (k.pid, pid_to_comm(k.pid), v.value))