import collections
from pprint import pprint
from functools import reduce

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

# 算總和
total_income = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
pprint(total_income)
total_sum = reduce(lambda acc, val: acc + val["income"], total_income, 0)
print(total_sum)

# 另一種算總和方式 直接使用sum
print(sum(x['income'] for x in total_income))