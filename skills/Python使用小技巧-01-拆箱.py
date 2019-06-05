#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
1.1 拆箱
"""
a, b, c = 1, 2, 3
print(a, b, c)
# (1, 2, 3)

a, b, c = [1, 2, 3]
print(a, b, c)
# (1, 2, 3)

a, b, c = (2 * i + 1 for i in range(3))
print(a, b, c)
# 1,3,5
a, (b, c), d = [1, (2, 3), 4]

print(a)
print(b)
print(c)
print(d)

