"""
初识对象
生活类比：
设计表格+打印表格+填写表格
python语句：
设计类（class）+创建对象+对象属性赋值
"""
# 设计类（设计表格）
# class student():
#     name=None
#     gender=None
#     nationality=None
#     native_place=None
#     age=None
# 打印表格
# stu_1=student()
# # 表格填写（赋值）
# stu_1.name="林俊杰"
# stu_1.gender="男"
# stu_1.nationality="中国"
# stu_1.native_place="山东"
# stu_1.age=19
# print(stu_1.name)
# print(stu_1.native_place)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.native_place)
# print(stu_1.age)
"""
class的语法：定义的属性（变量）-成员变量，定义的行为（函数）-成员方法
--------成员方法---------
def 方法名（self，参数1，参数2………………）
    方法体
"""
# --------------------定义类-------------------------
# class student():
#     name=None   # 属性
#     def say_hi(self):   # 行为
#         print(f"大家好，我是：{self.name}")
# stu=student()
# stu.name="黄老师"
# stu.say_hi()

#--------------------------类的成员方法---------------------------
'''
现实事物的组成：属性和行为
手机：属性（长宽，质量，型号），行为（拍照，打电话，上网）
class clock()：
id=None      # 序列号
price=None    # 零售价

def ring (self):    # 响铃
    import winsound
    winsound.Beep(2000,3000
'''
# ----------------------练习-------------------------
# class clock():  # “制作表格”
#     ID=None
#     price=None
#     def ring (self):
#         import winsound
#         winsound.Beep(2000,3000)
# clock=clock()    # “打印表格”
# clock.ID="爱你的第一声"
# clock.price=19.9
# print(f"闹钟的名称：{clock.ID},闹钟的价格：{clock.price}")
# clock.ring()

# -----------------------构造方法---__init__-----------------------------
# 好处：帮助我们省略填写图表的步骤and把属性放入了方法之中！！！
# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("你好！")
# stu=Student("黄老师",19)   # 省略了表格打印后的单个填写步骤！！！
# print(stu.name)
# print(stu.age)

print("------方法二：利用构造方法------------")
# class clock():
#     def __init__(self,ID,price):
#         self.ID=ID
#         self.price=price
#     def ring (self):
#         import winsound
#         winsound.Beep(2000,3000)
# clock=clock("爱你的第一声",19.9)
# print(f"闹钟的名称：{clock.ID},闹钟的价格：{clock.price}")
# clock.ring()

'''
-----------------------魔术方法----------------------
定义：python内置的方法有很多，总称为魔术方法
包括：__init__(构造方法)、__str__（字符串方法）,__lt__（>/<符号比较）,__le__（>=/<=符号比较）,__eq__（==符号比较）

'''
#   魔术方法案例分析
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print("你好！")
    # __str__方法：
    def __str__(self):
        return f"{self.name}, {self.age}"
    # __lt__方法：
    # def __lt__(self,other):
    #     return self.age<other.age
    # __le__方法：
    # def __le__(self, other):
    #     return self.age <= other.age
    # def __eq__(self,other):
    #     return self.age==other.age

stu1=Student("黄老师",19)   # 省略了表格打印后的单个填写步骤！！！
stu2=Student("李老师",22)
# print(stu.name)
# print(stu.age)
print("--------------")
print(stu1)
print(stu2)
print("--------------")
# print(stu1>stu2)
# print(stu1<stu2)
print("--------------")
# print(stu1>=stu2)
# print(stu1<=stu2)
print("--------------")
# print(stu1==stu2)

'''
 --------------------------------封装-----------------------------
定义：将显示世界的属性和行为，封装到程序世界的成员变量和成员方法
私有成员：无法被类对象直接使用的，__a__的形式即可
公有成员：可以直接被类使用的功能
'''
# 定义私有成员（变量/方法）
# class phone():
#     __current_vltage=None    # __类对象定义方法
#     def __keep_single_core(self):
#         print("让CPU按照单核运行")
# phone=phone()
# phone.__current_vltage=1
# phone.__keep_single_core()    # 私有成员无法被类直接使用！！！

# 私有成员的作用：私有成员不能在外部使用，但可以在类的内部使用。eg：手机内部的电压情况可以被手机自己使用，但不能被用户使用
print("-----------------------")
# class phone():
#     __current_vltage=3               # 私有变量
#     def __keep_single_core(self):    # 私有方法
#         print("让CPU按照单核运行")
#     def call_by_5g(self):
#         if self.__current_vltage>=1:   #  运用calss内的属性或方法必须“self”!!!
#             print("5g通话已开启！")
#         else:
#             print("电量不足，请充电！")
# phone=phone()     # 把类打印下来，用程序填写
# phone.call_by_5g()

# 习题练习————————设计带有私有成员的手机
# class phone():
#     __is_5g_enable=False      # 私有变量
#     def __check_phone(self):
#         if self.__is_5g_enable==True:  # 私有方法
#             print("5G开启！")
#         else:
#             print("4G开启！")
#     def call_by_5g(self):
#         self.__check_phone()
#         print("正在通话中…………")
# phone=phone()
# phone.call_by_5g()
'''
------------------------------继承-------------------------------
定义：把已有的功能拿过来继续使用
现实生活例子：苹果手机的迭代，都是在传统的基础上修改
语法：class 类名（父类名）：
            类内容体 
分类：单继承和多继承
注意：多继承的继承顺序先来后到原则
'''
# 单继承
# class phone():
#     IMEI=None
#     def call_by_4g(self):
#         print("我是4g")
# class phone2026(phone):
#     def call_by_5g(self):
#         print("我是5g")
# phone=phone2026()
# phone.call_by_4g()
print("--------------------------")
# 多继承
# class phone():
#     IMEI=None
#     def call_by_4g(self):
#         print("我是4g")
# class phone2026():
#     def call_by_5g(self):
#         print("我是5g")
# class NFC_reader():
#     nfc_type="第五代"
#     def nfc_read_card(self):
#         print("nfc读卡")
# class ID_face():
#     def id_face(self):
#         print("面部解锁")
# class phone_super(phone,phone2026,NFC_reader,ID_face):
#     pass    # 类里面不想写东西了只是单纯的继承，可以直接pass掉
# my_phone=phone_super()    # 类转程序
# # 类的测试
# my_phone.call_by_4g()
# my_phone.call_by_5g()
# my_phone.id_face()
# my_phone.nfc_read_card()

"""
------------------------------复写-------------------------------
定义：对继承的类不满意需要修改
情景：继承家业
注意：复写过程中仍然需要用一些父类功能
使用规范："父类.（变量/方法）"
"""
# class phone():
#     IMEI=None
#     producter="苹果"
#     def call_by_4g(self):
#         print("我是4g")
# class phone2026(phone):
#     producter ="华为"
#     def call_by_5g(self):
#         print(f"父类的公司是:{phone.producter}")     # 复写中引用父类变量
#         phone.call_by_4g(self)                     # 复写中引用父类方法  注意：self!!!
#         print("我是5g")
# my_phone=phone2026()       # 类的实例化！！！（拿过来用）
# print(my_phone.call_by_5g())

'''
------------------------------类型注解-------------------------------
功能：帮助第三方IDE工具对代码类型推断，协作做代码提示；(有注释，有帮助ctrl+p)

'''
# 基础数据类型注解：
var1:int=10
var2:float=1.2
var3:bool=True
#类对象注解：
class student():
    pass
stu:student=student()
# 容器内容注解：
my_list:list[int]=[1,2,3]
my_tuple:tuple[int,float,bool]=(1,2.1,True)
my_dict:dict[str,int]={"老黄":19}
print("-----------------------------------")
# 函数方法的类型注解：(非强制性，美观)
def add(x:int,y:int):
    return x+y

# Union 类型 （“U”大写）        注意：必须先导包
# my_list:list[Union[int,str]]=[1,"sfshf"]

"""
'''
------------------------------多态-------------------------------
定义：多种状态完成某一行为时，使用不同的对象会得到不同的状态
情境：三个公司同时生产手机，最后得出了三种不同状态的手机
实际应用：以父类为定义声明，子类做实际工作，用于活动同一行为不同状态
"""
# 练习
# class Animal():                    # 抽象类
#     def speak(self):               # 抽象方法
#      pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
# dog=Dog()
# cat=Cat()
# dog.speak()
# cat.speak()

"""
------------------------------数据分析案例-------------------------------
目标：计算每日销售额——————制作图表的形式展示
数据形式：（日期+销售ID+销售额+省份）
业务流程：
1.设计一个类完成数据封装
2.定义一个接口---“给一个模板”（抽象类union），定义文件读取的相关功能，并利用子功能完成的读取
3.


"""
#-----------------------------一、 数据实体----------------------------------

from pyecharts.charts import Bar,Line
from pyecharts.options import *
from pyecharts.globals import ThemeType
class Record():
    def __init__(self,date,product_ID,money,province):
        self.date=date
        self.product_ID=product_ID
        self.money=money
        self.province=province
    def __str__(self):
        return f"{self.date},{self.product_ID},{self.money},{self.province}"  # 定义一个record被使用的形式
  # def __repr__(self):
  #     return f"{self.date},{self.product_ID},{self.money},{self.province}"  # 定义多个record被使用的形式

# 只有成员变量没有成员方法
# 情景理解：仅仅是绘制了一个箱子，没有进行任何的打印（实例化）和东西装入
# 构造方法：把成员变量转化成了成员方法，省略了额外的数据填入的过程（注：只需要在类定义内封装）“直接赋值，不需要先打印后调用赋值”

#-----------------------------二、抽象类接口--------------------------------------

# from data_define import Record   #---导包操作
import json
class FileReader():
    def read_data(self):  #  ----返回值的注释----
        pass
'''读取文件的数据，读取的每一条对象都转化为Record对象，将他们都装到list内返回即可
'''

#-----------------------------三、 复写读取文件----------------------------------

# csv读取
class TextReader(FileReader):
    def __init__(self,file_path:str):
        self.file_path=file_path
        pass  # 顶层设计
    def read_data(self):   # 复写（实现抽象方法）
        f=open(self.file_path,"r",encoding='utf-8')
        lines=f.readlines()
        f.close()
        records_list:list[Record]=[]
        for line in lines:
            line=line.strip()      # 需要赋值！！！
            line=line.split(",")   # 需要赋值！！！
            record=Record(line[0],line[1],int(line[2]),line[3])  # 箱子实例化    # 简称：封装
            records_list.append(record)  # 收集所有封装好的变量
        return records_list
# json读取
class JsonReader(FileReader):
    def __init__(self,file_path:str):   # 要外部赋值的时候最好都用构造方法
        self.file_path=file_path
    def read_data(self):   # 复写（实现抽象方法）
        f=open(self.file_path,"r",encoding='utf-8')
        lines=f.read()
        f.close()
        lines= json.loads(lines)
        records_list: list[Record] = []
        for data_dict in lines:
            record=Record(data_dict["date"],data_dict["id"],int(data_dict["money"]),data_dict["province"])   # 钱一定要化为整数型
            records_list.append(record)
        return records_list
#-----------------------------四、主程序调用----------------------------------
text_file_reader=TextReader("D:/Users/H/Desktop/2011年1月份销售数据.txt")  # 实例化
json_file_reader=JsonReader("D:/Users/H/Desktop/2011年2月份销售数据.txt")  # 实例化
list1=text_file_reader.read_data()
list2=json_file_reader.read_data()
# print(list1)
# for i in list1:
#     print(i)
# print("----------------------------")
# for i in list2:
#     print(i)


#------------------------------五、数据计算---------------------------------
all_list=list1+list2
# for record in all_list:
#     print(record)
dict_data={}
for record in all_list:
    if record.date in dict_data.keys():
        dict_data[record.date]+=record.money
    else:
        dict_data[record.date]=record.money
print(dict_data)

#--------------------------------六、pecharts可视化-----------------------------

# 条形图
bar=Bar(init_opts=InitOpts(theme=ThemeType.DARK))
bar.add_xaxis(list(dict_data.keys()))
bar.add_yaxis("销售额",list(dict_data.values()),label_opts=LabelOpts(False))
# bar.reversal_axis()
bar.set_global_opts(
    title_opts=TitleOpts(title="2021年公司1月-2月销售数据",pos_right="top")
)

# 折线图
line=Line(init_opts=InitOpts(theme=ThemeType.DARK))
line.add_xaxis(list(dict_data.keys()))
line.add_yaxis("趋势线",list(dict_data.values()),label_opts=LabelOpts(False),is_smooth=True)
bar.overlap(line)
bar.render("2021年公司1月-2月销售数据.html")







