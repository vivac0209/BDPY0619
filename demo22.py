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

# 透過sorted去排序 依field課程種類去排 照字母順序
sorted_courses = sorted(courses, key=lambda x: x.field)
# print("sorted course:")
# pprint(sorted_courses)

print("what is group by?")
for c in groupby(sorted_courses, lambda x: x.field):
    # print(type(c), c[0], c[1])
    print(c[0], [x for x in c[1]])
print("################")
#這邊就沒有加入sorted去排序
print("what if not group by?")
for c in groupby(courses, lambda x: x.field):
    # print(type(c), c[0], c[1])
    print(c[0], [x for x in c[1]])

# 這邊是歸類好後 把同類型的一起顯示出來
# 用list來顯示出來
print("sorted, using list comprehension")
courseCategory = {c[0]: list(c[1]) for c in groupby(sorted_courses, lambda x: x.field)}
pprint(courseCategory)

#這邊是改成tuple去顯示
print("sorted, using list comprehension, with tuple")
courseCategory2 = [(c[0], list(c[1])) for c in groupby(sorted_courses, lambda x: x.field)]
pprint(courseCategory2)