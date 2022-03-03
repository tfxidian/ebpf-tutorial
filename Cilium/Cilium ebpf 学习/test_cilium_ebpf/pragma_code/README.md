# #pragma
在GCC下，#pragma GCC diagnostic push用于记录当前的诊断状态，#pragma GCC diagnostic pop用于恢复诊断状态。

**可以用于屏蔽局部代码的警告**
```
#pragma GCC diagnostic push 
#pragma GCC diagnostic ignored "-Wformat" 
//code
#pragma GCC diagnostic pop
```

example code:

```
#include <stdio.h>

/************************************************************************/
//记录当前的诊断状态
#pragma GCC diagnostic push
//关闭警告,诊断忽略没有返回值
#pragma GCC diagnostic ignored "-Wreturn-type"

int test1(void)
{
    return;
}
//恢复到之前的诊断状态
#pragma GCC diagnostic pop

int test2(void)
{
    return;
}

/************************************************************************/
int main(int argc, char* argv[])
{
    test1();
    test2();
    
    return 0;
}

```

在gcc下编译
`gcc -o test test.c -Wall`

可以看到test2函数提示警告没有带返回值，而test1没有警告

```
tf@tf:~/test_cilium_ebpf/test$ gcc -o test test.c -Wall
test.c: In function ‘test2’:
test.c:19:5: warning: ‘return’ with no value, in function returning non-void [-Wreturn-type]
   19 |     return;
      |     ^~~~~~
test.c:17:5: note: declared here
   17 | int test2(void)
      |     ^~~~~

```
