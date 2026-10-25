'''
擅长处理结构化数据（excel/mysql）
pandas处理数据的优势：
（1）底层是numpy，运算速度快
（2）有专门处理缺失数据的API
（3）强大的灵活的分组、聚合、抓换功能
pandas的核心对象：series和dataframe对象
columns:结构数据的列
自然索引：0-1-2-3-4…………
Series:一整行/一整列对象（通通用列表是，没有行的概念！！！）
DataFrame:整个表数据
'''
import pandas as pd
import numpy as np
import pymysql as sql
from sqlalchemy import create_engine
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']   # 设置黑体，支持中文
plt.rcParams['axes.unicode_minus'] = False    # 防止负号变成方框
#---------------------创建series对象--------------------------
# # （1）创建series对象，采用：默认自增索引
# data1=pd.Series([1,2,3,4])
# print(data1)
# # （2）创建series对象，采用：自定义自增
# data2=pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(data2)
# # （3）使用元组创建Series对象
# data3=pd.Series((1,2,3,4))
# print(data3)
# # （4）使用字典创建Series对象，自定义自增
# data4=pd.Series({"A":1,'B':2,'C':3,'D':4})
# print(data4)
# # （5）使用numpy————ndarray对象创建Series
# data5=pd.Series(np.array([1,2,3,4]))
# print(data5)

#---------------------series对象属性--------------------------
# # （1）创建Series对象，索引为：A-F，值为：0-5
# data1=pd.Series([1,2,4],index=['a','b','c'])
# print(data1)
# # （2）加入for的遍历
# data2=pd.Series([i for i in range(5)],index=[i for i in "abcde"])
# print(data2)
# # （3）获取索引index和值values
# print(data2.index)
# print(data2.values)
# # （4）根据索引获得元素：Series[index]=value
# print(data2["b"])

#---------------------创建DataFarme对象--------------------------
'''DataFrame是一个类似于二维数或表格数的对象，既有行索引，又有列索引
（1）行索引：不同行   ，index ，0轴，axis=0;
（2）列索引：不同列   ，column，1轴，axis=1;
pd.DataFrame(data=,index=,column=,dtype=,copy=)  # 参数形式
'''
# # （1）通过字典+列表实现（列数据插入）
# data1={
#     'name':['黄老师','李老师',"张老师","王老师"],
#     'gender':['男','女','女','男'],
#     'age':[23,55,32,43]
# }
# info=pd.DataFrame(data1)
# print(info)
# # （2）通过列表+元组/列表（行数据插入）
# data2=[
#     ['张三','男','23'],
#     ['李四','女','22'],
#     ['黄五','男','24']
# ]
# info1=pd.DataFrame(data2,columns=['姓名','性别','年龄'])
# print(info1)
# # （3）通过ndarray对象，封装表格数据
# data3=np.arange(12).reshape(3,4)
# info2=pd.DataFrame(data3,columns=['a','b','c','d'])
# print(info2)

#---------------------学生信息处理DataFrame案例--------------------------
# （1）生成10名学生，5门功课的成绩，成绩范围：40~100
# data4=np.random.randint(40,101,size=(10,5))
# # print(data4)
# info3=pd.DataFrame(data4)
# # （2）索引名插入
# # index_name=['同学0','同学1','同学2','同学3','同学4','同学5','同学6','同学7','同学8','同学9']   # 表示方法一
# index_name=[f"同学{i}" for i in range(10)]   # 方式二
# # print(index_name)
# # （3）列名插入
# columns_name=['语文','数学','英语','物理','化学']
# # （4）修改DataFrame中行和列名（全修改）
# info3.index=index_name
# info3.columns=columns_name
# print(info3)
# # # 4.1：利用参数修改（全修改）
# info4=pd.DataFrame(data4,index=index_name,columns=columns_name)
# print(info4)
# # 4.2利用rename函数修改（单个修改）
# info5=pd.DataFrame(data4)
# info5.rename(index={0:'黄老师'},columns={4:'体育'},inplace=True)
# print(info5)

# #---------------------DataFrame的基本属性--------------------------
# # （1）shape维度，即：行列数
# print(info3.shape)
# # （2）index:索引列
# print(info3.index)
# # （3）columns:列名
# print(info3.columns)
# # （4）data：数据
# print(info3.values)
# # （5）行列转换
# print(info3.T)

# #---------------------DataFrame的基本函数介绍--------------------------
# #（1）head(n)：查看前n行数据，head()：查看前五行数据
# print(info3.head())
# #（2）tail(n):查看后n行数据，head()：查看后五行数据
# print(info3.tail())
# #（3）info()，查看数据结构的详细信息
# print(info3.info())
# #（4）describe(),查看数据对象的描述性统计信息
# print(info3.describe())
# #（5）reset_index()，重置索引列
# print(info3.reset_index(drop=True))  # drop=True作用：删除原索引

#---------------------pandas的数据类型--------------------------
'''
pandas中的数据类型几乎和python中是一致，只有几个不同
eg:python :str————pandas:object，python：None————pandas:nan/NAN
# 例外：pandas还支持category分类类型，针对于分类数据操作更快，更节省内存
'''
# #（1）创建DataFrame对象
# data1=pd.DataFrame({
#     "name":['小东',np.nan,'小黄'],            # 设置空字符的方式“np.nan”
#     'sex':['男','女','保密'],
#     'age':[12,33,np.nan]
# })
# # print(data1)
# # print(data1.info())
# # (2) 演示日期类型dataframe
# data2=pd.DataFrame(['2025-03-29','2026-04-05','2026-10-19'],dtype='datetime64[ns]')
# print(data2)
# print(data2.dtypes)
# #（3）日期差
# start_time=pd.to_datetime('2006-10-17')
# end_time=pd.to_datetime('2026-10-18')
# print(end_time-start_time)
# print(type(start_time))
# # （4）category类型
# data3=pd.DataFrame(['2025-03-29','2026-04-05','2026-10-19'],dtype='category')
# print(data3.dtypes)
# print(type(data3))

#---------------------pandas基本数据操作--------------------------
# （1）加载数据
# data1=pd.read_csv('D:/Users/H/Desktop/stock_data.csv')
# print(data1)
# data2=data1.reset_index(drop=True)
# data2=data1.set_index('date')   # 设置date为索引！！！
# data2.index.name=None           # 删除索引名
# print(data2)
# （2）移除不需要的字段
# data2.drop(columns=['ma5','ma10','ma20','v_ma5','v_ma10','v_ma20'],axis='columns',inplace=True)
# print(data2)
# print(data2.info())
# print(data2.describe())
# （3）索引操作
# 操作一：根据行列索引
# print(data2['open']['2018-02-23'])   # 写法解读：先搜索引列变成Series对象，再进行行索引
# print(data2['open'])               # series对象
# 操作二：错误示范（先行后列）
# print(data2['2018-02-23']['open'])
# 操作三：结合loc或者iloc使用索引
# 格式：data2.loc[行索引，列名]，格式：data2.iloc[行号，列索引]
#---loc模式------
# data=data2.loc['2018-02-23','high']
# print(data)                                              # 获取一条数据
# data=data2.loc['2018-02-23':'2018-02-14',['open','high']]  # 获取多条数据
# print(data)
#---iloc模式------
# data=data2.iloc[0:3,0:4]
# print(data)

#---------------------pandas排序操作--------------------------
# 赋值操作一：
# data2.low=22
# print(data2)
# 赋值操作二：
# data2["low"]=22
# print(data2)
# （1）查看原数据
# print(data2)
# （2）基于open价格做降序排列
# data2.sort_values(by='open',ascending=False,inplace=True)  # 升序用True
# print(data2)
# （3）基于open降序排列，相同的通过high升序排列
# data2.sort_values(by=['open','high'],ascending=[False,False],inplace=True)
# print(data2)
#（4）按照索引降序排列
# data2.sort_index(ascending=True,inplace=True)
# print(data2)
#（5）Series对象也有sort_index()和sort_values()
# data=data2.open.sort_values(ascending=False)
# print(data)
# data=data2['open'].sort_index(ascending=False)
# print(data)

# 补充细节：利用inplace=True处理DataFrame数据（动原数据）或者利用赋值处理dataframe数据但（不动原数据）
# data=pd.DataFrame({
#     "a":[1,2,3],
#     "b":[4,5,6],
#     "c":[7,8,9]
# })
# index=['d','e','f']
# data.index=index
# print(data)
# ------方式一：赋值，不使用inplace,不改变原数据-------
# data1=data.sort_values("a",ascending=False)
# print(data1)
# print(data)
# ------方式二:不赋值，使用inplace,改变原数据-------
# data.sort_values("a",ascending=False,inplace=True)
# print(data)

#------------------------pandas的基本运算--------------------------
#（1）查看原数据
# print(data2)
#（2）针对close列进行加值
# data2=data2['close']+2
# data2=data2['close'].add(2)
# print(data2)
#（3）针对close列进行减值
# data2=data2['close']-2
# data2=data2['close'].sub(2)
# print(data2)
#（4）筛选open中大于23小于24的元素（query方法）
# data2=data2.query('open>23 & open<24')
# print(data2)
# （5）固定值的筛选（query或isin）
# data2=data2.query('open in [22.45,23.71]')      # query方法
# data2=data2[data2['open'].isin([22.45,23.71])]  # isin方法
# print(data2)

#------------------------pandas的统计函数--------------------------
# 拿数据
# print(data2)
# 统计函数：count(),mean(),min(),max(),std()
# data=data2.describe()
# print(data)
# print(data2.sum())
# print('-----------------')
# print(data2.high.sum())
# print('-----------------')
# print(data2.mean())
# print('-----------------')
# print(data2.median())
# print('-----------------')
# print(data2.cumsum())

#------------------------pandas的apply函数（自定义运算）--------------------------
# 需求：同时获取多列的最大值和最小值的差值，例如：open列和close列
# # 单个获取示范：
# print(data2.open.max()-data2.open.min())
# print(data2.close.max()-data2.close.min())
# 获取到open和close列
# print(data2[['open','close']])
# print(data2.loc[:,['open','close']])   # 注意：loc和iloc都用中括号“【】”！！！
# print(data2.iloc[:,[0,2]])
# 合并版，通过lambda函数实现
# data=data2.loc[:,['open','close']].apply(lambda col:col.max()-col.min())  # apply中加入自定义匿名函数，融合了多列和求极差需求！！！
# print(data)

#------------------------pandas的文件读写操作--------------------------
# （1）读取csv文件获取数据
# data1=pd.read_csv('D:/Users/H/Desktop/csv写入文件夹/stock_data.csv',sep=',',usecols=['date','open','high','low','close'])
# data2=data1.set_index('date')   # 设置date为索引！！！
# data2.index.name=None           # 删除索引名
# print(data2)
# （2）把读取的数据，写入文件中
# data2.iloc[:10,:].to_csv('D:/Users/H/Desktop/mycsv1.csv',sep=',',index=False)
# （3）特殊文件csv文件————tsv文件，区别：csv(',')，tsv('\t')
# data2.iloc[:5,:].to_csv('D:/Users/H/Desktop/csv写入文件夹/mycsv2.tsv',sep='\t',index=False)
# （4）读取tsv文件
# data=pd.read_csv('D:/Users/H/Desktop/csv写入文件夹/mycsv2.tsv',sep='\t')
# print(data)

#----------------------------------------------------------------------------------
# 需求：把数据写入到mysql数据表中
# （1）准备数据
# data=data2.iloc[:5,:]
# print(data)
# （2）导包
# from sqlalchemy import create_engine
# # （3）创建引擎对象
# 格式：数据库+模块名：//数据库用户名：密码@主机名/数据库？编码方式
# engine=create_engine('mysql+pymysql://root:2006@localhost:3306/boss?charset=utf8')
# # （4）具体的往数据库写数据的动作
# 格式：参数1：数据表名，参数2：引擎对象，参数三：是否把索引写入数据库，参数4：如果存在则如何处理（append/replace）
# data.to_sql('python_file',engine,if_exists='append')
#（5）从sql中取数据
# 参数1：数据表名，参数2:引擎对象
# data1=pd.read_sql('python_file',engine) # 读取全表
# data2=pd.read_sql("select * from python_file limit 0,3",engine)
# print(data1)
# print(data2)
# 方式一：删除index列
# data2=data2.drop('index',axis='columns')
# print(data2)
# 方式二：index列做索引,把index名字删掉
# data2=data2.set_index('index')
# data2.index.name=None
# print(data2)

# ------------------读写文件操作总结--------------
# 读入:需要（pd+read）
# pd.read_csv("地址",usecols"列筛选")
# 写出:需要（data+to+index）
# data.to_csv('地址',index=False)

#--------------------------------------项目实践----------------------------------------
# （1）pandas数据准备
# info=({
#     'student_id':[101,102,103,101,102,103],
#     'name':['张三','李四','王五','张三','李四','王五'],
#     'subject':['数学','数学','数学','英语','英语','英语'],
#     'score':[88,76,92,81,85,79]
# })
# data=pd.DataFrame(info)
# print(data)
# （2）数据写入mysql数据库
# engine=create_engine('mysql+pymysql://root:2006@localhost:3306/boss?charset=utf8')
# data.to_sql('python_file1',engine,index=False,if_exists='append')          # 注意:写入操作最好仅执行一遍！！！
# # （3）从MySQL读取整张表，打印全部数据
# data2=pd.read_sql('select * from python_file1',engine)
# # data2.drop('index',axis='columns',inplace=True)                            # 选择性删除索引列！！！
# print(data2)
# # （4）利用pandas进行排序
# data3=data2.query('score>80')
# print(data3)
#  （5）利用sql进行排序
# data2=pd.read_sql('select * from python_file1 where score>80',engine)
# print(data2)

#------------------------pandas的增删改查操作--------------------------
# 一：增！
# （1）准备数据
# data=pd.read_excel('D:/Users/H/Desktop/Agent自动项目库/新能源汽车市场_月度销量数据 (2).xlsx',engine='openpyxl')
# data.set_index('月份',inplace=True)
# data.index.name=None
# print(data)
# # （2）增单列：
# data['a']=29
# data['b']=[12,33,21,34,32,21]
# # print(data)
# # （2）增多列————函数：
# # 写法2: 通过 assign() 函数 → 新增n列
# data=data.assign(
#     c1 = 23,
#     c2 = ['cxk', 'lyf', 'wyf', 'wyb', '水冷哥','胡歌']
# )
# print(data)

# 二：删和去重！
#（1）数据准备：
# print(data)
#（2）删除行
# data1=data.drop(index=['2026-04','2026-06'])
# print(data1)
#（3）删除列
# data2=data.drop(columns='新能源汽车销量(万辆)')
# print(data2)

#（4）去重————DataFrame和Series
# data=pd.concat([data,data])   # 利用concat函数表格联合产生重复数
# print(data)
# data=data.drop_duplicates()   # DataFrame去重：再drop的基础上进行duplicates去重操作
# print(data)
# data=data['全国乘用车销量(万辆)'].drop_duplicates()
# print(data)

# 三：改
#（1）准备数据
# print(data)
#（2）一列多改：
# 与增同理
#（3）单个改：采用replace替换
# 公式：data.列=data.列.replace({a:b})  解释：再data的列columns中把数据a换成b！！！
# data['新能源汽车销量(万辆)']=data['新能源汽车销量(万辆)'].replace({134.4:134})
# print(data)

# 四：查
#（1）根据行索引获取数据
# data=data[:3]
# print(data)
#（2）基础函数
# data.head()
# data.tail()
# data=data['新能源汽车销量(万辆)']
#（3）query函数，结合条件获取
# data=data.query('`新能源汽车销量(万辆)` in [134.4,164.3]')
# # print(data)
# data=data.query('`新能源汽车销量(万辆)`<160')
# print(data)
# ---------注意：query可以用来筛选查看数据，但是特殊columns则用反引号包裹！！！----------
#（4）排序函数复习：
# data=data.sort_index(ascending=False)
# print(data)
# data=data.sort_values(by='新能源汽车销量(万辆)',ascending=False)
# print(data)

#------------------------pandas的进阶语法————数据合并（concata和merge）-------------------------
#（1）数据准备
# info=({
#     'student_id':[101,102,103,101,102,103],
#     'name':['张三','李四','王五','张三','李四','王五'],
#     'subject':['数学','数学','数学','英语','英语','英语'],
#     'score':[88,76,92,81,85,79]
# })
# data=pd.DataFrame(info)
# 顺便写入excel
# data.to_excel('D:/Users/H/Desktop/Agent自动项目库/缺失值项目.xlsx',index=False,engine='openpyxl')
# data1=data.head(3)  # data1=data[:3]
# data2=data.tail(3)  # data2=data[3:6]
# print(data)
#（2）通过concat()合并数据，公式：pd.concat([数据1，数据2，axis="columns/index"])
# 细节：列合并,默认参考“列名”
# data3=pd.concat([data1,data2],axis='columns')
# print(data3)
# 细节：行合并，默认参考“行索引”
# data4=pd.concat([data1,data2],axis='index')
# print(data4)
# 总结：concat默认是满外连接“并集”（左连接+右连接），优势：可拼接列也可拼接行，但仅限全外连接！！！
print('--------------------------------------------------')
#（3）通过merge()进行合并连接，公式：pd.merge(数据1,数据2,how=inner/left/right,on='内连接方式')
# print(data1)
# data2.student_id=[101,101,104]
# print(data2)
# 演示：merge()函数的默认合并方式
# data5=pd.merge(data1,data2,how='inner',on='student_id')
# print(data5)
# 演示：merge()函数内连接，指定合并字段
# data6=pd.merge(data1,data2,how='inner',on=['student_id','name'])
# print(data6)
# 演示：merge()函数外连接，指定合并字段
# data7=pd.merge(data1,data2,how='outer',on=['student_id','name'])
# print(data7)
# 左连接+有链接=外连接（并集）:先拼接共有的，再分别写自己的
# data8=pd.merge(data1,data2,how='left',on=['student_id','name'])
# print(data8)
# 总结：merge默认是内连接“交集”，优势：可内连接，但仅限行拼接！！！

#------------------------pandas的进阶语法————缺失值处理-------------------------
'''   知识点大纲：
- 应用isnull判断是否有缺失数据NaN
- 应用fillna实现缺失值的填充  --------增
- 应用dropna实现缺失值的删除  --------删
- 应用replace实现数据的替换   --------改
'''
# （1）读取数据
# info=pd.read_excel('D:/Users/H/Desktop/Agent自动项目库/缺失值项目.xlsx',engine='openpyxl')
# print(info)
# （2）查看数据的介绍
# print(info.columns)
# print(info.info())
# print(info.describe())
# （3）产生缺失值（改）
# info.name=info.name.replace({'王五':np.nan})  # 空值的数据类型是numpy
# print(info)
# （4）删除缺失值（删）
# info1=info.dropna()   # 删除缺失值所在的行
# print(info1)
# print(info)    # 对比
# （5）缺失值的查看（判读是否有缺失值）
# 1、判断是否有缺失值（方式一:输出结果是notnull对score列每个数据的判断）
# info2=pd.notnull(info.score)
# print(info2)
# 2、判断是否有缺失值（方式二：输出结果是notnull对score这一列的整体判断）
# info3=np.all(pd.notnull(info.score))
# print(info3)
# （6）填充缺失值（增）
# 1、填充固定值‘2’
# info.name=info.name.fillna(2)
# print(info)
# 2、填充score列的平均值
# info.name=info.name.fillna(info.score.mean())
# print(info)

print('-----------------------综合练习题---------------------------')
# 题目：for循环的方式，使用每列的平均值来填充给各列的缺失值
# （1）准备数据
# print(info)
# （2）产生缺失值
# info.score=info.score.replace({92:np.nan,85:np.nan})
# print(info)
# （4）获得每个列名
# for col_name in info.columns:
# # 5）获得判断的某列是否有缺失值
# # movie_df[col_name]: 根据列名, 找到 df中的某个列 → Series对象.
# # pd.notnull(某列数据): 判断该列的每个值是否为非缺失值, True → 不为空, False → 为空(缺失值)
# # np.all([True, False...]): 里边的值全部为True → 结果为True, 只要有一个为False → 结果为False.
#     if np.all(pd.notnull(info[col_name])) == False:
#         # print(col_name)  # 打印列名
#         # print(info[col_name].mean())# 5.4 打印这两列的平均值.
#         info[col_name]=info[col_name].fillna(info[col_name].mean())# 5.5 用该列的平均值来填充该列的缺失值.
# print(info)

#------------------------pandas的分组聚合操作-----------------------------
'''
分组格式：data.groupby(['分组字段1','分组字段2'])
聚合操作（agg——————Aggregate）
分组聚合：data.groupby(['分组字段1','分组字段2']).agg({"分组列","分组字段"})
'''

# （1）数据准备：
# info=pd.read_csv('D:/Users/H/Desktop/Agent自动项目库/sales_fact.csv')
# info=info.head(100)
# print(info)
# （2）场景一：按照单列分组
# info.groupby('city')
# print(info.groupby('city').get_group('上海'))    # 查看上海组的数据
# （3）场景二：按照多列分组
# info.groupby(['city','channel'])
# print(info.groupby(['city','channel']).get_group(('上海','门店购买')))   # 查看多列分组信息时get_group内要元组
# （3）场景三：分组+聚合
# info1=info.groupby(['city','channel']).agg({'revenue':'sum'})   # 返回dataframe对象！！！
# info1=info.groupby(['city','channel',as_index=False]).agg({'revenue':'sum'})   # 分组列从index到columns的写法
# print(info.groupby(['city','channel'])[['revenue']].sum())      # 同上!!!
# print(info1)
# info2=info.groupby(['city','channel']).revenue.sum()            # 返回series对象！！！
# print(info.groupby(['city','channel'])['revenue'].sum())        # 同上!!!
# print(info2)

#------------------------pandas的分组过滤操作：filter-----------------------------
#（1）数据准备
# print(info)
#（2）需求：根据城市分组，计算每个城市的销售平均值>30000的值
# info3=info.groupby(['city']).agg({'revenue':'mean'})   # 回顾！
# print(info3)
#（3）完成需求
# info4=info.groupby('city').filter(lambda x: x.revenue.mean()>30000)  # 通过filter分组过滤
# print(info4)        # 注意:最后拿出来的结果是每个组符合条件的所有列,不只是revenue列

#------------------------pandas的数据透视操作：pivot_table-----------------------------
'''
数据透视：列/行/值的表现，高效表格，聚合的另一种表现
写法：info.pivot_table(index='',columns='',values='revenue',aggfunc='sum')
'''
# 需求：根据城市，销售渠道分组，计算销售金额的总和
# info5=info.groupby(['city','channel'],as_index=False).agg({'revenue':'sum'})   # 分组聚合写法
# # print(info5)
# info6=info.pivot_table(index='city',columns='channel',values='revenue',aggfunc='sum')
# # print(info6)
# 数据透视表操作总结：先分组聚合看结构，（一列做表的index,一列做columns，一列做values，一列做功能）
#----------------------------------------------------------------------------------------------------------------

'''
知识点补充：
（1）dataframe数据细节：data['列名']：series对象，data[data.['列名']>100]（布尔型）：datafrme对象
（2）series和dataframe对象去重操作的区别：一个是unique(),一个是drop_duplicates()
（3）series对象变dataframe对象的方式：data[['列名']]，注意:describe()可以同时series和dataframe
'''
#--------------------pandas综合练习题---------------------
#（1）拿数据
# data=pd.read_csv('D:/Users/H/Desktop/Agent自动项目库/pandas练习数据.csv')
# # print(data)
# data.columns=['district', 'community', 'title', 'layout', 'area_sqm', 'price', 'floor', 'build_info', 'orientation', 'update_time', 'visitors', 'decoration', 'elevator']
# # print(data)
#1. 找到租金最低，和租金最高的房子
# data1=data.sort_values(by=['price'],ascending=False).head(1)
# data2=data.sort_values(by=['price'],ascending=False).tail(1)
# print(data2)
#2. 找到最近新上的 10 套房源
# data3=data.sort_values(by='update_time',ascending=False).head(10)
# print(data3)
#3. 查看所有更新时间
# data4=data[['district','update_time']]
# print(data4)
#4. 查看看房人数的平均值，最大值，最小值
# data5=data.visitors.describe()
# print(data5)
#5. 查看不同看房人数的房源数量，`as_index = False` 分组字段不作为行索引（默认为 True）
# data6=data.groupby('visitors',as_index=False).agg({'district':'count'})
# print(data6)
#6. 查看房租价格的分布，例如：平均值，标准差，中位数…
# data7=data.price.describe()
# print(data7)
#7. 找到看房人数最多的朝向
# data7=data.replace({'district':{'团结湖租房':"团结"}})    # 改名操作！！！
# print(data7)
# data8=data.sort_values(by='visitors',ascending=False).head(1).orientation
# print(data8)
#8. 查找最受欢迎的房型
# data9=data.sort_values(by='visitors',ascending=False).head(1).layout
# print(data9)
#9. 查找房子的平均租房价格（元 / 平米）
# data['avg_price']=data.apply(lambda x:x['price']/x['area_sqm'], axis='columns')
# print(data)
# apply方法 data.apply(fun,axis=0/1)

# ----------------------------pandas和seaborn绘图-------------------------------
##1、加载数据集，并设置 第1列为 索引列(语法模板！！！)，底层都是matplotlib
# info=pd.read_csv('位置',index_col=0)
# # print(info)
# # 2、查看数据集
# info.info()
# info.describe()
# # 3、需求：根据产地province进行分组，基于points列进行统计即可
# info1=info.groupby('province',as_index=False).agg('point','count').sort_values('count',ascending=False).head(10)
# info2=info1.get_group('beijing')  # 写法错误：get_group只能作用于groupby对象！！！
# 注意：重新理解分组（按照某字段进行分组，get_group只是拿到某一组）+聚合（将分组字段重构，只剩下分组字段列和聚合字段列）
# 4、针对上述结果进行绘图操作(随机数据)
# data={
#     'province':['beijing','shanghai','shenzhen','guangzhou','xiamen','nanchang'],
#     'count':[50,32,42,33,22,10]
# }
# data1=pd.DataFrame(data)
# data1['count']=data1['count']/(data1['count'].sum())  # 求比例写法
# 折线图
# data1.plot.line(x='province',y='count',figsize=(10,5),color=['r','g','b','y','c','m'],fontsize=15)
# 操作：定义参数，用字典封装后解析
# info_kwargs=dict(x='province',y='count',figsize=(10,5),color=['r','g','b','y','c','m'],fontsize=15)
# # 柱状图
# # data1.plot.bar(**info_kwargs)
# # 面积绘图
# # data1.plot.area(**info_kwargs)
# # 直方图
# data1.plot.hist(**info_kwargs)
# # 注意：条形图和直方图的区别：前者展示离散数字的分别，后者展示连续数值的频次分布（横坐标：连续区间，纵坐标：频次/次数）
# plt.show()  # 窗口显示

# ------------------------------seaborn(sns)绘图--------------------------------
# 准备数据
# 固定随机种子，每次运行生成一样的数据
np.random.seed(42)
n = 200

# 生成模拟数据，贴合tips数据集的数值特征
total_bill = np.round(np.random.uniform(5, 55, size=n), 2)
tip = np.round(total_bill * np.random.uniform(0.05, 0.22, size=n), 2)
sex = np.random.choice(["Female", "Male"], size=n, p=[0.4, 0.6])

data = {
    "total_bill": total_bill.tolist(),
    "tip": tip.tolist(),
    "sex": sex.tolist()
}
df = pd.DataFrame(data)
# # 1、创建画布
# fig,ax=plt.subplots(figsize=(10,5))
# # 2、绘制直方图图形
# # 参1：data:数据集
# # 参2：x:x轴列名
# # 参3：hue:分组依据列名
# sns.histplot(data=df,x='total_bill',hue='sex')
# # 3、设置标题
# ax.set_title('男女总账单情况',fontsize=20)
# # 4、展示图形
# plt.show()

# -------------------散点图：scatter()---------------------
# 创建画布
# fig, ax = plt.subplots(figsize=(10,5))
# # 需求描述总账单和小费情况(绘图)
# sns.scatterplot(x="total_bill", y="tip", data=df,hue='sex')
# # 设置标题
# ax.set_title('男女消费总消费和消费分布情况')
# # 看
# plt.show()















