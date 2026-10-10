"""
基础地图演示

"""
#      --------------------------基础地图的应用------------------------
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
#
# map=Map()
# # 数据准备---------------------注意：嵌套可以用元组/和列表，区别：元组不可修改更安全，列表可修改更灵活
# data=[
#     ("北京市",99),
#     ("上海市",199),
#     ("湖南省",299),
#     ("台湾省",8),
#     ("江西省",399)
# ]
# # 数据添加
# map.add("地图",data,"china")
# # 绘图
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,              # 是否显示
#         is_piecewise=True,    # 是否分类显示
#         pieces=[
#             {"min":1,"max":9,"label":"1~9人","color":"#CCFFFF"},
#             {"min":10,"max":99,"label":"10~99人","color":"#FF6666"},
#             {"min":100,"max":500,"label":"100~500人","color":"#990033"},
#         ]
#
#     )
# )
#
# map.render("中国地图.html")

# ------------------国内疫情地图-----------------------


#第一步：数据处理（json格式转为python字典）
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

f=open("D:/Users/H/Desktop/全国疫情数据可视化.txt","r",encoding="utf-8")
f_data=f.read()
# print(f_data)
# json数据格式向python的转化
f_data=json.loads(f_data)
# print(type(f_data))
f.close()  # 文件关闭！！！
# ----------数据提取------------

# 易错点！！！data_name1=data_name["name"]

# -----------------“data_name1 = data_name["name"]”——典型错误bug捕获判断-------------------
data_name=f_data["country"]["province_list"]
try:
    data_name1 = data_name["name"]
except Exception as e:
    print("data_name1 = data_name[""],出现了异常bug")
    print(f"异常的原因是：{e}")
else:
    data_name1 = data_name["name"]
    print(data_name1)
finally:
    print("判断结束！！")
print("----------------正确方法一------------------")
# data=[]
# data_name=f_data["country"]["province_list"]
# # print(data_name)
# for i in data_name:
#     data_name1=i["name"]
#     data_confirm=i["total"]["confirm"]
#     data.append((data_name1,data_confirm))
# print(data)

print("----------------正确方法二------------------")
data=[(i["name"],i["total"]["confirm"])for i in f_data["country"]["province_list"]]
print(data)

# 第二步:地图处理（利用pyecharts模块调用其功能）
map=Map()
map.add("疫情分布地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#8B0000"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#CD2626"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#EE6363"},
            {"min": 5000, "max": 9999, "lable": "5000~9999人", "color": "#FFA07A"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#FFE411"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
map.render("全国疫情数据可视化.html")








