# -*- coding: utf-8 -*-
"""
数据结构练习
# @Time: 2023/4/12 16:16
# @Author: supermap.lln
# @File: __init__.py.py
"""
import numpy as np


def StrTest():
    """
    字符串测试
    """
    var1 = 'Hello World!'
    var2 = "Runoob"
    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var2[1:5])
    print("已更新字符串 : ", var1[:6] + 'Runoob!')


def TupleTest():
    """
    元组测试
    """
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    # 不需要括号也可以
    tup3 = "a", "b", "c", "d"
    print(type(tup3))
    tub4 = (50)
    print(type(tub4))
    # 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
    tub5 = (50,)
    print(type(tub5))
    # 访问元组
    print("tup1[0]: ", tup1[0])
    print("tup2[1:5]: ", tup2[1:5])

    # 创建一个新的元组
    tup6 = tup1 + tup2
    print("tup6: ", tup6)
    del tup6
    # 实例元组被删除后，输出变量会有异常信息
    print("删除后的元组 tup6 : ", tup6)


def DictTest():
    """
    字典测试
    """
    testDict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print("字典长度： " + len(testDict).__str__())
    print("字典内容： " + str(testDict))
    print("testDict['Name']: ", testDict['Name'])
    print("testDict['Age']: ", testDict['Age'])
    print(testDict.get("Name"))
    del testDict['Name']  # 删除键 'Name'
    testDict.clear()  # 清空字典
    del testDict  # 删除字典


def SetTest():
    """
    集合测试
    """
    setTest = {'1', '2', '3', '4', '5', '6'}
    # 去重
    print(setTest)
    # 快速判断元素是否在集合内
    print("1" in setTest)
    print("7" not in setTest)
    setTest1 = {'1', '2', '3', '4', '5', '7'}
    # 交集
    print(setTest & setTest1)
    # 差集
    print(setTest - setTest1)
    # 并集
    print(setTest | setTest1)
    # 不同时包含的元素
    print(setTest ^ setTest1)
    # 添加元素
    setTest.add('8')
    setTest.update("9")
    print(setTest)
    # 移除元素
    setTest.remove("8")
    # 移除空元素不报错
    setTest.discard("81")
    print(setTest)


def OutExpRes():
    """
    推导式测试
    """
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    # 类型转换
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)
    # 计算推导式 30 以内可以被 3 整除的整数：
    multiples = [i for i in range(30) if i % 3 == 0]
    print(multiples)
    setNew = {i ** 2 for i in (1, 2, 3)}
    print(setNew)
    # 字典推导式
    dictTest = ['Google', 'Runoob', 'Taobao']
    newDict = {key: len(key) for key in dictTest}
    print(newDict)


def ExceptionTest():
    """
    异常捕获测试
    """
    try:
        x = int(input("请输入一个小于5的数字: "))
        if x > 5:
            raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
    except Exception:
        print("不是数字或者数字大于5")


def NpTest():
    """
    numpy 数组练习
    """
    array001 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    a2 = np.arange(5)
    a3 = np.ones((2, 2))
    a4 = np.empty((2, 2))
    a5 = np.random.rand(4, 2)
    a6 = np.linspace(10, 30, 5)
    print('\n序列型数据转化得到数组:', array001,
          '\n显示该数据结构类型:', type(array001),
          '\narange()函数创建的数组:', a2,
          '\nones()函数创建的全1数组:\n', a3,
          '\nempty()函数创建的未赋值的数组:\n', a4,
          '\nrandom()函数创建的随机数组:\n', a5,
          '\nlinespace()函数创建的随机数组:', a6)


if __name__ == '__main__':
    # StrTest()
    # TupleTest()
    # DictTest()
    # SetTest()
    # OutExpRes()
    ExceptionTest()
    # NpTest()
