# '''
# 大模型基础能力：
# （python语言基础）、（数据处理与分析）、（计算机基础知识）、（大模型基础概念）
# AI的构成：数据（基础）、算法（引擎）、算力（平台）
#
# '''
# import pandas as mpl
# import numpy as np
# import matplotlib as m
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([1,2,3,4])
# y = np.array([10,20,15,25])
# plt.plot(x,y)
# plt.show()

# import pandas as pd
# import pymysql
#
# # 连接数据库
# # 放开列的显示限制，全部列打印
# pd.set_option('display.max_columns', None)
# # 放开单行宽度
# pd.set_option('display.width', None)
#
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='2006',
#     database='north_wind',
#     charset='utf8mb4'
# )
#
# # ===== 这里写你DBeaver练习的SQL语句 =====
# sql = """
# select * from employees;
# """
#
# # pandas读取sql结果，变成表格
# df = pd.read_sql(sql, conn)

# print(df)
#
# # 关闭连接
# conn.close()







# import pandas as pd
# import pymysql
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 显示全部列
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
#
# # 连接数据库
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='2006',
#     database='north_wind',
#     charset='utf8mb4'
# )
#
# # SQL
# sql = """
# select e.employee_id, e.last_name, e.reports_to
# from employees e;
# """
# df = pd.read_sql(sql, conn)
# conn.close()

# seaborn画图
# plt.figure(figsize=(8,4))
# sns.countplot(data=df, x="reports_to")
# plt.title("每个领导下属人数")
# plt.show()

# numpy 的简介
'''
（1）高性能科学计算的数据分析的基础包
（2）ndarry，多维数组，具有矢量运算能力，快速节省空间
（3）矩阵运算，无需循环，可完成了类似matlab的矢量运算
'''
# # （1）创建numpy的ndarray对象
import numpy as np
# data=np.arange(15).reshape(3,5)
# print(data)
# # （2）演示numpy的常用属性
# print(f'numpy的轴：{data.ndim}')    # 几层数据
# print(f'numpy的维度：{data.shape}') # 几行几列
# print(f'numpy的元素类型：{data.dtype}')
# print(f'numpy的元素个数：{data.size}')
# print(f'numpy的元素占用字节数：{data.itemsize}')

# --------------------------------------------------
# （1）array()函数创建python列表对象
# my_list=[1,2,3,4,5]
# print(my_list)
# # （2）把python列表转换为 ndarray对象
# data1=np.array([1,2,3,4,5])
# print(data1)
# print(type(data1))
# # ----------------arange()函数，创建ndarray对象-------------------------
# # (1)创建ndarray对象
# data2=np.arange(0,10,2,dtype=np.int32)
# # (2)打印ndarray对象
# print(data2)
# print(type(data2))
# print(f"元素的类型：{data2.dtype}")
# # -----------------------随机数生成ndarray对象---------------------
# # (1)random.rand() 生成 0.0~1.0之间，包左不包右的随机小数矩阵
data3=np.random.rand(3,5)
print(data3)
print(type(data3))
# # (2)random.randint(起始值，结束值，size(行，列))包左不包右的随机整数矩阵
data4=np.random.randint(3,6,size=(2,5),dtype=np.int32)
print(data4)
# print(type(data4))
# # (3)random.uniform(起始值，结束值，size(行，列)) 生成指定范围，包左不包右的随机小数矩阵
# data5=np.random.uniform(2,6,size=(2,5))
# print(data5)
# print(type(data5))
# ----------------numpy的类型转换-----------------------
# （1）创建ndarray对象
# data6=np.arange(0,10,2,dtype=np.int32)
# print(data6)
# print(data6.dtype)
# # （2）把上述的data6 narray对象的元素 从int32 类型转为 float32类型
# data7=data6.astype(np.float32)
# print(data7)
# print(data7.dtype)

# ----------------等比/等差数列----------------------
# #（1）创建等比数列：参1：起始值（充当10的指数），参2：结束值（充当10的指数），参数3：元素个数
# data8=np.logspace(0,3,4)
# print(data8)
# print(data8.dtype)
# # （2）创建等比数列：参1：起始值（充当2的指数），参2：结束值（充当2的指数），参3：元素个数，参4：修改底数/基数为2，参5：修改数据类型为int32
# data8=np.logspace(0,3,4,base=2,dtype=np.int32)
# print(data8)
# print(data8.dtype)
# # （3）创建等差数列：参1：起始值，参2：结束值，参3：元素个数，参4：是否包含结束值，参5：修改数据类型为int32
# data9=np.linspace(1,10,4,endpoint=False,dtype=np.int32)
# print(data9)
# print(data9.dtype)

#---------------------numpy基本函数--------------------
# （1）创建标准的正态分布的序列
# data10=np.random.randn(3,5)
# print(data10)
# # （2）测试基本函数
# print(np.ceil(data10))   # 天花板————向上取整，比他大的，取最小的那个整数
# print(np.floor(data10))  # 地板数————向下取整
# print(np.rint(data10))   # 四舍五入取整
# print(np.abs(data10))    # 绝对值
#
# print(np.multiply(data10,data10)) # 矩阵乘法（行列数一致）
# print(data10*data10)              # 效果一致
#
# print(np.divide(data10,data10))   # 矩阵出发（行列一致）
# print(np.where(data10>0,1,-1))   # 类似python中的if函数

#---------------------numpy统计函数函数--------------------
# （1）定义ndarray对象（数组对象）
# data1=np.arange(12).reshape(3,4)
# print(data1)
# # （2）验证累加
# print(np.cumsum(data1))  # [ 0  1  3  6 10 15 21 28 36 45 55 66]
# # （3）验证求和
# print(np.sum(data1))     # 66
# print(np.sum(data1, axis=1))  # 1——行
# print(np.sum(data1, axis=0))  # 0——列

#---------------------numpy去重和排序函数--------------------
# # （1）定义数组
# data1=np.array([[1,2,1],[2,3,4]])  # 2行3列
# print(data1)
# # （2）对上述元素去重
# data2=np.unique(data1)  # 去重，返回新副本（原数组不变）
# print(f'data1: {data1}')
# print(f'data2: {data2}')
# （3）定义数组
# data3=np.array([11,33,22,66,55])
# print(data3)
# # （4）通过np.sort()方式排序——返回新副本
# data4=np.sort(data3)
# print(f'data3: {data3}')
# print(f'data4: {data4}')
# # （5）通过数组对象sort()————直接修改原数组
# print(f'排序前data3: {data3}')
# data3.sort()
# print(f'排序后data3: {data3}')

#---------------------numpy 基本运算--------------------
# # （1）定义数组
# data1=np.array([10,20,30,40])
# data2=np.arange(4)
# # （2）打印数组
# print(f'data1={data1}')
# print(f'data2={data2}')
# # （3）减法运算
# print(data1-data2)
# print(data1+data2)

# # 乘法运算数组一（矩阵A和B行列完全相同）
# data5=np.array([[1,2],[3,4]])
# data6=np.array([[3,4],[5,6]])
# print(data5*data6)              # 符号法:对应位置相乘，不是矩阵乘法！！！
# print(np.multiply(data5,data6)) # 函数法：效果同上
# # 乘法运算数组二（矩阵行列不同,但A列等于B行）
# data3=np.array([[10,20,30,40],[50,60,70,80]])
# data4=np.array([[1,2],[3,4],[4,5],[5,6]])
# print(data3@data4)
# print(np.dot(data3,data4))
