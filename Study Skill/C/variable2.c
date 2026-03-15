#include<stdio.h>


int globle = 100;  // 这个是全局变量，在{}外面

int main()
{
    int local = 10;  // 这个是局部变量，在{}里面
    printf("%d\n", globle);
    printf("%d\n", local);
    // sizeof可以计算表达式或变量的大小，单位是字节
    printf("%d\n", sizeof(local));
    printf("%d\n", sizeof(int));
    printf("%d\n", sizeof(3 + 3.5));
    printf("------------------------------------------------\n");
    // 因为sizeof返回的是一个size_t的类型，本身可以用%d来输出，但是用%zd更标准
    printf("%zd\n", sizeof(char));
    printf("%zd\n", sizeof(_Bool));
    printf("%zd\n", sizeof(short));
    printf("%zd\n", sizeof(int));
    printf("%zd\n", sizeof(long int));
    printf("%zd\n", sizeof(float));
    printf("%zd\n", sizeof(double));
    printf("%zd\n", sizeof(long double));
    return 0;
}
/*
变量数据都是存在内存中的，分为栈区、堆区、静态区
栈区：局部变量、函数参数
堆区：动态内存管理，此处省略
静态区：全局变量，静态变量
--此处目前只做了解后面会学--
*/
 