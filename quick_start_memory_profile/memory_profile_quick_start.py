# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/9
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: memory_profile_quick_start.py
@Software: PyCharm
"""

from memory_profiler import profile


@profile
def go():
    for i in range(1000):
        pass

    x = 1 + 2
    return


if __name__ == '__main__':
    go()
