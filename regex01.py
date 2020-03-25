"""
regex01.py re模块 功能函数演示2
生成match对象函数
"""
import re
s = "今年是2019年,建国70周年"
pattern = r'\d+'

# 返回迭代对象
iter = re.finditer(pattern,s)
for i in iter:
    print(i.group())    # 获取match对象对应内容，每一个匹配到的i就是一个match对象
#2019
#70

# 完全匹配一个字符串
m = re.fullmatch(r'[,\w]+',s)  #注意这种写法，直接将\w写在字符集[]中，这样是可以的
print(m.group())
#今年是2019年,建国70周年

# 匹配目标字符串的开始位置
m = re.match(r'\w+',s)
print(m.group())
#今年是2019年

# 匹配第一处符合正则规则的内容
m = re.search(r'\d+',s)
print(m.group())