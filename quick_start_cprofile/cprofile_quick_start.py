# -*- coding: utf-8 -*-
'''
@Time    : 2021/9/8
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: cprofile_quick_start.py
@Software: PyCharm
'''


import time

def a():
    time.sleep(3)

def b():
    for _ in range(10**6):
        pass

def main():
    a()
    b()
    print('done')


if __name__ == '__main__':
    """cProfile 输出解释
    ncalls: 函数的被调用次数
    tottime: 函数总计运行时间，不含调用的函数运行时间
    percall: 函数运行一次的平均时间，等于tottime/ncalls
    cumtime: 函数总计运行时间，含调用的函数运行时间
    percall: 函数运行一次的平均时间，等于cumtime/ncalls
    filename:lineno(function): 函数所在的文件名、函数的行号、函数名
    """

    import cProfile
    import pstats

    # 直接打印结果
    # cProfile.run('main()')

    cProfile.run('main()', './out.txt')  # 打印结果并且输出到'./out.txt'中
    p = pstats.Stats('./out.txt')  # 将'./out.txt'中的内容读进来
    p.sort_stats('time').print_stats()  # 按照按照'time'项排序并输出

