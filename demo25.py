import collections
from pprint import pprint
from functools import reduce
from itertools import groupby
import time
import multiprocessing
import os

course = collections.namedtuple("course", ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
andbiz = course(name='andbiz', field='android', attendee=12, remote=False)
pykt = course(name='pykt', field='python', attendee=9, remote=False)
aiocv = course(name='aiocv', field='python', attendee=20, remote=True)
cplus = course(name='cplus', field='c/c++', attendee=15, remote=False)
courses = (poop, bdpy, andbiz, pykt, aiocv, cplus)


def transform(x):
    print(f'{os.getpid()}==>start process record:{x.name}')
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f'{os.getpid()}==>done process record:{x.name}')
    return result

# multiprocessing 同步工作
if __name__ == '__main__':
    start = time.time()
    # processes=2 只能一次跑兩筆資料
    pool = multiprocessing.Pool(processes=2, maxtasksperchild=1)
    print(f"now we can parallel with process:{pool._processes}")
    result = tuple(pool.map(transform, courses))
    end = time.time()

    pprint(result)
    print(f"total time:{end - start:.6f} seconds")