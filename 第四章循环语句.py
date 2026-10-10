# num=int(input("请输入表白的次数："))
# while num<100:
#     print("小美，我喜欢你！")
#     num+=1
from os import times_result

# 1-100的和
# i=1;sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(f"1-100的值为：{sum}")

# 升级版猜数字小游戏
# import random
# num=random.randint(1,100)
# num_1=int(input("请输入你猜的数字："));sum=0
# while num_1!=num:
#     if num_1>num:
#         print("大了")
#     num_1 = int(input("请再输入你猜的数字："))
#
#     else:
#         print("小了")

# 升级版猜数字小游戏
# import random
# num=random.randint(1,100)
# flag=True;count=0
# while flag:
#     num_1=int(input("请输入你猜的数字："))
#     count+=1
#     if num_1==num:
#         print("你猜对了")
#         flag=False
#     else:
#         if num_1>num:
#             print("偏大了")
#         else:
#             print("偏小了")
# print(f"猜对了，你用了{count}")

# while 循环语句
# print("hello ",end='')
# print("world",end='')
# print("hello\tworld")
# print("some\thao")

# 九九乘法表
'''i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{i}*{j}=%s\t"%(i*j),end='')
        j+=1
    print()
    i+=1'''

# for语句
# name="hung"
# for i in name: # 将name变量挨个取出赋予i临时变量
#     print(i)
# english="hs2wfiuwfw";count=0
# for i in english:
#     print(i)
#     if i=="w":
#         count+=1
# print(f"{english}中，共有：{count}个字母w")

# range语句
# name=range(4)
# print(name)# 表示range中有4个数字包括0，不包括4（0，1，2，3）
'''for i in range(5,10,2):
    print(i)

for i in range(0,10):
    print("送玫瑰花")

count=0
for i in range(0,3273,4):
    if i%2==0:
        count+=1
print(f"有{count}个偶数")

# for示例 （每天都向小美表白，每天都送10朵玫瑰花）
i=0
for i in range(1,101):
    for j in range(1,11):
        print(f"{j}朵玫瑰")
    print(f"第{i}次向小美表白，小美我喜欢你！")
print(f"第{i}天表白成功")

   #while 示例
i=1
while i<=100:
    j=1
    while j<=10:
        print(f"第{j}朵玫瑰花")
        j+=1
    print(f"第{i}次表白，小美我喜欢你！")
    i+=1
print(f"第{i-1}次表白成功！")

   #混合形式
i=1
while i<=100:
    for j in range(1,11):
        print(f"送小美的第{j}朵玫瑰花")
    print(f"第{i}次说小美，我喜欢你！")
    i+=1
print(f"在第{i-1}次表白成功")'''

# 用for语句写99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}\t",end='')
#     print()

# 控制循环continue/break
# for i in range(1,3):
#     for j in range(1,5):
#         print("jjj")
#         break
#         print("iii")
#     print("666")

         # 复习题
# 绩效为第一条件-循环语句发公司案例
# i=1;a=0;j=10000#a拿公司的人数，j为剩余的钱
# while i<=20:
#     import random
#     num = random.randint(1, 10)
#     if num<5:
#         print(f"员工{i}绩效为{num},小于3，没工资")
#     else :
#          if j>=1000:
#              print(f"员工{i}绩效为{num}，发放工资1000元，账户还剩{j - 1000}元")
#              a += 1
#              j = 10000 - 1000 * a
#          else:
#              print("工资已经发完下次拿")
#              break
#     i+=1
 # 金钱为第一条件
money=10000
for i in range(1,21):
    if money<1000:
        print(f"因为账户余额不够，各位下个月领吧")
        break
    else:
        import random
        num=random.randint(1,10)
        if num>=5:
            print(f"员工{i}，绩效{num}达标，领取1000元，余额还剩{money-1000}")
            money = money - 1000

        else:
            print(f"员工{i},绩效{num}，小于5不达标")














