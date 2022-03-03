
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

