#include<stdio.h>
#include<stdbool.h>


int main()
{
    // 字符区分
    signed char name = "2021";  // 有符号可以表示全体实数的数字，默认不写signed为有符号的字符变量
    unsigned char name2 = "2022";  // 无符号的只能表示大于等于0的数

    // 整形区分,可以用signed和unsigned来区分有无符号，默认都是有符号的
    short a = 10;  // 短整形
    int b = 100;  // 整形
    long c = 1000; //长整形
    long long d = 10000; //长长整形

    // 浮点类型
    float e = 1.0f;  // 单精度,若需要和双精度区分，那么可以考虑加上f
    double f = 1.00;  // 双精度
    long double g = 1.000;  // 呃，这个应该是非常高的精度了吧

    // 布尔值
    /*
    在c语言中没有布尔值，0为假，其余为真
    如果要使用布尔值，那么需要引入一个头文件，#include<stbool.h>,这个之后判断语句会学，此处省略...
    */

    // 变量,定义变量需要声明数据类型才可以定义

    return 0;
}
