# coding=utf-8

'''
    字符串方法
'''

# 查找
s = r'D:\PythonCode\Python_code\Damon2.py'
index = s.rfind('\\')
print(index)
print(s[index + 1:])

# 替换字符串
s = 'hello 帅哥，我是你爸爸。帅哥，我是你爷爷'
s = s.replace('帅哥', '美女', 1)
print(s)

# 切割   spilt('分隔符'，最大分割次数（可选）) ---- 返回分割后的列表 ， 如果没有指定分割次数默认所有的都进行切割
s = r'D:\PythonCode\Python_code\Damon2.py'
list1 = s.split('\\')

print(list1)