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

'''
字符串内置函数：
    字符串判断相关函数：
        1、isupper() 是否小写
        2、islower() 是否大写
        3、isalpha() 是否字符串中只有字母组成，如果是则返回True，不是返回False
        4、isdigit() 是否是纯数字，如果是则返回True，不是返回False
        5、startswitch() 是否以指定的内容开头
        6、endswitch() 是否以指定的内容结尾
    
'''

s = 'hello'
print(s.isalpha())

qq = input('qq号码：')
print(qq.isdigit())

print(qq.startswith('x'))
