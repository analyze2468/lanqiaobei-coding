# my_list=[[1,'你的',4],[3,5,7]]
# print(my_list)
# print(type(my_list))

                        # 列表-------[],,------定义空列表list()
# 列表的下标索引
# my_list=["黄老师","李老师","詹老师"]
# print(my_list[1])
# print(my_list[0])
# print(my_list[-1])
# # 嵌套索引
# my_list2=[[666,'老几',True],[1,2,3]]
# print(my_list[-2][1 ])
# print(type(my_list[0][2]))
# name=my_list2.index([1,2,3])
# print(name)# 下标索引
# my_list[0]="叶老师"#在0号下标索引处替换为叶老师
# print(my_list)
# my_list.insert(1,"刘老师")
# print(my_list)
# my_list.append('666')
# print(my_list)
# my_list.extend('[1,2,3]')
# print(my_list)
# del my_list[2]
# print(my_list)

#公式展示
''''# my_list=[1,2,"黄老师","my"]
# 数据容器下标索引值
name=my_list.index(2)
print(name)
# 数据插入insert
my_list.insert(3,666)
print(my_list)
# 数据删除del
del my_list[3]
print(my_list)
# 数据屁股追加
my_list.append('my')
print(my_list)
# 数据取出2元素的功能
my_list.pop(2)
print(my_list)
# 列表清空
# my_list.clear()
# print(my_list)
# 列表元素数目
num=my_list.count('my')
print(num)
# 取出数据
x=my_list[2]
# 列表总元素长度
num2=len(my_list)
print(num2)'''

# # 案例
# my_list=[21,25,21,23,22,20]
# print(type(my_list))
# name=my_list
# print(name)
# my_list.append(31)
# print(my_list)
# my_list.insert(7,[29,33,30])
# print(my_list)
# del my_list[0]
# print(my_list)
# del my_list[6]
# print(my_list)
# location=my_list.index(31)
# print(location)
# num1=my_list.count(20)
# print(num1)
# num2=len(my_list)
# print(num2)

# 遍历列表while/for
# i=0 # 列表的下标
# while i<len(my_list):
#     num=my_list[i]
#     print(num)
#     i=i+1
# print()
# for i in range(0,len(my_list)):
#     num=my_list[i]
#     print(num,end='')

#                           # 元组--------(),,定义空元组turple()
# #定义元组
# t1=(12,3,4)
# print(f"t1的内容是{t1}，类型为{type(t1)}")# turple
# num=t1.index(3)
# print(num)
#
# i=0
# while i<len(t1):
#     num=t1[i]
#     print(num)
#     i+=1
# 与列表的区别：可以容纳多个数据，有下标索引，内容不可修改，元组是只读的
#
# # 案例
# turtle=('周杰伦',11,['football','music'])
# location=turtle.index(11)
# print(location)
# print(f"学生姓名为{turtle[0]}")
# del turtle[2][0]
# print(turtle)
# turtle[2][0]='coding'
# print(turtle)

                          # 字符串-------"",,定义空字符串---str()
# 字符串也是数据容器（列表，元组）注意：只读不可进行修改
# 字符串的替换
# value='黄老师 and 江老师'
# print(value)
# # replace方法（字符串的替换字符串的本身发生改变）
# value=value.replace("江老师",'汪峰')
# print(value)
# # split方法（将字符串以空格分割转化为列表形式）
# value="and you so du no"
# print(value)
# value2=value.split()
# print(value2)
# # strip方法（）字符串内容移除方法
# x='  sfi,ahi,sjj  '
# x=x.strip()
# print(x)
# y='12sff,sff,wff21'
# y=y.strip('12')
# print(y)
# num=y.count('f')
# print(num)
# num2=len(y)
# print(num2)
# # 遍历
# for i in y:
#     print(i)
#
# i=0
# while i<len(y):
#     num=y[i]
#     print(num)
#     i+=1
# 只能是字符串
'''y="ssf 33 45"
y2=y.replace(45,55)
print(y2)'''

#  字符串容器案例
'''chuan='haunglaoshi lilaoshi liulaishi'
num=chuan.count('li')  # 计数
print(num)
num2=chuan.replace( ' ',"|") # 字符串内容替代
print(num2)
num3=chuan.split("|")  #  字符串转表格
print(num3)'''

# 序列
# 切片列表、元组、字符串取出子序列
my_list=[1,2,3,4,5,6] #步长为n，则每次跳过n-1个元素取
result=my_list[1:4:1] #从列表中取出1-3的下标索引值（包括起始值，不包括结束值）
print(result)
my_tuple=(1,2,3,4,5,6)
result=my_tuple[0:2:1]  # 第三个内容表示步长
print(result)

# 案例
# my_list=["万过月薪","程序员来","python学习者"]
# name=my_list[1]
# print(name)
# num=my_list[::-2]
# print(num)
# del my_list[1]
# print(my_list)
#
# x="万过薪月,员序程马黑来,nohtyP学"
# y=x[::-1][9:13]
# print(y)
# y=y.split(",")
# print(y)

                          # 集合    ------{
'''my_set={"传智教育",'000','黄老师','python','python'}     # 特点：乱序和去重
print(my_set)
my_list1=my_set.add('python')    #  添加的方法 -----.add()
element=my_set.pop()             #  随机提取出来的一个值-----.pop()
print(element)
over=my_set.clear()              #  清除全部内容------.clear()
print(over)
                     #  取插集   set3=set1.different(set2)
# 集合--显差异
set1={"黄老师","李老师","张老师"}
set2={"黄老师","林老师","向老师"}
set3=set1.difference(set2)
print(set3)
# 集合--消差异
set4=set1.difference_update(set2)
print(set4)
# 集合--联合
set5=set1.union(set2)
print(set5)
# 集合--求长度
set6={"1",'2','3','4','1','2'}
num=len(set6)
print(num)'''

#  案例分析

'''my_set=set()           #--------------定义空集合为方法set()----------------
my_list=['黑马程序员','传智博客','黑马程序员','传智博客','liteheima','litcast','best']
for i in my_list:
    my_set.add(i)
print(f"变成的集合结果为：{my_set}")


                #----------------------------字 典--------------------------------------

# 字典的定义：通过字找到相关的含义////python的字典：通过key找到value
# 通过否个东西找到相关的东西 （通过名字找到分数）
# 定义字典的字面量 :{key:value,key:value}
# 定义空字典： dict()---------不允许重复

my_dict={"黄老师":90,"李老师":88,"张老师":89}
score=my_dict["黄老师"]
print(score)
             #---嵌套字典----
my_dict={"周杰伦":{
    "语文":77,
    "数学":66,
    "英语":33
},"王力宏":{
    "语文":88,
    "数学":65,
    "英语":67
},"林俊杰":{
    "语文":89,
    "数学":90,
    "英语":84
}}
print(f"我定义的字典为{my_dict}")

# 问题：如何查询周杰伦的语文成绩？
socer=my_dict["周杰伦"]['语文']
print(socer)

#--------------------------------问题升级，学生分数查询系统----------------------------
x=input("请输入你要查询学生的名字：")
y=input("输入要查询的科目：")
socer=my_dict[x][y]
print(f"学生{x}的分数为{socer}")'''

#   ----------------------字典常用操作--------------------------

'''my_dict={"周杰伦":90,"黄老师":91}
print(f"我定义的字典为：{my_dict}")
# 字典插入内容操作/插入元素,赋值法
# 注意：张学友存在与字典中，则为更改对应key的value
my_dict["张学友"]=80
print(my_dict)
my_dict["周杰伦"]=80
print(my_dict)            # [nnn]:表是字典中以nnn为key的value
# 删除元素,pop（“[]”表示关键的value更改,“（）”表示关键的集合的修改）
my_dict.pop("周杰伦")
print(my_dict)
# 清空元素，clear
my_dict.clear()
print(my_dict)
# 获取全部的key
my_dict={"周杰伦":90,"黄老师":91}
keys=my_dict.keys()
print(keys)
# 遍历字典（方式1，通过获取全部的实现字典的遍历）
for key in keys:
    print(f"字典中对应学生为：{key}")
    print(f"对应的分数为：{my_dict[key]}")
# 遍历字典（方式2，通过直接获取字典集合的key）
for key in my_dict:
    print(f"字典中对应学生为：{key}")
    print(f"对应的分数为：{my_dict[key]}")
# 统计字典的元素数量，len()
num=len(my_dict)
print(num)                   #-------注意！！！key+value的整体被称为一个元素---------

           #--------字典案例练习---------
my_dict={"王力宏":{"部门":"科技部","工资":3000,"级别":1},"周杰伦":{"部门":"市场部","工资":3000,"级别":2},
         "林俊杰":{"部门":"市场部","工资":7000,"级别":3},"张学友":{"部门":"科技部","工资":4000,"级别":1}}
print(f"全体员工当下信息如下：{my_dict}")
for name in my_dict:    # 最重要的是逗号内容！！！
    if my_dict[name]["级别"]==1:
        my_dict[name]["级别"]=my_dict[name]["级别"]+1                  # name=my_dict[key]
                                                                    # name["级别"]=name["级别"]+1
                                                                    # name["工资"]=name["工资"]+1000
                                                                    # my_dict[key]=name
        my_dict[name]["工资"] = my_dict[name]["工资"] + 1000
print(f"全体员工级别为1的员工完成升值加薪操作：{my_dict}")   '''



# 数据容器的通用操作
my_list=[1,2,3,"黄老师",3,4]
my_tuple=(2,1,3,4)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4}
# 数据容器间的相互转化（列表+元组+字符串+集合+字典）
# ！！！！注意！！！   不能转化为字典因为没有value值
print(f"数据容器转化为列表的结果为：{list(my_list)}")
print(f"数据容器转化为列表的结果为：{list(my_tuple)}")
print(f"数据容器转化为列表的结果为：{list(my_str)}")
print(f"数据容器转化为列表的结果为：{list(my_set)}")
print(f"数据容器转化为列表的结果为：{list(my_dict)}")
# 数据容器通用排序功能，sorted(list())，！！！注意：排号的序为列表符
print(f"排序的结果为：{sorted(my_set)}")





