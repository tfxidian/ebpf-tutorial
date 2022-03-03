# ebpf tutorial
 
����ļ�����������liz rice�Ĵ������ѧϰ�������������ġ�
ִ�����̣�
�õ�����ebpf.py
`chmod +x ebpf.py`

ִ�н�����£�

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
������ֱ����`python3`�ǲ��еģ���`python ./ebpf.py`����`./ebpf.py`�ǿ��Եġ�

Ȼ�����hello.py������Ҳ��ֱ����ԭ���򣬲������ִ�ģ�

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

��Ҫע��һ�� ` bpf_trace_printk("Hello world\\n");` ����Ľ�β��`\\n`������`\n`
