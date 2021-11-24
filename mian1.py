'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''
import random
Ran = random.randint(1,20)
money=5000
a=0
#   随机生成数字  （开始int，结束int）  []
while a<15:
    num=input("请输入一个数字")
    num=int(num)
    #  键盘输入  随机数
    if num == Ran:
        print("猜对了")
        money=money+300
        a=0
        print(money)
    elif num>Ran:
        print("猜大了")
        money=money-100
        a+=1
        print(money)
    elif num<Ran:
        print("猜小了")
        money=money-100
        a+=1
        print(money)

