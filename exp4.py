# 打开yq_in.txt文件
yq_in = 'yq_in.txt'
f_in = open(yq_in, 'r', encoding = 'gb2312') 
# 将文件内内容写入file
file = f_in.read()
f_in.close()

list0=[]
simple = []
flag=0
simple.append(file.split())  # file里的全部元素作为一个列表集合放入simple这个列表里
for i in simple[0]:   # 遍历simple列表里第0个元素
    list0.append(i)  # 将其添加到list0中

new_str = ''
j = 0
num = 0
help_list = []

for i in list0:
    if(j == 0 ):
        limit = i
        print(i, end='\n')
#         help_list.append(i)
    else:
        if(i == limit or list0[j-1] == limit or list0[j-2] == limit):
            if(i == limit):  # 省份
                pass
            elif(list0[j-1] == limit):  # 城市
                print(i, end='\t')
            elif(list0[j-2] == limit):  # 数量
                i = int(i)
                num += i
                print(i, end='\n')
        else:
            limit = i
#             help_list.append(i)
            print('总数为：', num)
            num = 0  # 总数重置清零
            print('-'*50)
            print(i, end='\n')
    j+=1
print('总数为：', num)

iyq_out = 'yq_out_04.txt'
f_out=open(yq_out, "w+")
f_out.write(new_str)
f_out.close()
