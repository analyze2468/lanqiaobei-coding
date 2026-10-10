#-------------------------数据可视化的折线图可视化-----------------------------------
'''
一、折线图——————新冠累确诊人数与时间的走势图
二、全国疫情地图的可视化——————地图
三、动态GDP柱状图
四、数据来源：网络全国公开数据；使用技术：Echarts————————pyecharts（第三方包）
'''
                         #------------------------案例开发---------------------

# 第一节：--------------------------json数据格式-----------------------------------
'''
（1）定义：轻量级数据交互格式+特定格式的字符串     # 交互定义：使两台不同的电脑/语言变的互相看的懂彼此的内容
（2）主要功能:在各个编程语言中流通的数据格式
（3）
例如1：负责不同地区语言的通用语言————普通话
例如2：python与c++数据交互可以使用json作为中转，否则c++看不懂
（4）json是python的字典或列表（特定格式的字符串 ）
'''
print("-----------------------------------------------------")
'''
演示josn和python字典的相互转化
my_list=list(str)    #内容转化的相似理解
----------------------------------------
'''
# 列表/字典转化为json
"""import json
data=[{"name":"黄老师","age":20},{"name":"刘老师","age":21},{"name":"张老师","age":18}]
json_str=json.dumps(data,ensure_ascii=False)  # 准备列表的字典，将其转化为json
print(type(json_str))      # ensure_ascii=False——————把中文编码转化为中文格式
print(json_str)
print("----------------------------------")
# json字符串转化为python类型
s='[{"name": "黄老师", "age": 20}, {"name": "刘老师", "age": 21}, {"name": "张老师", "age": 18}]'
l=json.loads(s)
print(type(l))
print(l)

# 案例小练习

print("----------------------------------")
json_str=json.dumps({"name":"周杰伦","age":20},ensure_ascii=False)
# dumps：把python的列表/字典转化为json的字符串格式
print(type(json_str))
print(json_str)
d=json.loads('{"name": "周杰伦", "age": 20}')
# loads：把json的字符串格式转化为python的列表/字典
print(type(d))
print(d)
print("----------------------------------")
json_str=json.dumps(["周杰伦","老六",18],ensure_ascii=False)
print(type(json_str))
print(json_str)
l=json.loads('["周杰伦", "老六", 18]')
print(type(l))
print(l)
"""
# 第二节：--------------------------pyecharts-----------------------------------
#网站：pyecharts.org
#网站：gallery.pyecharts.org

              # ----------------基础折线图-------------------
'''from pyecharts.charts import Line #注意大小写！！！
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
line=Line()      #  坐标轴的生成
line.add_xaxis(["中国","美国","日本"])
line.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(is_show=False),)
#set_global方法----------------- 注意：control+p可以看到指示
#（全局配置选项）：配置图表标题、配置图例、配置鼠标移动效果、配置工具栏、配置工具箱
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_top="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
# 通过render方法将代码变成图像！！！
line.render()

# 字符串知识补充：通过replace函数处理开头（批量替换），利用序列提取：data[:5:1]
'''



#----------------------------------美日印三国日期随人数变化趋势这先统计图---------------------------
"""
用到的工具：
懒人工具：ab173（将json格式化），txt文件，pyecharts模块，豆包
"""


#    ----------------------代码演示------------------------

import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 打开美日印初始文件
us_f=open("D:/Users/H/Desktop/美国.txt","r",encoding="utf-8")
jp_f=open("D:/Users/H/Desktop/日本.txt","r",encoding="utf-8")
in_f=open("D:/Users/H/Desktop/印度.txt","r",encoding="utf-8")
# 读取文件进入python
us_f_data=us_f.read()
jp_f_data=jp_f.read()
in_f_data=in_f.read()
us_f.close()
jp_f.close()
in_f.close()
# 字符串方法清洗乱码文件
us_f_data=us_f_data.replace("/* 这是文件开头的乱码内容：123456abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+ */","")
jp_f_data=jp_f_data.replace("-- 开头乱码：random_text_123_!@#$%_japan_health_report --","")
in_f_data=in_f_data.replace("/* garbage text at start: india_health_data_xyz_1234567890_!@#$%^&*() */","")
# 序列清洗方法：us_f_data[:-2]
# print(us_f_data)
us_f_data=json.loads(us_f_data)
jp_f_data=json.loads(jp_f_data)
in_f_data=json.loads(in_f_data)
# josn格式与python格式的交互（字符串转化为字典）
#---------------类型测似-------------------------
# print(type(us_f_data))
# print(us_f_data)
# print(type(jp_f_data))
# print(jp_f_data)
# print(type(in_f_data))
# print(in_f_data)
print("------------------------------------")
# pyecharts函数的调用
line=Line()
# ----------------横坐标数据---------------------

# 遍历方法一：
us_x_data=[i["date"]for i in us_f_data["detailed_data"]] # 列表内遍历：表达式（脑子里的列表长什么样子）+for i in 可迭代变量
jp_x_data=[i["date"]for i in jp_f_data["detailed_data"]]
# 遍历方法二：
#jp_x_data=[]
#for i in jp_f_data["detailed_data"]:
#    cotent=i["date"]
#   jp_x_data.append(cotent)    # append:把内容从前追加到后，insert：从某个索引值插入
in_x_data=[i["date"]for i in in_f_data["detailed_data"]]

# ----------------纵坐标数据---------------------
# print(us_x_data)
us_y_data=[i["diagnosis_count"]for i in us_f_data["detailed_data"]]
jp_y_data=[i["diagnosis_count"]for i in jp_f_data["detailed_data"]]
in_y_data=[i["diagnosis_count"]for i in in_f_data["detailed_data"]]
# print(us_y_data)

#          ——————-——————————折线图处理操作————————————————————————
# 横坐标处理只需要一类（因为都是日期）
line.add_xaxis(us_x_data)
line.add_yaxis("美国",us_y_data,label_opts=LabelOpts(is_show=False),color="#0000FF")
line.add_yaxis("日本",jp_y_data,label_opts=LabelOpts(is_show=False),color="#00A800")
line.add_yaxis("印度",in_y_data,label_opts=LabelOpts(is_show=False),color="#000000")
#options全局优化
line.set_global_opts(
    title_opts=TitleOpts(title="美日印三国病诊情况",pos_left="center",pos_top="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
)
# 转html
line.render("美日印三国的病诊情况.html")







