import collections
from pprint import pprint

# 設定出閣式 該輸入的值
# 把各個課程資料輸入 裝進tuple 再print出
course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=False)
aiocv = course(name='aiocv', field='python', attendee=20, remote=True)
andbiz = course(name='andbiz', field='android', attendee=12, remote=False)
courses = (poop, bdpy, pykt, aiocv, andbiz)
# pprint(courses)


#印出所有的資料
pprint([c for c in courses])
#只印出python的資料
print("only print python course")
pprint([c for c in courses if c.field == 'python'])

# 把指印出python的資料裝進tuple
print("convert to tuple")
pprint(tuple([c for c in courses if c.field == 'python']))

#直接把上面兩者合併
pprint(tuple(c for c in courses if c.field == 'python'))


