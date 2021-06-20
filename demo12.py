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

# 找出是遠端課程remote is true
# 找一個值去接過濾後的結果
# filter(這邊寫function ) 這邊使用function : lambda
isRemoteCourse = filter(lambda x: x.remote is True, courses)
print(type(isRemoteCourse))
print(isRemoteCourse)
# 要印出結果 要寫for loop
pprint([x for x in isRemoteCourse])

# 找出 人數超出13個人的課程
isOver13 = filter(lambda x: x.attendee >= 13, courses)
pprint([x for x in isOver13])

##################################
##################################
#過濾兩種條件 人數超過10 跟遠距上課
print("over 10 and remote")
isOver10 = filter(lambda x: x.attendee >= 10, courses)
isOver10RemoteCourse = filter(lambda x: x.remote is True, isOver10)
pprint([x for x in isOver10RemoteCourse])
