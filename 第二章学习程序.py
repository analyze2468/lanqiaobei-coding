from sys import builtin_module_names

print(type("我爱中国！"))

name=type(12.2)
num_float=name
print("类型为：",num_float)

int(13.13)
num_int=int(13.13)
print(type(num_int))
print(num_int)


num_str=str(13)
print(type(num_str),num_str)

# 错误示范
num_int1=int("11")
print(type(num_int1),num_int1)

num_=float(13)
print(type(num_),num_)
#内容限定：中文、数字、符号_、数字
name="张三"
print(name)
AB="张三"
aB="李四"
print(AB,aB)
# def=aB,错误示例引用了特殊函数

# 加号用“+”，取整的除法“//”，取余数的除法“%”，幂的运算“**”
print("2+3=",2+3)
print("5//2=",5//2)
print("9%5=",9%5)
print("2**2=",2**2)
print("2^2=",2^2)
# 赋值运算符
c=1
c+=1 # c=c+1
print("c的值为:",c)

a=1
a-=0 # a=a-0
print(a)

b=4
b/=2 #b=b/2
print(b)

b=5
b*=5 #b=b*5
print(b)

b=6
b//=5 #b=b//5
print(b)

b=7
b%=5 #b=b%5
print(b)

# 单引号示范
name='黄老师'
print(type(name))
# 三引号示范
name="'黄老师'"
print(type(name))
# "\"示范放错误引号前面可以取消引号作用
name="\"黄老师\""
print(type(name))

print('黄老师'+"李老师")

name="黄老师";sex="男"
print("姓名："+name,"性别："+sex)

# 错误示范
# a=1;b=2
# print("我："+a,"他："+b)

#字符串格式化拼接示范
name="黄老师"
print("姓名：%s" %name)
#字符串格式化拼接2
a=4
print("他的年龄：%s"%a)

#所谓值字符串格式化
name="黄老师";age=19
print("他的姓名是：%s,他的年龄为：%s"%(name,age))
# 错误示范
#Sname="凌落宸";age=18
#print("她叫：%s","她的年龄为：%s"%(name,age))
# 改正示范
name="凌落宸";age=18
print("她叫：%s,她的年龄为：%s"%(name,age))
# %d整数 %f浮点数 %s字符串
time=2006;name="黄孝东";age=19
message="我出生于：%d,我的名字是：%s,我年龄为：%d"%(time,name,age)
print(message)
time=2006;name="李 四";age=20
message="我出生于：%d,我的名字是：%s,我的年龄为：%d"%(time,name,age)
print(message)

# 数字宽度和小数限制
num1=11;num2=11.226
print("数字11宽度限制5：%5d"%num1)
print("数字11宽度限制1：%1d"%num1)
print("数字11.225宽度限制在7，小数限制在2：%7.2f"%num2)

# 字符串简易格式化f"{---}"避免使用了%d,%f,%s
name="李四";set_year=2006;birthday=10.34
print(f"他叫：{name},出生在：{set_year}年,生日为：{birthday}")

# 对表达式格式化
# 表达式：具有明确结果的代码语句
print("3*4的结果为:%5s"%(3*4))
print("他的名字是：%s"%name)

# 股票小练习
name="天星传媒"
stock_price=19.88
stock_code="003032"
stock_daily_growth=1.2
growth_day=7
finally_stock_prise=stock_price*stock_daily_growth**7
print(f"公司名称：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数：%.1f,经过7天增长后，股价到了:%.2f"%(stock_daily_growth,finally_stock_prise))

# input 语句
# name=input('请输入你的名字')
# print("原来你的名字叫：%s:"%name)
# age=input("你的年龄是多少：")
# print("哦，原来你这么年轻才：%s岁"%age)
# name_=input("那我该叫你什么：")
# print("真棒！%s爱你："%name_)

# input 字符串类型
# age=input("你多少岁：")
# age=float(age)
# print(f"这个数字类型为:{type(age)}")

# input 小练习
# name=input("请输入您的名字:")
# print("您好：%s"%name)
# num_private=input("请输入您的账号:")
# print(f"欢迎{name}先生，您的账号{num_private}是尊贵的ssssssvip会员，欢迎您的光临！")

# 布尔运算,bool也是属于数字类型
result=10<5
result2=10>5
print(f"10>5的结果是：{result}",type(result))
print("10>5的结果是：%s"%result2,type(result2))







