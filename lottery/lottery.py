# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/19
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: lottery.py
@Software: PyCharm
"""


def jackpot(same):
    jp = {
        (5, 2): 1,
        (5, 1): 2,
        (5, 0): 3,
        (4, 2): 4,
        (4, 1): 5,
        (3, 2): 6,
        (4, 0): 7,
        (3, 1): 8,
        (2, 2): 8,
        (3, 0): 9,
        (1, 2): 9,
        (2, 1): 9,
        (0, 2): 9,
    }
    if same in jp:
        print('*' * 18)
        print('******** jackpot!!!')
        print(f'******** {jp[same]} 等奖')
        print('*' * 18)


def open_lottery(buy, lottery):
    l_pre, l_last = lottery[:5], lottery[5:]
    for i, b in enumerate(buy):
        pre, last = b[:5], b[5:]
        pre_res = [l for l in pre if l in l_pre]
        last_res = [l for l in last if l in l_last]
        print(f'{i}: pre {str(pre_res):8} last {str(last_res):8}')
        jackpot((len(pre_res), len(last_res)))
    return


if __name__ == '__main__':
    # 20210918
    buy = [
        [3, 8, 21, 30, 31, 3, 4],
        [1, 6, 15, 22, 32, 3, 12],
        [2, 4, 5, 25, 31, 11, 12],
        [2, 7, 23, 27, 30, 2, 3],
        [3, 7, 17, 31, 34, 1, 4],
        [1, 11, 27, 29, 32, 3, 10],
        [8, 16, 27, 33, 35, 4, 7],
        [11, 12, 14, 21, 33, 2, 12],
        [15, 21, 22, 25, 29, 10, 11],
        [8, 15, 25, 33, 35, 3, 7],
    ]

    lottery = [5, 19, 22, 26, 35, 2, 6]
    open_lottery(buy, lottery)
