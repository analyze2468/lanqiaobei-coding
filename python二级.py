# # ----------------一、format格式化-------------------
# # 方法一、
# print("{}你好".format("黄老师"))
# # 方法二、
# s="二级考试"
# print("{0:*^25}".format(s))    #要求：顺序！！！（内容"0"+":"+填充"*"+对齐">^<"+步长"25"+千位分隔符,+精度".2f"）
# 完整{}.format索引情况：{[索引/变量]：[填充字符][对齐][步长][千分位分隔符][.精度][类型码（b"二进制"/o"八进制"/x"十六进制"）]}
# print("{0:-^30}".format("黄老师"))
# print("{0:{1}{2}{3}}".format(s,"*","^",25))
# 例题实战
# n=int(input("请输入正整数："))
# n=eval(input("请输入正整数"))  注：把填入数据的双引号去除
# print(n)
# print("n的数据类型：{}",type(n))\

# ----------------二、turtle海龟制图-------------------
'''
# 1-导入
import turtle
turtle.setup(600,400,0,0)
# 2-移动
turtle.fd(100)
turtle.bk(50)
# 3-转向
turtle.left(0)
turtle.right(90)
turtle.seth(90) # 绝对角度：不论海龟现在在哪都变成竖直向上
# 4-画笔控制(pen)
turtle.penup()
turtle.pendown()
turtle.pensize(2)
turtle.pencolor("red")
# 5-填充图形
turtle.begin_fill()
# turtle.color(0.2,0.8,0)  # rgb混合色
turtle.color("red")
turtle.end_fill()
# 6-定位
# turtle.goto(-200,200)
# 7-隐藏画笔
turtle.hideturtle()
turtle.done()
# 8-画圆
# turtle.circle(半径+逆时针度数)
# 9-知识点
# 五角星：五条边的度数为：144度，正五边形：72度，重复用：for i in range(4)
'''
# import random
# 例题一（五角星）
# import turtle
# turtle.setup(600,400,0,0)
# turtle.pensize(3)
# turtle.color("red","blue")
# turtle.begin_fill()
# for i in range(5):
#     turtle.fd(100)
#     turtle.right(144)
# turtle.end_fill()
# turtle.done()
print("--------------------------------")
# 例题二（同心圆）
# import turtle
# import random
# r=[50,100,150]
# turtle.setup(600,400,0,0)  # 建立画布
# turtle.pensize(2)          # 画笔尺寸确定
# # turtle.goto()  注：同心的关键一步(圆心固定)！！！
# turtle.left(90)
# for i in r:
#     x=random.choice(["red","blue","green"])     # 注：内部一定要为列表“random.randint(1:10)”中1：10是列表的表示
#     turtle.pencolor(x)      # 随机函数确定画笔颜色
#     turtle.penup()           # 换海龟坐标必须抬落笔！！！
#     turtle.goto(i,0)      # 从圆的右边界开始绘图！
#     turtle.pendown()        # goto是绝对坐标:只与海龟原始坐标0，0为基准
#     turtle.circle(i)    # 逆时针！！！
# turtle.done()
print('-------------------')
# 海龟例题三
# import turtle as t  # 导包
# import random
# t.setup(600,400,0,0)
# t.pensize(2)
# color_1=random.choice(["red",'green','blue'])
# t.pencolor(color_1)
# for i in range(4):
#     t.fd(200)
#     t.left(90)
# # 画圆步骤
# t.right(45)
# t.circle(100*2**(1/2))   # 易错点：2**(1/2)，必须加括号！！！
# t.done()     # 重要!!!
print("-----------方法二-------------")   # way二： print("{0:-^25}".format("方法二"))
# # 画圆步骤
# t.left(135)
# t.penup()
# t.goto(200,200)
# t.pendown()
# t.circle(100*2**(1/2))
# t.done()
# 总结：海龟（首“setup”+尾“done”+for+pen.size/color+t.begin_fill+t.end_fill+圆逆时针和坐标与圆心的关系）

# ----------------三、第三方库-------------------
# 1-jieba库
# import jieba    # 把字符串类型用词语类型变成列表形式！！！
# data="国家计算机二级python考试"
# name=jieba.lcut(data)
# print(name)
# print('----------------------------------')
# # 2-wordcloud库
#
# print("{0:-^100}".format("模拟题练习"))

# 一：满二叉树叶子结构公式(总节点数)：2**k-1，第k层节点数：2**(k-1)
# 二：进制转换问题：二（Ob）——十，八(Oo)——十，十六(Ox)——十，方法：eg.ob1010:1*2**3+0*2**2+1*2**1+0*2**0
# 十转其他：十——二（Ob）,十——八（Oo）,十——十六（Ox），方法：eg.520:除于后余数为1和0形式，答案为：Oo1010
# print(bin(10)) #  十进制转化为二进制
# print(oct(10)) #  十进制转化为八进制
# print(hex(163)) # 十进制转化为十六进制：a-d，表示10-13！！！
# 特别注意：各个进制之间可以相加减，python可以兼容例如：“OxAD0+50”是正确的！！！

"""三：知识点补充：
（1）文件读取两种方式：文本自动编码/解码+二进制字节流
（2）write:writelines/write/seek 注：没有writetext!!!
（3）序列类型：只能装有一维的数据！
（4）字典属于映射类型：由高维键值对组成
（5） x= 10;y=3; divmod(x,y): x为除数，y为余数
（6）字典键值对索引：d[""]和d.get(""),区别：前者没取到报错，后者输出None!!!
（7）并行符号和换行符号：end=""+/
（8）字典键值对方法：d={key,value},d.get(key,0)与d[key]目的相同
（9）同时取出字典中的key和value方法：for k,v in d.items()   注意：items取出来的是元组包裹的（key和value）
（10）复数形式：实部：z.real，虚部：z.imag，“z=3+4j”
（11）continue:跳过当前一次循环，break：跳出循环
（12）写入csv格式：关键写入“list=[a,b,c],”,{",".join(list)},通过逗号将abc连接起来
（13）python考试写法：control+n创建，control+s保存
（14）count和len的用法：count(list.count/str.count)“单个数”,len()“总长度”
（15）文件写入清空问题：f.write不会清空，f=open("","w")会清空！
"""
#  ---------------------模拟一：基础编程题----------------------

# # 练习一：
# print("-----方法一--------")
# x=((3**2+5*6**7)/8)**0.5
# x=round(x,3)   # round用于保留小数位次
# print(x)
# print("-----方法二--------")
# x=((3**2+5*6**7)/8)**0.5
# print("{:.3f}".format(x))
#
# # 练习二：进制题+format格式化应用
# data=0x4DC0+50
# print("二进制{0:0b}、八进制{0:0b}、十进制{0}、十六进制{0:0x}".format(data))

# 练习三：海龟制图
# import turtle as t
# t.setup(600,400,0,0)
# t.pensize(2)
# re=0
# # t.begin_fill()
# for i in range(4):
#     # t.color("red","blue")
#     t.fd(200)
#     re+=90
#     t.seth(re)  # 注意：绝对角度！！！
# t.end_fill()
# t.done()

# 练习四：词语第三方库jieba的考查
# import jieba
# s="中国特色特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美\好生活需要和不平衡不充分的发展之间的矛盾。"
# n=len(s)
# m=len(jieba.lcut(s))
# print("中文字符数为{0},中文词语数为{1}".format(n,m))
'''
# 练习五：算列表中各类型的数量（必考题！）——————通用方法：字典{key,value}
print("--------方法一--------")
ls=["综合","理工","综合","综合","综合","综合","综合","师范","理工","综合","理工","综合","理工","理工","理工","理工","师范","综合","农林","理工","综合","理工","农林","民族","军事"]
# 目标：d={key,value}和key:value
d={}
for i in ls:      # 核心步骤！！
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
# 字典标准可视化
for k,v in d.items():
    print("{0}:{1}".format(k,v))
print("--------方法二--------")
ls=["综合","理工","综合","综合","综合","综合","综合","师范","理工","综合","理工","综合","理工","理工","理工","理工","师范","综合","农林","理工","综合","理工","农林","民族","军事"]
d={}
for i in ls:
    d[i]=d.get(i,0)+1    # 核心步骤！！！ # 注意：利用get取值自身有if判断的功能！
for k,v in d.items():
    print("{0}:{1}".format(k,v))

# 练习六：压轴题文件处理题
print("--------------第一问-------------")
fi=open("D:/Users/H/Desktop/sensor.txt","r",encoding="utf-8")
fo=open("D:/Users/H/Desktop/arpa001.txt","w")
data=fi.readlines()
for line in data:
    line_1=line.strip("\n")      # 换行符的符号："\n "!!!
    line_2=line_1.split(",")
    # print(line_2)
    if line_2[1]=="earpa001":
        fo.write("{0},{1},{2},{3}\n".format(line_2[0],line_2[1],line_2[2],line_2[3]))
fi.close()
fo.close()
print("-----------------第二问----------------")
f=open("D:/Users/H/Desktop/arpa001.txt","r",encoding="utf-8")
f1=open("D:/Users/H/Desktop/999.txt","w")
d={}
for i in f.readlines():
    i=i.strip("\n")
    i=i.split(",")
    x=i[2]+"-"+i[3]
    d[x]=d.get(x,0)+1
# print(d)
for k,v in d.items():
    # print("{0}:{1}".format(k,v))
    f1.write("{0}:{1}\n".format(k,v))
f.close()
f1.close()
'''
# ---------------------------------综合大题练习----------------------------------------

# import jieba
# f=open("D:/Users/H/Desktop/article.txt","r",encoding="utf-8")
# f1=open("D:/Users/H/Desktop/result.txt","w",encoding="utf-8")
# dict={}
# for line in f.readlines():
#     line_1=line.strip("\n")
#     line_2=line_1.replace("，",'')
#     line_3=line_2.replace("。","")
#     line_4=jieba.lcut(line_3)    # 把字符串通过词语的方式变成了列表的形式！
#     # print(line_4)
#     for word in line_4:
#         dict[word]=dict.get(word,0)+1
# # print(dict.values()/keys())    # 直接打印value的方法
# # 自定义函数代替lambada函数排序问题
# def count(item):
#     return item[1]
# sort_=sorted(dict.items(),key=count,reverse=True)
# # print(sort_)
# # for i in sort_:
#     # print("{0}:{1}".format(i[0],i[1]))
# for i in sort_:
#     if i[1]>=2:
#         f1.write("{0}:{1}\n".format(i[0],i[1]))
# f.close()
# f1.close()

#--------------------模拟题三--------------------

# 要求：input语句输入整数，如果是整数直接返回，如果是小数或其他就显示再次输入！！
# def getInput():
#     try:
#         s=eval(input("请输入一个整数："))     # 注意：eval只能用于脱去数字，不能脱字母会有识别错误！！！
#         if s==int(s):
#             return s
#         else:
#             while True:
#                 s = eval(input("请输入一个整数："))
#                 if s==int(s):
#                     return s   # return：总用回顾（返回值+终止循环）
#                 else:
#                     continue
#     except Exception as e:   # Exception as e 的作用是把bug名称赋值出来
#         # print(e)
#         return getInput()     # 意思：被捕获后返回getinput再执行一遍
#         # pass                # 意思：被捕获后啥也不干
# print(getInput())

#-----------------------综合大题---------------------------
# print("--------第一问--------")
# f=open("D:/Users/H/Desktop/论语.txt","r",encoding="utf-8")
# f_1=open("D:/Users/H/Desktop/论语原文.txt","w")
# center=False  # 开关作用！！！
# for line in f.readlines():
#     if "【原文】"in line:
#         center=True
#         f_1.write(line)
#     elif "【注释】"in line:
#         center=False
#     elif center==True:
#         line=line.strip(" ")
#         if line.count("\n")!=len(line):   #  空行的表示方法
#             f_1.write(line)
# f_1.close()
# f.close()
# print("------------第二问------------")
# f_1_=open("D:/Users/H/Desktop/论语原文.txt","r")
# f_2=open("D:/Users/H/Desktop/论语译文.txt","w")
# for line in f_1_.readlines():
#     for i in range(1,3):
#         line=line.replace(f"({i})","")
#         f_2.write(line)
# f_1_.close()
# f_2.close()

#------------------------------------模拟题四-------------------------------------------
# turtle 大题代码：
# import turtle
# turtle.setup(600,400,0,0)
# turtle.left(30)
# turtle.fd(200)
# turtle.right(60)
# turtle.fd(200)
# turtle.right(120)
# turtle.fd(200)
# turtle.right(60)
# turtle.fd(200)

#--------------------------- 综合大题-------------------------------------
# -----第一问-------：
# f=open("D:/Users/H/Desktop/命运.txt","r",encoding="utf-8")
# data=f.read()
# # print(data)
# dict_={}
# for i in data:
#     syboml="，","。","：","‘","’","”","“","！","?","-","《","》","\n","（","）","“","”",'"'
#     if i in syboml:
#         continue       # 仅用于循环过程中
#     else:
#         dict_[i]=dict_.get(i,0)+1
# # print(dict_)
# dict_=list(dict_.items())    # d.items()是字典变成元组的；把元组转化到列表里面去加“list()转化”
# # print(dict_)
# dict_.sort(key=lambda x:x[1],reverse=True)
# # print("{}:{}".format(dict_[0][0],dict_[0][1]))
# # --------------第二问----------------：
# # for i in range(10):
# #     print(dict_[i][0],end="")
# # --------------第三问----------------
# f1=open("D:/Users/H/Desktop/命运-频次排序.txt","w",encoding="utf-8")
# for i in dict_:
#     f1.write(str(i[0])+":"+str(i[1]))

'''
python二级真题
(1)软件工程三要素：方法、工具、过程
(2)R-S相连接，需要相同的属性
(3)线性表的链式存储结构多余顺序存储结构
(4)算法的有穷性：程序的运行时间是有限的
（5）软件设计的模块准则：高内聚低耦合
（6）每个程序都有统一的运算模式：ipo模式
（7）再a和b之间产生随机的整数用random.randint。产生随机的小数用random.uniform
（8）continue:只用于循环语句或“循环+分支”中，不存在与分支语句中（if-else）
（9）break只能打破一个循环
（10）while True:循环，while False:终止。while 1/10：循环，while 0:终止
（11）sort(x)对x进行排序，但不会将结果写回到原变量，list.sort(key=lambda x:x[1],reverse=True))   注：针对的是列表！！！
(12)copy的使用：只是单纯的复制内容，复制前后列表还是有区别的    eg:da=[1,2,3];fa=da.copy()  注意：此处的da和fa是不相同的
（13）pop的用法:字典中拿出元素，对于原字典来说少了一个元素
(14)d.items()方法：取出key和value组成元组，但打印出来为dict_items([("name":"黄老师"),("age":20)])
（15）remove语句在循环语句的删除规则：列表中间删除后自动往前移。循环索引不变
(16)计算阶乘方法：把n利用循环拆开成“1到n”，每循环到其中一个数就乘之前的积
（17）判断奇偶数的方法：n%2看是余零还是一
（18）判断整数的方法：s=int(s)
（19）判断大小写用isupper()
(20)把字符串中部分字符去除用replce()！！！
（21）字符串中字符数量大则自定义“垃圾变量”+if i not in num
eg:
da=[1,2,4,0,0,0]
for i in da:
    if i==0:
        da.remove(i)
print(da)
（16）字符串拼接：“a”+“b”="ab",“a+b”=a+b  易错点！！！
（17）文件读取seek(2)跳过文件的前两个字符
'''
# dict={"name":"黄老师","age":20}
# print(list(dict.items()))
# print(dict.items())
# # 案例示范
# da=[1,2,4,0,0,0]
# for i in da:
#     if i==0:
#         da.remove(i)
# print(da)
#
# # 基础编程题：
# # 第一题：
# data=input("输入")
# data_=data.split(",")
# print(data_[1]*int(data_[0]),int(data_[0]),data_[1]*int(data_[0]))



# 练习一：（n的阶如何计算）
# n=eval(input("请输入一个整数："))
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
# print("{0}阶乘为：{1}".format(n,sum))

# 练习二：（奇偶数判断）
# data=eval(input("请输入一个整数："))
# if data%2==0:
#     print("这个数是偶数！")
# elif data%2==1:
#     print("这个数是奇数！")

# 练习三：（整数判断）
# data=eval(input("请输入一个数："))
# if data==int(data):
#     print('这个数是整数')
# else:
#     print("这个数是非整数")

# 练习四：（清除字符串的垃圾符号）
# content="你好，我是黄老师，请问你有什么需求，可以随时和我沟通"
# content=content.replace("，"," ")
# print(content)
# list_0=[("黄老师",20),("王老师",22),("张老师",19)]
# list_0.sort(key=lambda x:x[1],reverse=True)
# print(list_0)
"""
知识点总结：
（1）sort排序：原地排序，eg：list=[],list.sort(key,reverse)  注：不需要赋值！！！
（2）字符串：s=s.replace(old,new),s=s.split("_"),s=s.strip(),s=" ".join(s) 注：用空格把s字符串链接起来
（3）列表：list.append()  注：原地修改，尾部增加数，不需要赋值,list.remove()  注：不赋值,s=list.pop("下标")
"""

# 练习五：（文件读取中大量垃圾符号清理方法）
# s="你好，欢迎来到快乐之都，请选择您喜欢的游玩项目，。！？"
# data="，。！？"
# for i in s:
#     if i not in data:
#         print(i,end="")
#     else:
#         continue

# 基础编程题：
# 一：
# data=input("请输入内容：")
# data=data.split(",")
# s_1=data[0]
# s_2=data[1]
# print("{0:{1}^20}".format(s_1,s_2))  #  format里面只能写变量，不能写索引（结构：“{0：}”）

# 二、
# data=input("请输入有1和0组成的二进制字符：")
# data_1=int(data,2)   # int():参数默认为十进制/int(a,b)：a必须为字符串，b为进制类型
# print("{0:o}".format(data_1))

# 三、
# f=open("D:/Users/H/Desktop/新建 文本文档.txt","r",encoding="utf-8")
# data=f.readlines()
# sum=0
# for line in data:
#     line_1=line.strip("\n")
#     line_2=line_1.split(",")
#     # len1=len(line_2)
#     num=0
#     for i in line_2:
#         i_=i.split(":")
#         i_1=int(i_[1])
#         sum+=i_1
#         num+=1
#     print("总和为：{0:.1f},平均值为:{1:.2f}".format(sum,sum/num))
# f.close()
# 计算列表中元素个数的两种方法：(1)len法；(2)循环法“i=0————i+=1”；

# 四、
# import turtle
# turtle.setup(600,400,0,0)
# r=10
# for i in range(4):
#     turtle.seth(90)
#     turtle.circle(r)
#     turtle.penup()
#     r+=40
#     turtle.goto(r, 0)
#     turtle.pendown()
# turtle.done()

# 五、
# import jieba
# data=input("请输入一句话：")
# data=jieba.lcut(data)
# # print(data)
# symbol="“","”","、","，","。",","
# num=0
# d={}
# for i in data:
#     if i in symbol:
#         continue
#     else:
#         d[i]=d.get(i,0)+1
#         num=num+1
#         print(i,end="/")
# print("\n")
# print("中文词语数是：{0}个".format(num))
# # print(d)
# d_1=list(d.items())
# d_1.sort(key=lambda x:x[1],reverse=True)
# # print(d_1)
# for i in d_1:
#     name=i[0]
#     liang=i[1]
#     print("{0}:{1}".format(name,liang))
# name_max=d_1[0][0]
# liang_max=d_1[0][1]
# print("出现最多的是({0})，次数是:{1}次".format(name_max,liang_max))

# 列表中pop用法：
# data=[1,2,3]
# data_1=data.pop(2)
# print(data)
# print(data_1)
#
# # 切片方法(所有字面量都可以用)：
# s="你好，黄老师呀"
# data=s[:-4]  # 索引值一正一负可以用于截取，清除不用的量。(用法总结：（1）去除部分，（2）删除部分”大面积内容情况“)

# 五、
# import random
# random.seed(123)
# for i in range(10):
#     print(random.randint(1,1000),end=",")

# 六、（易错代码）
# data=input("请输入姓名性别年龄：\n")
# num=0 # 男
# r=0  # 总人数
# sum=0 # 总年龄
# for i in data:
#     data_1=data.strip("\n")             # 注意：一定要注意strip在split的前面，因为strip只能处理字符串
#     data_2=data_1.split(" ")
#     # data=data.strip()
#     if data_2[1]=="男":
#         num+=1
#     else:
#         continue
#     sum+=int(data_2[2])
#     r+=1
# a_sum=sum/r
# print("\n平均年龄是{0}，男性人数是{1}".format(a_sum,num))

# 修改代码：
# data=input("请输入姓名性别年龄：\n")
# num=0 # 男
# r=0  # 总人数
# sum=0 # 总年龄
# while True:
#     data_1=data.strip("\n")
#     data_2=data_1.split(" ")
#     if data_2[1]=="男":
#         num+=1
#     sum+=int(data_2[2])
#     r+=1
#     data=input("请输入姓名性别年龄：\n")
#     if data=="":
#         break   # 注意：break和continue都是作用于循环，而不是分支语句！！！
# a_sum=sum/r
# print("\n平均年龄是{0:.2f}，男性人数是{1}".format(a_sum,num))
# import jieba
# data=input("请输入一串中文：")
# num_1=len(data)
# num_2=jieba.lcut(data)
# num_3=len(num_2)
# print("总字符{0}个,总词语数{1}".format(num_1,num_3))
# 注意：表示随机数用(i<=n<=j)，或者[i,i+1___,j]（易错点：random.randiant(i,j+1)知识生成一个随机数不能代表i到j这个区间！！！）

'''
知识点补充：
（1）while判断:False(0/""/{}/[]/())/True(非零),
（2）只有文件提取的readlines()转列表才需要用strip("\n")的末尾分隔符，input不需要，因为input自动去除末尾的“\n”!!!
（3）一般用“”来表示空行；
（4）元组不可以被修改，其中元素类型可以是不同的。
（5）数据类型：序列型（列表、字符串、元组）/映射型（字典）
（6）jion方法：“，”.jion(ls),注意：其中ls的每一个元素都要是字符串
（7）线性结构一定能才去顺序存储，但非线性结构可能采用顺序存储。
（8）软件三要素：程序、数据、相关文档
（9）一个模块直接调用下一个模块的数目称为模块的扇出数
（10）程序设计语言分为：机器语言、汇编语言、高级语言
（11）S&T运算，包含S和T中共有的元素；
（12）“zhang”，属于字符串类型，print后不带“”！！！
（13）空集合不可以用{}来创建，应该用set()
（14）深度为h的总结点数：2**h-1;第h层的总结点数为2（h-1）
（15）第三方库：
深度学习：TensorFlow,PyTorch,Keras,MXNet
We框架：Django,Flsk,Pyramid
GUI桌面：PyQt5,wxPython
网络爬虫：requests,BeautifulSoup(HTML)
数据分析：numpy,pandas,matplotlib
（16）复利公式：a*(1+b)**t
注意：a(初始值)，b(增长率)，t(增长周期)
（17）range()是python的内置函数
（18）需求分析阶段主要的文档是：需求规则说明书
（19）数据库增删改查属于数据操作语言
（20）进程的类型包括：并行性+动态性
（21）转码函数：chr()
（22）小写变大写函数：.upper()
注意：键盘输入的字符都为字符串形式“abcdef”="a","b","c","d","f"
（23）pow(m,n):表示m的n次方
（24）jion的使用规则：“，”.jion(ls)，被连接的ls数组类型可以是列表或字符串等，但是被连接的元素必须是字符串！！！
（25）jieba函数的使用规则：jieba.lcut(data)，data必须是字符串，但是最后得出来的是列表
（26）输出结果屁股后面有“，”用：end=","，屁股后面没有用：空列表+字符串
ls=[]
for i in data:
ls.append(i)
ls=",".join(ls)
print(ls)





'''
# 小写转大写题型练习：
# data=input("请输入5个小写的字母：")
# data=data.upper()
# # print(data)
# print("{}".format(",".join(data[::-1])))

# 方案一：用str字符串拼接“/”
# import jieba
# s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
# slist=jieba.lcut(s)
# m=0
# st=""
# for i in slist:
#    if i in "，。":
#       continue
#    else:
#       st=st+i+"/"
#       m+=1
# print(st)
# print("\n中文词语数是：{}\n".format(m))

# 方案二：jion拼接
# import jieba
# s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
# slist=jieba.lcut(s)
# m=0
# ls=[]
# for i in slist:
#    if i in "，。":
#       continue
#    else:
#       ls.append(i)
#       m+=1
# sl="/".join(ls)
# print(sl)
# print("\n中文词语数是：{}\n".format(m))
# s=s.split(",")
# s_1=[]
# for i in s:
#     if i[-1]=="。":
#         i=i.replace("。","")
#         s_1.append(i)
#     else:
#         s_1.append(i)
# print(s)
# print(s_1)
# # for i in s_1:
# #     print("{0:^20}\n".format(i))

'''
import jieba
f1=open("D:/Users/H/Desktop/data2018.txt","r")
f2=open("D:/Users/H/Desktop/data2019.txt","r")
data1=f1.read()
data2=f2.read()
f1.close()
f2.close()
data1=jieba.lcut(data1)
data2=jieba.lcut(data2)
symbol="，","。","“","”","\n","、"
d = {}
for i in data1:
    if i in symbol:
        continue
    else:
        d[i]=d.get(i,0)+1
lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
lt_=lt[:10]
lst=[]
for k,v in lt:
    lst.append(f"{k}:{v}")
res=",".join(lst)
print("2018:{}".format(res))

d2 = {}
for i in data2:
    if i in symbol:
        continue
    else:
        d2[i]=d2.get(i,0)+1
lt = list(d2.items())
lt.sort(key = lambda x:x[1],reverse = True)
lt_=lt[:10]
lst_=[]
for k,v in lt:
    lst_.append(f"{k}:{v}")
res=",".join(lst_)
print("2019:{}".format(res))
'''

# while True:
#     s=input("请输入：")
#     num="0","1","2",'3',"4","5","6","7","8","9"
#     for i in s:
#         if i in num:
#             s=input("再次输入")
#             break
#     break
# print(len(s))