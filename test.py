# coding=utf-8
'''
    1、橘色字体代表关键字
    2、紫色字体代表函数对象
'''

# 查看关键字
import keyword
import random

# print(keyword.kwlist)

#  r+'' 保留字符串原有格式  r == raw  原有的
s1 = r'hello \n world'
print(s1)

'''
# 变量类型：
# int
# float
# bool
# byte：字节，b'+字符串
# list：列表 [] 允许重复元素
# tuple：元组 () 允许重复元素
# set：集合 {} 不允许又重复元素
# dict：字典 {key:value}
'''
sockets = {'ip': '192.168.0.1', 'port': 8080}

print(sockets['ip'])

# 运算符
s = 'hello'
ss = s + ' world'
print(ss)
s = 10
print(s ** 3)

a = 10
print(id(a))  # 获取变量的地址

b = 10
print(id(b))
print()
print(a == b)  # 比较的是两个数的值
print(a is b)  # 比较的是两个数的地址

a, b = 10, 20
print(a, b)

# 简单的猜数字游戏
random_num = random.randint(1, 10)

time = 0

while time < 3:
    num = int(input("请输入你才猜的数字："))
    if (num == random_num):
        print("恭喜你找到了！")
        print(random_num)
        break
    elif num < random_num:
        print("猜小了。。")
    else:
        print("猜大了。。。")
    time += 1
if time == 3:
    print('您要猜的数字：', random_num)
    print("您的机会已用完，太菜了")
