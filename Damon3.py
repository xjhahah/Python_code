'''
数据类型：
    int str float bool complex(复数)
    容器：
        列表 list[]
        元组 tupe()
        集合 set{}
        字典 dict{}
# 列表连接，相当于 +=
    a.extend(b)
    print(a)
'''



# 计算器
for i in range(1, 7):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j), end='')
    print()
