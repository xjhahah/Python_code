# coding=utf-8

'''
    字符串方法
'''

# 查找
s = 'D:\PythonCode\Python_code\Damon2.py'
index = s.rfind('\\')
print(index)
print(s[index + 1:])

# 替换字符串
s = 'hello 帅哥，我是你爸爸。帅哥，我是你爷爷'
s = s.replace('帅哥', '美女', 1)
print(s)

# 切割

