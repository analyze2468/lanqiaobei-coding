"""
基础柱状图构建+反转x轴和y轴
反转x轴y轴，——————为什么不直接将x轴和y轴的数据交换而要用reversal功能呢？？？
原因:因为xaxis只能容纳一类量，而yaxis可以容纳多个量
"""
'''
# 导包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar=Bar()
# 绘制x轴y轴
bar.add_xaxis(["中国","美国","英国"])   # axis：轴
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
# 绘图
bar.reversal_axis()
# bar.render("基础柱状图.html")

#-----------创建时间线----------------
#时间线定义：（1）Timeline————时间线；（2）从左向右的x轴；（3）点1对应一个图表，点2对应一个图表，随着数量的堆积就成了动态

# 图二
bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[50,30,50],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

# 图三
bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[80,70,60],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

# 构建时间线对象
timeline=Timeline({"theme":ThemeType.LIGHT})

#在时间线上添加图表
timeline.add(bar,"点一")
timeline.add(bar1,"点三")
timeline.add(bar2,"点二")

# 自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 主题设计
# 在构建时间线时，导入ThemeType模块

# 绘制图表
timeline.render("动态GDP条形图.html")
'''

#---------------------------------动态GDP条形图完整流程（列表sort排序+数据处理+绘图）-------------------------------------


# 一、知识点补充：
# （1）列表sort方法和sorted方法
# # sort方法：对原列表进行修改————————————————list.sort特点：原地排序
# my_list1=[2,1,3]
# my_list1.sort(key=函数参数,reverse=Ture降序/False升序），sort():key为全局，reverse为Ture
# print(my_list1)
# # sorted方法：排序生成新的列表——————————————sorted()特点：排序生成新的列表
# my_list2=[5,4,6]
# my_list3=sorted(my_list2)
# print(my_list2)
# print(my_list3)
# （2）readlines和readline方法的区别：
# readline:只读取文件的一行内容以字符串形式出现；eg:"content1"
# read:原封不动读取所有内容；eg:content
# readlines:按照行，读取所有内容形成一个大列表;eg:["content1","content2"…………]
# （3）空字典中创造key的操作
# dict={}
#----核心表达式------
# dict[key]=[]-------------人话：没有key就没有value，现在我要创造一个空value，key自然就出现了
# 有value一定有key
# （4）keys方法：把字典中的key全部以列表形式拿出来

#二、实操应用
# 函数（定义+return）练习：
# def choose_list(element):
#     return element[1]
# element=list(input("请输入一个列表："))
# print(element)
# print(choose_list(element))

# 嵌套列表排序方法！！！
# my_list=[["a",33],["b",55],["c",11]]
# def choose_list(element):
#     return element[1]
# my_list.sort(key=choose_list,reverse=True)
# print(my_list)

# ---------------------------------实战练习------------------------------------
# 项目名：1960-2019年全球GDP数据变化动态趋势

# 第一步：数据提取
# 格式：{year1:"[contury1,gdp1],[contury2,gdp2]…………",year2:"[contury1,gdp1],[contury2,gdp2]…………",…………}

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
f=open("D:/Users/H/Desktop/1960-2019年全球GDP变化数据.txt","r",encoding="utf-8")
f_global_data=f.readlines()  # -------------取数据------------
# print(f_global_data)
f.close()
f_global_data.pop(0)
# 数据插入字典
dict={}
for lines in f_global_data:
    line=lines.split(",")
    year=int(line[0])
    country=line[1]
    gdp=float(line[2])
    try:
        dict[year]
    except KeyError:
        dict[year]=[]  #插入key的关键步骤
        dict[year].append([country, gdp])
    else:
        dict[year].append([country,gdp])
# print(dict)
def content(list):   # 参数函数的定义
    return list[1]
timeline = Timeline({"theme":ThemeType.LIGHT})
for year in sorted(dict.keys()):
    dict[year].sort(key=content,reverse=False)
    data_country = []
    data_gdp = []
    for country_gdp in dict[year]:
        data_country.append(country_gdp[0])
        data_gdp.append(country_gdp[1]/100000000)#///////////////亿元
# print(data_country)
# print(data_gdp)
    bar=Bar()
    bar.add_xaxis(data_country)
    bar.add_yaxis("全球GDP（亿）",data_gdp,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 设置标题-------
    bar.set_global_opts(
        title_opts=TitleOpts(title="全球1960-2019年GDP变化分析", pos_top="1%"),
    )
# 时间线--------
    timeline.add(bar,year)
    timeline.add_schema(
        play_interval=1000,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=False,)

timeline.render("全球1960-2019年GDP（亿）变化分析.html")



