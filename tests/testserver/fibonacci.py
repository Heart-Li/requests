#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

"""
其中代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
n=b
m=a+b
a=n
b=m
执行以上程序，输出结果为：
1
1
2
3
5
8
"""


para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

vvv = para_str.find("实例", 0, len(para_str))
print(vvv)


