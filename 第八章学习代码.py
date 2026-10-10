              #------------- 文件编码-----------------
# 思考：计算机只能识别0和1，那么我们丰富的表达内容是如何被计算机识别的呢？
# 答案：使用编码技术将内容翻译成0和1进行读取

# 计算机中许多可用的编码类型（UTF-8（全球通用编码格式）,GBK（中文体系）,Big-5（繁体字））

             #--------------文件的读取操作---------------

#1-open()——打开文件函数
              # open(name,mode,encoding)
              #name:要打开的目标文件名的字符串(文件位置+文件名+.txt)
              # ————————不是文件夹——————————！！！！
              #mode:设置打开文件的模式（访问模式）：只读/写入/追加“r,w,a”
              #encoding：编码格式（推荐使用UTF-8）
# f=open("D:/Users/H/Desktop/测试.txt","r",encoding="UTF-8")
# print("------------------------------")

# #2-read()——读取文件
# # print(f"读取的文件名为：{type(f)}")
# # print(f"读出文件的5个字节为：{f.read(5)}")         # 可选择性的读取字节个数
# print("------------------------------")

# #3-readlines()——读取文件“可读出文件的全部行以列表形式输出”
#  # print(f"读取的文件名为：{type(f.readlines())}")
# print(f"读出文件的全部字节为：{f.readlines()}")    # 可直接读取全部的字节
# print("------------------------------")

# #4-readline()——文件读取“一次读取一行”
# print(f"第一行：{f.readline()}")
# print(f"第二行：{f.readline()}")
# print(f"第三行：{f.readline()}")
# for line in f:
#     print(f"每一行的内容为：{line}")
# print("------------------------------")

# # 5-close()——文件的关闭
# f.close()
# print("------------------------------")
# # 6-with open 语法操作文件（无需close!!!）
# with open("D:/Users/H/Desktop/测试.txt","r",encoding="UTF-8")as f:
#     print(f"读取的内容为：{f.readlines()}")
# print("------------------------------")
            #-----------------综合案例-----------------
# print("方法一------------------------------")
'''with open("D:/Users/H/Desktop/word.txt","r",encoding="UTF-8")as f:
    num=0
    sum1=f.read()
    sum2=sum1.split()
    print(sum2)
    for i in sum2:
        print(i)
        if i=="itheima":
            num+=1
    print(f"itheima共有{num}次出现")
print("方法二---------------------------------")
f=open("D:/Users/H/Desktop/word.txt","r",encoding="UTF-8")
x=f.read()
print(x)
y=x.count("itheima")
print(f"itheima出现的次数为：{y}")
print("---------------------")
f=open("D:/Users/H/Desktop/word.txt","r",encoding="UTF-8")
x=f.readlines()
print(x)
print("---------------------")'''
    # ————————————————————————————文件的写入操作——————————————————————————

       #文件操作————打开+写入+关闭
# 1.打开文件
f=open("D:/Users/H/Desktop/写入文件.txt","w",encoding="UTF-8")
# 2.文件写入
f.write("hello world！")
# 3.内容刷新
f.flush()
# —————注意：直接调用write写入内容未被真正写入文件（硬盘）中，而是被暂存再内存中，称之为“缓冲区”！
# —————当使用flush时才是真正被写入了文件内部
# #--------------------文件写入演示-----------------------
# f=open("D:/Users/H/Desktop/写入文件.txt","w",encoding="UTF-8")
# f.write("hello world，我爱中国！！！")
# f.flush()    # 功能：将内存区功能写入硬盘中
# f.close()    # 注意：close  的调用包括了flush的功能
#   # write的调用特点（1）文件存在就覆盖/清空原有内容；（2）文件不存在就创建；
#
#               # ————————————————————————————文件的追加操作——————————————————————————
# f=open("D:/Users/H/Desktop/写入文件.txt","a",encoding="UTF-8")
# f.write("\n我是黄老师，同学们好！")
# f.close()

print("-----------------------综合案例---------------------")

f=open("D:/Users/H/Desktop/bill.txt","r",encoding="UTF-8")
answer1=f.read()
print(answer1)
f.close()
print("----------------------------")
f=open("D:/Users/H/Desktop/bill.txt.bak.txt","w",encoding="UTF-8")
f.write('''周杰轮,2022-01-01,100000,消费,正式           # 注意： 此处需要用"三引号"换行，不可用"双引号"换行因为双引号只能一行，语法上不兼容。
周杰轮,2022-01-02,300000,收入,正式
周杰轮,2022-01-03,100000,消费,测试
林俊节,2022-01-01,300000,收入,正式
林俊节,2022-01-02,100000,消费,测试
林俊节,2022-01-03,100000,消费,正式
林俊节,2022-01-04,100000,消费,测试
林俊节,2022-01-05,500000,收入,正式
张学油,2022-01-01,100000,消费,正式
张学油,2022-01-02,500000,收入,正式
张学油,2022-01-03,900000,收入,测试
王力鸿,2022-01-01,500000,消费,正式
王力鸿,2022-01-02,300000,消费,测试
王力鸿,2022-01-03,950000,收入,正式
刘德滑,2022-01-01,300000,消费,测试
刘德滑,2022-01-02,100000,消费,正式
刘德滑,2022-01-03,300000,消费,正式''')
f.close()
print("----------------------------")
# f=open("D:/Users/H/Desktop/bill.txt","r",encoding="UTF-8")
# for readline in f:
#     readline=readline.strip()
#     readline=readline.split(",")
#     print(readline)
#     print(readline)
# print("----------------------------")
print("-----------------------方案一-----------------")
# f=open("D:/Users/H/Desktop/bill.txt","r",encoding="UTF-8")
# for line1 in f:
#     line2=line1.strip()        #去除将字符串变为列表的换行符用字符串处理法————strip()/replace(\n,"")
#     line3=line2.split(",")     #字符串以“，”为单位把字符串分割成列表形式
#     if line3[4]!="测试":
#         # f1 = open("D:/Users/H/Desktop/筛选文件.txt", "w", encoding="UTF-8")
#         # f1.write(line1)                                         # 此程序会被反复覆盖的原因是文件被反复的open
#         f2 = open("D:/Users/H/Desktop/答案文件.txt", "a", encoding="UTF-8")
#         f2.write(line1)
#     else:
#         continue
# f.close()

# print("-----------------------方案二-----------------")
# f=open("D:/Users/H/Desktop/bill.txt","r",encoding="UTF-8")
# f1=open("D:/Users/H/Desktop/bill1.txt","w",encoding="UTF-8")
# for line1 in f:
#     line2=line1.strip()
#     line3=line2.split(",")
#     if line3[4]=="测试":
#        continue        # countinue与break的区别：（1）continue一出来本次的循环结束；（2）break一出来整个循环就拜拜了
#     else:
#         f1.write(line1)  # 只要不反复open文件，write就不会反复覆盖！！！
# f.close()
# f1.close()




























