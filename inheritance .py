# -*- coding: utf-8 -*-

"""
Created on 2020-05-16

Updated on 2020-05-16

@author: 小小磊

@requirements: Python 3.5

@decription: Python 类的继承

@ref:
"""

"""    
1.继承:父类有的子类也有（私有方法(__private_method)和私用属性(__private_attrs)除外） —— 类名(父类名) 

2.多继承:继承多个父类（若继承多个父类有相同的函数, 则继承前面的函数）

3.超继承：继承父类并添加了新特性 —— super(类名, self).属性名/方法名(参数)

4.重写：子类中重写父类

5.拓展：子类中父类没有的函数
"""


class Dad:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sport(self, hours):
        print(self.name + "运动{}小时".format(hours))

    def cooking(self):
        print(self.name + "会做红烧肉")

    def smoke(self):
        print(self.name + "吸烟")


class Mother:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cooking(self):
        print(self.name + "会做寿司")


class Girl(Dad):  # 子类（继承）

    def sport(self, hours):  # 超继承
        super(Girl, self).sport(hours)  # 保持父类的特性
        print(self.name + "早晨运动")

    def smoke(self):  # 重写
        print(self.name + "不吸烟")

    def coding(self):  # 拓展
        print(self.name + "是一个程序员")


class Son(Mother, Dad):  # 子类（多继承）
    pass


Girl("丽丽", "20").cooking()  # 继承
Girl("丽丽", "20").sport(1)  # 超继承
Girl("丽丽", "20").smoke()  # 重写
Girl("丽丽", "20").coding()  # 拓展
Son("明明", "25").cooking()  # 多继承
