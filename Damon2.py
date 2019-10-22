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

# 转换
'''
    upper() 转大写
    lower() 转小写
    title() 每个单词的首字母大写
    capitalize() 字符串的第一个单词的首字母大写
'''
s = 'xjh is a man'
print(s)
s = s.upper()
print(s)
s = s.capitalize()
print(s)
s = s.title()
print(s)
