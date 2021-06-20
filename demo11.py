import collections
from pprint import pprint

course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)

# 裝進list中
courses = [poop, bdpy]
pprint(courses)

# 但list中可以做修改  把poop刪掉
del courses[0]
pprint(courses)

# 裝進tuple中 不能做修改 把oop刪掉  會跑出error
courses2 = (poop, bdpy)
pprint(courses2)
# del courses2[0]