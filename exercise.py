'''
运算符：
    成员运算符：in not in
    身份运算符：is is not
    三目运算符：if elif else
'''

# coding=uff-8

# 成员运算符
names = ['jiahu', 'caicai', 'haote', 'asheng']
print('jiahu' in names)
print('feifie' not in names)

a = 10
b = 10
print(a is b)
print(id(a))
print(id(b))
print(a is not b)

'''
# 模拟登录系统   练习while循环
count = 0
while count < 3:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123456':
        print('欢迎进入系统！')
        break
    else:
        print('密码或用户名错误，请重新输入！')
    count += 1
else:
    print('账户被锁定！请联系管理员')
'''

# 计算累加和
sum = 0
count = 1
while count <= 100:
    sum += count
    count += 1
else:
    print('累加和：', sum)
