# 系统函数
'''name="ui无法v笔记本"
length=len(name)
print(length)

# 自定义函数
num_1="hjhj"
num_2="hfshf"
num_3="fhfufh"
count=0
for i in num_3:
    count+=1
print(f"字符串的长度为：{count}")'''
#
# def name_len(date):
#     count=0
#     for i in date:
#         count+=1
#     print(f"{date}中有{count}个单位")
# name="fhsufhergeg33s"
# name_len(name)
#
# def name_exa():
#     print("欢迎你，\n请输入您的健康吗和72小时核酸证明")
# name_exa()

# # 函数定义
# def add(x,y):
#     result=x+y
#     return result
# r=add(9,4)
# print(r)
# # 函数参数
# def num(date):
#     if date<=37.5:
#         print("可以进入")
#     else:
#         print("请去医院")
#     return date
# num(38)
# 函数返回值
#
# def add(x,y):
#     result=x+y
#     return result
# r=add(9,4)
# print(r)

 # None语句的实际用法
# def num(age):
#     if age>=18:
#         return age
#     else:
#         return None
# r=num(int(input("请输入数字：")))
# if r==None:
#     print("你未成年！")
# else:
#     print(f"你的年龄：{r}，大于18，成年")
#
# # 函数定义和调用
# def num(x,y):
#     """函数说明：两个数相加的应用
#     :param x:表示两数中的一个数
#     :param y:表示两数中的另一个数
#     :return:表示两个数相加和的返回值
#     """
#     result=x+y
#     return result
# r=num(1,3)
# print(r)

# def name():
#     print("666")
# name()   # 没有None的原因：（1）没有涉及到判断，比如：赋值（2）比如：提要求让别人帮买东西，别人帮你买，给不给你的例子

# 全局变量/局部变量
# num=10
# def abb():
#     global num
#     num=20
#     print(f"{num}")
# abb()
# print(f"{num}")

# ATM 函数案例
'''money=5000000
name=input("请输入你的名字:")
def num_1():
    print(f"{name}你好，您的查询余额为{money}")
def num_2(num):
    global money
    money+=num
    print(f"你的存款额为：{num}")
    print(f"你的余额为：{money}")
def num_3(num):
    global money
    money-=num
    print(f"{name}您好，您的取款额为：{num}")
    print(f"{name}您好，您的余额剩余：{money}")
def tisk():
    print(f"{name}您好，欢迎来到黑马银行ATM，请选择操作：")
    print(f"查询余额：[输入1]")
    print(f"存款：\t[输入2]")
    print(f"取款：\t[输入3]")
    print(f"退出：\t[输入4]")
    return input("请输入您的选择：")
while True:
    main=tisk()
    if main=="1":
        num_1()
        print()
    elif main=="2":
        num=int(input("请输入你的存款额："))
        num_2(num)
        print()
    elif main=="3":
        num=int(input("请输入你的提款额："))
        num_3(num)
        print()
    else:
        print("程序结束！")
        break'''

# 简易点餐系统
'''money=0
def lookup():
    print("今日推荐：“麻辣香锅”")
def order(num):
    global money
    money+=num
def sum_lookup():
    print(f"当前总消费：{money}元")
def menue():
    print("查看今日推荐：\t 选择1")
    print("点单：\t\t 选择2")
    print("查看当前总消费：选择3")
    print("退出系统：\t 选择4")
    return int(input("请选择类型："))
while True:  #菜单函数
    a=menue()
    if a==1:
        lookup()
        print()
    elif a==2:
        num=int(input("菜品，点单金额："))
        order(num)
        print()
    elif a==3:
        sum_lookup()
        print()
    else:
        print("退出系统")
        break'''




