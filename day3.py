'''''''''
#实现输入10个数字，并打印10个数的求和结果
'''''''''
# print("请输入数字")
# n=0
# for i in range(0,10):
#     a=int(input())
#     n+=a
# print(n)
import random

''''''''''''''
#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
''''''''''''''
# l=list(eval(input("10个数字用，隔开")))
# avg=sum(l)/len(l)
# a=sum(l)
# v=max(l)
# print("最大值",v)
# print("平均值",avg)
# print("总和",a)
''''''''''''''''''
#使用random模块，如何产生 50~150之间的数？
''''''''''''''''''
# print(random.randint(50,150))
''''''''''''''''''''
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
''''''''''''''''''''
# a=int(input("请输入你的第一条边长："))
# b=int(input("请输入你的第二条边长："))
# c=int(input("请输入你的第三条边长："))
# if a+b>c and b+c>a and a+c>b:
#     print("可以构成三角形")
#     if a==b==c:
#         print("等边三角形")
#     elif a==b!=c or a==c!=b or  b==c!=a:
#         print("等腰三角形")
#     elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")
''''''''''''''''
#有以下两个数，使用+，-号实现两个数的调换。
'''''''''''''''''
# A=float(input("A:"))
# B=float(input("B:"))
# A=B-A
# B=B-A
# A=B+A
# print("经置换后A值为：",A)
# print("经置换后B值为：",B)
''''''''''''
#实现登陆系统的三次密码输入错误锁定功能.
''''''''''''
# name='root'
# passwd='admin'
#
# for i in range(0,3):
#     a=input("用户名")
#     b=input("密码")
#     if a==name and b==passwd:
#         print("成功进入系统")
#         break
#     elif name !=a or passwd !=b:
#         if i <2:
#             print("用户名密码错误，请重新输入")
#         else:
#             print("对不起，机会只有三次。")
''''''''''''''''''
#编程实现下列图形的打印
''''''''''''''''''
# print("请输入")
# n=eval(input())
# for i in range(1,n+1,2):
#     print("{0:^{1}}".format("*"*i,n))
''''''''''''''
#使用while循环实现NxN乘法表的打印。
''''''''''''''
# row=1
# while row<=9:
#     col=1
#     while col<= row:
#         print('%d*%d=%d\t'%(row,col,row*col),end='')
#         col+=1
#     print('')
#     row+=1
''''''''
#编程实现99乘法表的倒叙打印
''''''''
# line=int(input("请输入打印的行数"))
# for i in range(line,0,-1):
#     for m in range(1,i+1):
#         print('%d*%d=%d'%(m,i,m*i),end='\t')
#         print('')
''''''''
#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
''''''''
# a=20
# i=0
# while 1:
#     a-=3
#     if a <0:
#         print(i)
#         break
#     a+=2
#     i+=1
''''''''
#判断下列变量命名是否合法
''''''''
# print("char合法")
# print("Oax_li合法")
# print("flul合法")
# print("BYTE合法")
# print("Cy%ty不合法")
# print("$123不合法")
# print("3_3不合法")
# print("T_T合法")
''''''''
#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
''''''''
def factorial(n):
    if n==1:return 1
    return n*factorial(n-1)
for i in range(1,21):
    print(i,'!=',factorial(i))