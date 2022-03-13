# 打开yq_in.txt文件
f_in = open("yq_in.txt", 'r', encoding = 'gb2312') 
# 将文件内内容写入file
file = f_in.read()
f_in.close()

list0=[]
simple = []
flag=0
simple.append(file.split())  # file里的全部元素作为一个列表集合放入simple这个列表里
for i in simple[0]:   # 遍历simple列表里第0个元素
list0.append(i)  # 将其添加到list0中

new_str = ''
num = 0
j = 0
for i in list0:
    if(j == 0):  #第一行数据读取
        # 第一行一定是省份
        new_str += i
        new_str += '\n'  # 省份做单独一行
    elif(j%3 == 0):  # 省份 
        # help_list.append(i)
        if(new_str.find(i) == -1):  # 如果new_str中没有找到i这个省份
            new_str += '\n'  # 与之前的数据分格开来
            new_str += i
            new_str += '\n'  # 省份做单独一行
    elif(j%3 == 1):  # 市区
        new_str += i
        new_str += '\t'
    elif(j%3 == 2):  # 数量
        new_str += i
        new_str += '\n'
    j+=1
    num += 1
print(new_str)

f_out=open("yq_out.txt","w+")
f_out.write(new_str)
f_out.close()