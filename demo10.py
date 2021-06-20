import collections

# 像是把格式都設定好了
course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

# 依照格式 放入對應的值
poop = course(name='poop', field='python', attendee=10, remote=False)
print(poop)
print([poop])
print(poop.remote, poop.attendee, poop.name)

# 不能修改值
poop.name = 'aiocv'