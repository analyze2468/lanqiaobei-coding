# --------------------异常模块与包的学习--------------------（错误——BUG）
# 概念：虫子代表bug的原因：第一次计算机出现异常的原因是因为一只虫子——
# f=open(D:/user/h.txt,"r",encoding="utf-8")
'''为什么要捕获异常？
世界上没有完美的程序。
出现了bug怎么办，如何处理？
（1）整个程序因为bug停止运行;（2）对bug进行提醒，整个bug继续运行！！！'''
# ----------------演示捕获异常----------------------

# 捕获语法
# try:
#     f=open("D:/abc.txt","r",encoding="utf-8")       # 注意：except捕获需要看类型！！！
# except:
#     print("出现了异常，因为文件不存在，我将open模式，改成w模式去打开")
#     f=open("D:/abc.txt","w",encoding="utf-8")
# # 捕获指定的异常
# try:
#     print(name)
# except NameError as e:
#     print("因未能命名导致了异常")
#     print(e)
# # 捕获了多个异常
# try:
#     print(name)
#     1/0
# except(NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义，0用法异常")
#     print(e)
#  未正确设计异常类型将无法捕获异常
print("方法一------------------------------------")
# 捕获全部异常方法：
# try:

# except:
print("方法二------------------------------------")
# try:
#     name
# except Exception as e:
#     print("出现了异常！！！")
#     print(e)


# else方法
try:
    name
except Exception as e:
    print("出现了异常！！！")
    print(e)
else:
    print("恭喜，没有异常！！！")
finally:
    print("我是finally,有没有异常我都要执行！！！")

'''总结：标准的捕获语法——————try:+except Exception as e:+else:+finally:
         正常操作的捕获语法：
         try:
         
         except Exception as e:'''


print("--------------------------异常的传递性--------------------------")
# def fun_1():
#     print("fun_1开始执行")
#     num= 1/0     # bug 错误点
#     print("fun_1结束运行")
# def fun_2():
#     print("fun_2开始运行")
#     fun_1()
#     print("fun_2结束运行")
# def fun_3():
#     try:
#         fun_2()
#     except Exception as e:
#         print(f"出现的异常是{e}")
# fun_3()


print("--------------------------模块的该概念和导入--------------------------")
# 模块的定义：一个python文件，里面包括（函数、类、变量）
# 导入模块：拿过来去用


# 模块导入操作
# 一、import用法————使用import导入time模块使用sleep功能
# import time     # 使用python内置的time文件（功能都能使用）
# print(3)
# time.sleep(3)
# print(4)


# 二、from导入 模块名 import 功能
# from time import sleep    # 针对某一个功能使用
# print("你好！")
# sleep(3)
# print("你好！")


# 三、使用*导入time模块的去全部内容
# from time import *
# print("你好！")
# sleep(3)
# print("你好！")

#————————————————————总结：form 模块名+import 函数/类/变量/*


print("-----------------------------自定义模块----------------------------------")
print("方法一------------------")
# import my_modle          # 只引用模块，则模块内函数的应用需要另外说明！！！
# my_modle.test(3,4)
print("方法二------------------")
# from my_modle import *   # 同时引用模块+方法，则可以直接使用模块内函数
# test(5,6)

                    #-------------------------特殊方法一------------------
#if __name__ == '__main__':
# 内置功能“main”:保证在调用模块函数的时候不会运行其中的代码！！！
# 好处：及解决了模块测试代码不能删除的问题，又解决了调用模块时只想要函数功能的想法！！！
from my_modle import *
test(3,4)
                    #-------------------------特殊方法二------------------
#__all__功能，针对*的指定引用

print("-----------------------------Python包----------------------------------")
# 物理意义：一个装py文件的文件夹
# 逻辑上：仍然是模块
# 作用：管理py模块
# 外形：python软件包，有__init__文件
'''
演示python包

# import使用方法：
import my_package.my_modle1
from my_package import my_modle1, my_modle2

my_package.my_modle1.test1()
import my_package.my_modle2
my_package.my_modle2.test2()
print("-----------------------------")
# from语句方法1：
from my_package.my_modle1 import *
test1()
from my_package.my_modle2 import *
test2()
print("-----------------------------")
# from语句方法2：
from my_package import *
my_modle1.test1()
my_modle2.test2()
'''
print("-----------------------------安装第三方包----------------------------------")
# 第三方包：非python官方提供的包，例如：
'''
科学计算:numpy包；# 高级计算机
数据分析：pandas包；
大数据计算：pyspark、apache—flink包
图形可视化常用：pyecharts # 图像
等等等
'''

print("-----------------------------案例练习----------------------------------")
'''
一、要求：
（1）创建一个自定义包
（2）包内提供两个模块
（3）模块内容1：
函数：接受传入字符串，将字符串反转返回
函数：按照下标x和y，对字符串进行切片
（4）模块内容2：
函数：接受传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输入提示信息，通过fianlly关闭文件对象
函数：接收文件路径以及传入数据，将数据追加得写入文件中
----------------------------------------------------------------------------------'''
# 二、包+模块测试：
'''''''''''
from my_package.my_tool.my_str import *
print(my_str1("黄老师"))
print(my_str2("我是黄老师",2,5))
print('----------------------------------------------')
from my_package.my_tool.my_file import *
test_file("D:/Users/H/Desktop/666.txt")    #文件的名字————————位置+命名+格式！！！！
test_file("D:/Users/bill.txt")
append_file("D:/Users/H/Desktop/666.txt","黄老师我们一起加油利用个人成长社会法为社会出一份力量!")
'''''

