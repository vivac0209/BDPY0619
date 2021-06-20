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

# 另一種寫法 找出上課人數超過8人 跟 遠端上課
# 先在函式寫好過濾條件

def isAvailable(course):
    return course.attendee >= 8


def isRemote(course):
    return course.remote is True

print("will open remote course")
willOpenRemoteCourse = tuple(filter(isAvailable, filter(isRemote, courses)))

# 這樣寫 只會顯示記憶體位置
#willOpenRemoteCourse = (isAvailable, isRemote)
pprint(willOpenRemoteCourse)