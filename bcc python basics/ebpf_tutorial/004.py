#!/usr/bin/python3
from bcc import BPF

prog = '''
#include <uapi/linux/ptrace.h>

BPF_HASH(last); 
int do_trace(struct pt_regs *ctx){
    u64 ts, *tsp, delta, key = 0;
    tsp = last.lookup(&key);
    
    if(tsp != NULL){
        delta = bpf_ktime_get_ns() - *tsp;
        if (delta < 1000000000){
            bpf_trace_printk("%d\\n", delta/ 1000000);
        }
        last.delete(&key);
    }   
    ts = bpf_ktime_get_ns();
    last.update(&key, &ts);
    return 0;
}
'''

b = BPF(text=prog)
b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name="do_trace")
start = 0
while(1):
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    if start == 0:
        start = ts
    ts = ts -start
    print("At time %2.f s: multiple syncs detected, last %s ms ago" % (ts, msg))
