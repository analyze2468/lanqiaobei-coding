               #--------------------------函数的多返回值--------------------------

# 多返回值示例
def test_return():
    return 1,2
x,y=test_return()
print(x)
print(y)

# 函数的多种传参方式
# 函数参数种类：位置参数（一对一） +关键字参数（key对value）+缺省参数+不定长参数(变为元组或者字典)
# 一对一位置参数
def my_test(name,age,gender):
    print(f"输入的名字为：{name},年龄为：{age},性别为：{gender}")
my_test(name="老师",age=22,gender="男")
# 不定长参数
#   （1）数量随意，数据做为元组存在  “*”
def my_user(*args):
    print(f"args的数据类型为：{type(args)},输出的内容为：{args}")  # 为“*”定义方式
  #例题：my_user(1,2,3,"黄老师")
#   （2）数量随意，数据作为字典存在  “**”
def my_user1(**kwargs):
    print(f"kwargs的数据类型为：{type(kwargs)},内容为：{kwargs}")
my_user1(age=23,name="黄老师")


# 函数自身可作为参数传递
# 函数：代码的执行逻辑
# 普通函数：数据不一样，代码的执行逻辑一定
# 函数参数函数：数据一样，代码的执行逻辑不一定
           #---------------------函数作为参数的传递-------------------------------
def compute(x,y):         # 函数定义
    return x+y
def test_function(compute):   # 函数参数传递
    result=compute(2,3)
    print(f"计算的结果为：{result}")
    print(f"compute的参数类型为：{compute}")
test_function(compute)  # 函数调用测试

     #-----------------lambda匿名函数--------------------
# def：定义可带有名称的的函数，lambda：可以定义无名称函数
def test_function(compute):   # 函数参数传递
    result=compute(2,3)
    print(f"计算的结果为：{result}")
    print(f"compute的参数类型为：{compute}")
test_function(lambda x,y: x+y)       #    lambda 函数参数：运算逻辑


