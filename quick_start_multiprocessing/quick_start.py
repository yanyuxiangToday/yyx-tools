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


def main():
    p_list = []
    for i in range(3):
        p_list.append(Process(target=info, args=(i, )))

        # Launch.
        p_list[i].start()

    for i in range(3):
        # Waiting for each sub process.
        p_list[i].join()
    print('All process done.')


if __name__ == '__main__':
    main()