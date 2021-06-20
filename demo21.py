import collections
from pprint import pprint
from functools import reduce

# 設定出格式 該輸入的值
# 把各個課程資料輸入 裝進tuple 再print出
course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=False)
aiocv = course(name='aiocv', field='python', attendee=20, remote=True)
andbiz = course(name='andbiz', field='android', attendee=12, remote=False)
cplus = course(name='cplus', field='c/c++', attendee=15, remote=False)
courses = (poop, bdpy, pykt, aiocv, andbiz, cplus)

# 把課程做分類 把python 跟android 的分出來歸類
# 但是這邊多加c++的課程 這樣就會跑出error
# 這邊再改demo20檔的內容
def reducer(acc, val):
    #acc.setdefault(val.field, [])
    acc[val.field].append(val.name)
    return acc


course_by_category = reduce(reducer, courses, collections.defaultdict(list))
pprint(course_by_category)
