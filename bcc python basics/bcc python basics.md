## 初始化

构造器

### BPF

Syntax: `BPF({text=BPF_program | src_file=filename} [, usdt_contexts=[USDT_object, ...]] [, cflags=[arg1, ...]] [, debug=int])`

不同的初始化方法：

```python
# define entire BPF program in one line:
BPF(text='int do_trace(void *ctx) { bpf_trace_printk("hit!\\n"); return 0; }');

# define program as a variable:
prog = """
int hello(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""
b = BPF(text=prog)

# source a file:
b = BPF(src_file = "vfsreadlat.c") //利用c文件作为输入代码

# include a USDT object:
u = USDT(pid=int(pid))
[...]
b = BPF(text=bpf_text, usdt_contexts=[u])

# add include paths:
u = BPF(text=prog, cflags=["-I/path/to/include"])
```

## Events

### 1. attach_kprobe()

Syntax: `BPF.attach_kprobe(event="event", fn_name="name")`

Instruments the kernel function `event()` using kernel dynamic tracing of the function entry, and attaches our C defined function `name()` to be called when the kernel function is called.

例如：

```python
b.attach_kprobe(event="sys_clone", fn_name="do_trace")
```

这条语句将会插桩内核`sys_clone()`函数，每次它被调用的时候就会运行我们的BPF定义函数`do_trace()`

可以多次调用attach_kprobe()，并将BPF函数附加到多个内核函数。还可以多次调用attach_kprobe()将多个BPF函数附加到同一个内核函数。

### 2. attach_kretprobe()

Syntax: `BPF.attach_kretprobe(event="event", fn_name="name" [, maxactive=int])`

Instruments the return of the kernel function `event()` using kernel dynamic tracing of the function return, and attaches our C defined function `name()` to be called when the kernel function returns.

例如：

```python
b.attach_kretprobe(event="vfs_read", fn_name="do_return")
```

**这将插桩内核vfs_read()函数，然后在每次调用时运行BPF定义的do_return()函数。**您可以多次调用attach_kretprobe()，并将您的BPF函数附加到多个内核函数返回。**还可以多次调用attach_kretprobe()将多个BPF函数附加到同一个内核函数返回。**


### 3. attach_tracepoint()

Syntax: `BPF.attach_tracepoint(tp="tracepoint", fn_name="name")`

Instruments the kernel tracepoint described by `tracepoint`, and when hit, runs the BPF function `name()`.

`tracepoint` 是由内核开发人员在代码中设置的静态 `hook` 点，具有稳定的 `API` 接口，不会随着内核版本的变化而变化，可以提高我们内核跟踪程序的可移植性。但是由于 `tracepoint` 是需要内核研发人员参数编写，因此在内核代码中的数量有限，并不是所有的内核函数中都具有类似的跟踪点

系统中所有的跟踪点都定义在`/sys/kernel/debug/traceing/events`目录中

```shell
alarmtimer    filemap       kvm             power         sync_trace
avc           fs_dax        kvmmmu          printk        syscalls
block         ftrace        libata          pwm           task
bpf_test_run  gpio          mce             qdisc         tcp
bpf_trace     header_event  mdio            random        thermal
...
exceptions    irq           oom             skb           xen
ext4          irq_matrix    page_isolation  smbus         xhci-hcd
fib           irq_vectors   pagemap         sock
fib6          jbd2          page_pool       spi
filelock      kmem          percpu          swiotlb

```

skb下的目录为：

```shell
root@ftang-virtual-machine:/sys/kernel/debug/tracing/events/skb# ls
consume_skb  enable  filter  kfree_skb  skb_copy_datagram_iovec
```


对于bcc程序来说，以监控`kfree_skb`为例，tracepoint程序可以这样写：

```python
b.attach_tracepoint(tp="skb:kfree_skb", fn_name="trace_kfree_skb")
```

bcc遵循tracepoint命名约定，首先是指定要跟踪的子系统，这里是“skb:”，然后是子系统中的跟踪点“kfree_skb”

同样的，我们看一下random目录,下面有urandom_read:

```shell
# define BPF program
bpf_text = """
#include <uapi/linux/ptrace.h>

struct urandom_read_args {
    // from /sys/kernel/debug/tracing/events/random/urandom_read/format
    u64 __unused__;
    u32 got_bits;
    u32 pool_left;
    u32 input_left;
};

int printarg(struct urandom_read_args *args) {
    bpf_trace_printk("%d\\n", args->got_bits);
    return 0;
};
"""

# load BPF program
b = BPF(text=bpf_text)
b.attach_tracepoint("random:urandom_read", "printarg")
```

`open` 系统调用具有两个 `syscalls` 类型的静态跟踪点，分别是 `syscalls:sys_enter_open` 和 `syscalls:sys_exit_open`，前者是进入函数，后者是从函数返回，功能基本等同于 `kprobe/kretprobe`。其中 `syscalls` 表示子系统模块， `sys_enter_open` 表示跟踪点名称。

`tracepoint` 的完整列表可以使用 `perf` 工具的 `perf list` 命令查看，当然如果知道 `tracepoint` 的子系统，也可以进行过滤，比如 `perf list 'syscalls:*'` 命令只用于显示 `syscalls` 相关的 `tracepoints` 。

为了在 eBPF 程序中使用，我们还需要知道 `tracepoint` 相关参数的格式，`syscalls:sys_enter_open` 格式定义在 `/sys/kernel/debug/tracing/events/syscalls/sys_enter_open/format` 文件中。


```shell
$cat /sys/kernel/debug/tracing/events/syscalls/sys_enter_open/format
name: sys_enter_open
ID: 497
format:
	field:unsigned short common_type;	offset:0;	size:2;	signed:0;
	field:unsigned char common_flags;	offset:2;	size:1;	signed:0;
	field:unsigned char common_preempt_count;	offset:3;	size:1;	signed:0;
	field:int common_pid;	offset:4;	size:4;	signed:1;

	field:int nr;	offset:8;	size:4;	signed:1;
	field:const char * filename;	offset:16;	size:8;	signed:0;
	field:int flags;	offset:24;	size:8;	signed:0;
	field:umode_t mode;	offset:32;	size:8;	signed:0;

print fmt: "filename: 0x%08lx, flags: 0x%08lx, mode: 0x%08lx", ((unsigned long)(REC->filename)), ((unsigned long)(REC->flags)), ((unsigned long)(REC->mode))
```



## 参考链接

[使用EBPF追踪LINUX内核](http://kerneltravel.net/blog/2021/ebpf_ljr_9/)

[Trace - 一文读懂tracepoint](https://blog.csdn.net/rikeyone/article/details/116057261)

[使用 tracepoint 跟踪文件 open 系统调用](https://www.ebpf.top/post/open_tracepoint_trace/)
