#!/usr/bin/python3
#-*- coding:utf8 -*-
'''
lhl_str='吕浩亮'
lhl_bytes=lhl_str.encode('utf-8')
print(lhl_bytes,len(lhl_bytes))
lhl_bytes=lhl_str.encode('gbk')
print(lhl_bytes,len(lhl_bytes))
'''
# 定义person类，其父类为object，注意：python中所有类都是从object类直接或间接继承下来的
class Person(object):     # object 所有类的的父类
# 类属性,可以通过对象和类名去访问它
    cnt = 0

    # 初始化，如果init里含有参数，在创建对象时就要写上参数,用于创建对象时进行初始化工作
    # 初始化函数，只要一创建对象，就会自动被调用一次
    def __init__(self,name,age,sex):
        self.____name = name
        self.__age = age
        self.__sex = sex
        Person.cnt +=  1
        
# 方法，除了第一个参数要是self,其他和函数一样
    def study(self):
        print('我能学习')
    
    def sum(self,n):
        s=0
        for i in range(1,n+1):
            s+=i
        return s

    # 修改属性的年龄
    def set_age(self,age):
        self.__age+=1

    def show(self):
        # sep='':以空格分隔输出， sep='x':以x分隔输出
        print(self.____name,self.__age,self.__sex,sep=':')
        
    

# 创建一个person的对象,对象名为p1
p1=Person('橘子','18','女')
p2=Person('lhl','22','男')

print(p1)
# 调用对象p1,采用study方法
p1.study()
# 调用对象p1,采用sum方法
print(p1.sum(100))
# 
p1.show()
p2.show()
p1._Person__name='玉玲珑'
p1._Person__age='24'
p1.show()

print(p1.cnt)
print(Person.cnt)

# 对象的属性,可以给对象任意绑定动态属性，对象的属性是独立的（没个对象的属性不同）
p1.age=30
p2.age=25
print(p1.age,p2.age)















