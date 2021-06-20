import collections
from pprint import pprint
from functools import reduce
from itertools import groupby

# 設定出格式 該輸入的值
# 把各個課程資料輸入 裝進tuple 再print出

# 這邊有改順序andbiz改到第三個
course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
andbiz = course(name='andbiz', field='android', attendee=12, remote=False)
pykt = course(name='pykt', field='python', attendee=9, remote=False)
aiocv = course(name='aiocv', field='python', attendee=20, remote=True)
cplus = course(name='cplus', field='c/c++', attendee=15, remote=False)
courses = (poop, bdpy, andbiz, pykt, aiocv, cplus)

courseCategory = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},
                        courses, {'python': [], 'android': [], 'c/c++': []})
pprint(courseCategory)


# 這邊是老師舉例
x1 = {'a': 0, 'b': 1, 'a': 0 + 1, 'b': 1 + 2}
print(x1)
x2 = {'a': 0, 'b': 1}
x3 = {'a': 1, 'b': 2}
x4 = {**x2, **x3}
print(x4)

# 後面壓前面
x5 = ['a', 'b'] + ['c']
print(x5)
x6 = {'a': ['apple'], 'b': ['banana']}
x7 = {'c': ['cookie'], 'b': ['banana', 'apple pie']}
print({**x6, **x7})