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

# 把課程名稱name跟課程種類field 抓出來 再放進tuple
name_and_field = map(lambda x: {'name': x.name, 'field': x.field}, courses)
pprint(tuple(name_and_field))

#另一種形式 打name跟field抓出來 再放進去tuple
shortCourse = collections.namedtuple('shortCourse', ['name', 'field'])
shortCourses = map(lambda x: shortCourse(name=x.name, field=x.field), courses)

print('using namedtuple')
pprint(tuple(shortCourses))