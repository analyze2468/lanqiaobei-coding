# 布尔运算,bool也是属于数字类型
'''result=10<5
result2=10>5
print(f"10>5的结果是：{result}",type(result))
print("10>5的结果是：%s"%result2,type(result2))

bool_1=True
bool_2=False
print(f"bool_1的内容是{bool_1},类型是：{type(bool_1)}")
# 比较运算符的使用 ==，！=，>=，<=
num1=12;num2=14
print(f"12不等于14的结果是：{num1!=num2}")

name1="张三";name2="李四"
print("张三等于李四的结果是：%s"%(name1==name2))
num1=12;num2=13
print(f"12大于等于13：{num1>=num2}",type(num1>=num2))
print(f"12小于等于13：{num1<=num2}",type(num1<=num2))

# if语句基本语法格式
# 格式if age <=23:  并且执行语句需要四个空格
# 如果正确执行print语句，不正确则不执行
age=30
if age <=18:
    print("真好")'''

#if语句的案例
'''print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age=int(input("请输入您的年龄："))
if age >=18:
    print("您已经成年，游玩需要补票10元")
    print("游玩愉快！")
else :
    print("您未成年，可以免费游玩！")'''

# # if else语句的用法
# print("欢迎来到黄老师课堂！")
# degree=int(input("请输入你们的期末成绩："))
# if degree >=90:
#     print("座左边")
# else :
#     print("座右边")
# print('现在开始自行寻找')

# # elif 语句的案例，注意if，elif,else中只有一个会被执行（全部满足执行第一个，都不满足执行else，）
# print("欢迎来到黄老师游乐场！")
# name=input("请输入您的姓名：")
# age=int(input("您好%s,请输入您的年龄："%name))
# rank=int(input("请输入您的vip等级："))
# if age <=18:
#     print("您可以免费游玩此场地")
# elif rank >=3:
#     print("您可以享有免费教练！")
# else :
#     print("不好意思，您不满足条件，需要缴纳20元费用才可有教练")


# 猜数字游戏
# print("我们来玩个1-10以内的猜数字游戏")
# if int(input("请输入第一次猜想的数字："))==10:
#     print("答对了，真棒！")
# elif int(input("错了，再给你一次机会："))==10:
#     print("答对哦，真棒！")
# elif int(input("答错了，再给你最后一次机会："))==10:
#     print("终于答对了，真棒！")
# else :
#     print("笨蛋我的答案是10！")

# 勾股定理求斜边
'''x=int(input("请输入三角形的第一条直角边："))
y=int(input("请输入三角形的第二条直角边："))
import math
z=math.sqrt(x**2+y**2)
z=int(z)
print(f"斜边的长为：{z}")'''

# 输入三角形的两条边一条斜边看是否构成直角三角形
'''import math
x=int(input("请输入一条边："))
y=int(input("请输入另一条边："))
z=int(input("请输入斜边："))
if z==math.sqrt(x**2+y**2):
    print("三条边满足勾股数可以构成直角三角形")
else:
    print("无法构成直角三角形")'''

# if嵌套判断语句
# hight=int(input("请输入你的身高:"))
# if hight>120:
#     print("您的身高大于120，不可以免费")
#     print("但是您的vip等级大于3，可以免费")
#     if int(input("请输入您的vip等级"))>3:
#         print("恭喜你！vip等级大于3可以免费")
#     else:
#         print("不好意思，您需要支付10元才可以游玩。")
# else:
#     print("恭喜你，可以免费游玩！")

# 复杂嵌套语句2
'''age=int(input("请输入您的年龄："))
if age>=18:
    if age<=30:
        print("您满足基础条件")
        if int(input("请输入入职时间（年）："))>2:
            print("可领取奖励")
        elif int(input("请输入级别（vip）"))>3:
            print("可以领取奖励")
        else :
            print("不好意思，两个条件都不满足，只能有安慰奖！")
    else:
        print("超出年龄阶段不可领取")
else:
    print("未成年不可领取奖励")'''

# 案例随机猜数字
'''import random
num =random.randint(1,10)
perpare=input("这是一个猜数字游戏，你只能猜1-10里面的数字,你只需要输入是否准备好：")
if perpare =="准备好了":
    print("游戏开始！")
else:
    print("请开始准备")
num_1=int(input("请输入你猜的数字："))
if num_1!=num:
    if num_1>num:
        print("偏大了！")
    elif num_1<num:
        print("偏小了！")
else:
    print("真棒！一次就对")
num_2=int(input("再给你一次机会："))
if num_2!=num:
    if num_2>num:
        print("偏大了！")
    elif num_2<num:
        print("偏小了！")
else:
    print("答对了！")
num_3=int(input("给你最后一次机会："))
if num_3!=num:
    if num_3>num:
        print("害，偏大了，你没机会了")
    elif num_3<num:
        print("害，偏小了，你没机会了")
else:
    print("终于答对了！")'''

# 猜数字第二弹
import random
num =random.randint(1,10)
num_1=int(input("请输入你猜的数字："))
if num_1==num:
    print("恭喜回答正确")
else:
    if num_1>num:
        print("偏大了")
    else:
        print("偏小了")

    num_2=int(input("第二次机会:"))
    if num_2==num:
        print("回答正确")
    else:
        if num_2>num:
            print("偏大了")
        else:
            print("偏小了")
        num_3=int(input("最后一次机会："))
        if num_3==num:
            print("回答正确")
        else:
            if num_3>num:
                print("还是大了")
            else:
                print("还是小了")









