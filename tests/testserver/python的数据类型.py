#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python有五个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）


# 1 Python数字
# 数字数据类型用于存储数值。
# 他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
# 当你指定一个值时，Number对象就会被创建：
var1 = 1
var2 = 10
# 您也可以使用del语句删除一些对象的引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]
# 您可以通过使用del语句删除单个或多个对象的引用。例如：
del var1, var2

# Python支持四种不同的数字类型：
# int（有符号整型）
# long（长整型[也可以代表八进制和十六进制]）
# float（浮点型）
# complex（复数）

# 注意：long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。lon

# 2 Python字符串
# 字符串或串(String)是由数字、字母、下划线组成的一串字符。
# 一般记为 :
# s="a1a2···an"(n>=0)
# 它是编程语言中表示文本的数据类型。
# python的字串列表有2种取值顺序:
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头
#   R    O   U   O   O   B
#   0    1   2   3   4   5
#  -6   -5  -4  -3  -2  -1

# 字符串截取规则：包含前不包含后
stringTest = "abcdef"
subString = stringTest[1:5]
print(subString)
print("------------1-----------")

str = 'Hello World!'

# 输出完整字符串
print(str)
# 输出字符串中的第一个字符
print(str[0])
# 输出字符串中第三个至第六个之间的字符串
print(str[2:5])
# 输出从第三个字符开始的字符串
print(str[2:])
# 输出字符串两次
print(str * 2)
# 输出连接的字符串
print(str + "TEST")
print("------------2-----------")

lettles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lettles[1:4:2])
# 打印结果：['b', 'd']
# 结论：索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串

# 验证
print(lettles[1:6:2])
print("------------3-----------")

# 3.Python列表
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [786, 'john']

# 输出完整列表
print(list)
# 输出列表的第一个元素
print(list[0])
# 输出第二个至第三个元素
print(list[1:3])
# 输出从第三个开始至列表末尾的所有元素
print(list[2:])
# 输出列表两次
print(tinylist * 2)
# 打印组合的列表
print(list + tinylist)
print("------------4-----------")


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
print("------------5-----------")

# 4.Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print("------------6-----------")
# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
# string、list 和 tuple 都属于 sequence（序列）。
# 注意：
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。
print("------------7-----------")

# 5.Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print("a=")
print(a)
print("b=")
print(b)
print("a 和 b 的差集:")
print(a - b)
print("a 和 b 的并集:")
print(a | b)
print("a 和 b 的交集:")
print(a & b)
print("a 和 b 中不同时存在的元素")
print(a ^ b)

print("------------8-----------")

# 6. Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print("------------9-----------")
# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。