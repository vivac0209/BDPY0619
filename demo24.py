import collections
from pprint import pprint
from functools import reduce
from itertools import groupby
import time

course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
andbiz = course(name='andbiz', field='android', attendee=12, remote=False)
pykt = course(name='pykt', field='python', attendee=9, remote=False)
aiocv = course(name='aiocv', field='python', attendee=20, remote=True)
cplus = course(name='cplus', field='c/c++', attendee=15, remote=False)
courses = (poop, bdpy, andbiz, pykt, aiocv, cplus)


def transform(x):
    print(f'start process record:{x.name}')
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f'done process record:{x.name}')
    return result

start = time.time()
result = tuple(map(transform, courses))
end = time.time()

pprint(result)
print(f"total time:{end-start:.6f} seconds")