# -*- coding: utf-8 -*-
'''
@Time    : 2021/9/3
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: decorator.py
@Software: PyCharm
'''

import time


def timer(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        func(*args, **kw)
        print(f'cost time: {time.time() - t1}')

    return wrapper


@timer
def func1():
    for i in range(10 ** 6):
        pass
# 修饰器实际上做的事情就是把func1改写成了一个新函数wrapper
# @timer的写法实际等价于：func1 = timer(func1)，即执行func1()实际上是在执行wrapper()

@timer
def func2(sleep_time, output):
    time.sleep(sleep_time)
    print(f'this is in func2, output is {output}')


if __name__ == '__main__':
    func1()
    func2(3, 2)
