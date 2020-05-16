# -*- coding: utf-8 -*-

"""
Created on 2020-05-16

Updated on 2020-05-16

@author: 小小磊

@requirements: Python 3.5

@decription: Python 类与对象

@ref: https://github.com/Lei-yiyi/object-oriented_programming/blob/master/classAobject.py
"""

"""
类 —— 一群具有 相同特征或相同行为 的事物的一个统称 —— 人类：

（1）类只有一个
（2）特征：一般为特性, Python中称为属性
（3）行为：一般为动作, Python中称为方法（在类的外面定义的一定是函数, 在类的里面定义的才是方法）
（4）在类下可以调用类外的函数
"""


class PeopleInfo:
    head = 1

    def __init__(self, name, age, height):
        """
        构造方法 —— 绝大多数情况下会用__init__方法来创建属性

        :param name:形参, 由类名("张三")来传参实参
        :param age:形参, 由类名(20)来传参实参
        :param height:形参, 由类名(170)来传参实参
        """
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        """
        实例方法 —— 在类下创建的方法, 如果带 self, 那么它叫做实例方法
        """
        print("{}会跑步".format(self.name))

    def __str__(self):
        """
        魔术方法 —— 使用return来定义

        （1）如果使用print函数打印一个对象, 那么会自动调用__str__实例方法
        （2）往往_str__实例方法需要返回一个字符串, 否则会报错
        """
        return "{}".format(self.name)


"""
对象 —— 一个具体的存在 —— 男人 女人 性别不详的人：

（1）对象由类创建（创建对象是一个实例化的过程）, 并且具有类的特征和行为
（2）对象有很多个
（3）每个对象间拥有不同的属性值
（4）每个对象的实例属性是独有的
"""
one_person = PeopleInfo("张三", 20, 170)  # 类名() 默认调用__init__方法, 实参
two_person = PeopleInfo("李四", 30, 180)

one_person.run()
print(one_person.__str__())
