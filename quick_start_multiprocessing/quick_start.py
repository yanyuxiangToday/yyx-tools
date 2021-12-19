# -*- coding: utf-8 -*-
'''
@Time    : 2021/8/26
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: quick_start.py
@Software: PyCharm
'''

from multiprocessing import Process
import os

def info(title):
    print('-' * 10)
    print(title)
    print('module name:', __name__)  # Name.
    print('parent process:', os.getppid())  # Id of main process.
    print('process id:', os.getpid())  # Id of sub process.
    for i in range(10 ** 6):
        pass
    print(f'{title} {os.getpid()} done')

if __name__ == '__main__':
    p_list = []
    for i in range(3):
        # La
        # 启动三个多进程，其中args需是一个迭代器，按照元组格式写
        p_list.append(Process(target=info, args=(i, )))

        # 进程启动
        p_list[i].start()

    for i in range(3):
        # 父进程等待当前所有子进程结束方可继续执行
        p_list[i].join()
    print('hello')