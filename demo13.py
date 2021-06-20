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
pprint(courses)

#跟demo12 不同
#這邊用tuple

isRemote = tuple(filter(lambda x: x.remote is True, courses))
pprint(isRemote)
#這邊不用裝到一個值 直接在print裡面打function 過濾出來
print("everything function")
pprint(tuple(filter(lambda x: x.remote is True, courses)))

# 看起來是直接把全部課程資料print出來
print("complete")
pprint(tuple(filter(lambda x: True, courses)))
