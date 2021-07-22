# -*- coding:utf-8 -*-
# __author__ = 'kafka'

import time
from functools import wraps

def my_loop(x):
    return x

def timefn(fn):
    @wraps(fn)
    def measure_time(*args,**kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f"@timefn:{fn.__name__} took {t2 - t1: .5f} s")
        return result
    return measure_time