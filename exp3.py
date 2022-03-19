# 打开yq_in.txt文件
while(1):
    yq_in = input()
    try:
        f_in = open(yq_in, 'r', encoding = 'gb2312') 
        # 将文件内内容写入file
        file = f_in.read()
        f_in.close()
        break
    except FileNotFoundError:
        print('FileNotFoundError!请重新输入！')

list0=[]
simple = []
flag=0
simple.append(file.split())  # file里的全部元素作为一个列表集合放入simple这个列表里
for i in simple[0]:   # 遍历simple列表里第0个元素
    list0.append(i)  # 将其添加到list0中

new_str = ''
j = 0
flag = 0
limit = input()  # 由用户输入需要输出的省份名字
for i in list0:
    if(i == limit or list0[j-1] == limit or list0[j-2] == limit):
        if(flag == 0):
            new_str += i
            new_str += '\n' # 省份做单独一行
            flag = 1

        if(list0[j-1] == limit):  # 市区
            new_str += i
            new_str += '\t'
        elif(list0[j-2] == limit):  # 数量
            new_str += i
            new_str += '\n'
    j+=1
print(new_str)

yq_out = input()
f_out=open(yq_out, "w+")
f_out.write(new_str)
f_out.close()
