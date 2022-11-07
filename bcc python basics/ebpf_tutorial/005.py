from bcc import  BPF

prog = '''
#include <uapi/linux/ptrace.h>

BPF_ARRAY(counts, u64, 1);

int do_sync(struct pt_regs *ctx){
    u64 *now = 0;
    int index = 0;
    
    counts.increment(index);
    now = counts.lookup(&index);
    if (now !=NULL){
         bpf_trace_printk("%d\\n", *now);
    }
    //bpf_trace_printk("hello\\n");
    return 0;
}
'''

b = BPF(text=prog)
b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name = "do_sync")

while(1):
    try:
        (task, pid,cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    print("task %s At time %.2f s: count sync is %s\n" % (task, ts,msg))