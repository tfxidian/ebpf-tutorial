# ebpf tutorial
 
这个文件夹下我利用liz rice的代码进行学习，基本不做更改。
执行流程：
得到代码ebpf.py
`chmod +x ebpf.py`

执行结果如下：

```
root@ftang-virtual-machine:~/ebpf-beginners# chmod +x ebpf.py
root@ftang-virtual-machine:~/ebpf-beginners# ./ebpf.py
No entries yet
No entries yet
No entries yet
ID 0: 1
ID 0: 1
ID 0: 1
ID 0: 1
ID 0: 1
```
这里我直接用`python3`是不行的，用`python ./ebpf.py`或者`./ebpf.py`是可以的。

然后测试hello.py这里我也是直接用原程序，不过是手打的：

```
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

```

需要注意一下 ` bpf_trace_printk("Hello world\\n");` 这里的结尾是`\\n`而不是`\n`
