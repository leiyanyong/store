
#
#
# '''
#  1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
#  2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# #3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
#  4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
#  5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法
# '''
#
# class cooker :
#     __name=''
#     __age=''
#
#     def set_name(self,name):
#         self.__name=name
#
#     def get_name(self):
#         return self.__name
#
#     def set__age(self,age):
#         self.__age =age
#
#     def get_age(self):
#         return self.__age
#
#     def cooking(self):
#         print('蒸饭1')
#
# class new_cooker(cooker):
#     def cooking2(self):
#         print('炒菜')
#     def cooking(self):
#         super().cooking()
#         print('蒸饭')
#
#
# class test(new_cooker):
#     pass
#
# b=test()
# b.set__age('20')
# b.set_name('tony')
# print(b.get_age(),b.get_name())
# b.cooking()
# b.cooking2()
#
# a=new_cooker()
# a.cooking()
# a.cooking2()

'''
#  i.	人：年龄，性别，姓名。
#
#  ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
#
#  iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''

class person:
    age=''
    sex=''
    name=''

class worker(person):
     def working(self):
         print('正在干活')

class student(worker):
     def learn(self):
         print('正在学习')
     def sing(self):
         print('正常唱歌')

a=student()
a.age='10'
a.sex='男'
a.name='xiao'
a.work_type='工人'
a.number='10055'
a.working()
a.learn()
a.sing()
