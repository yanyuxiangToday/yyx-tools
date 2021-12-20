# -*- coding: utf-8 -*-
'''
@Time    : 2021/12/20
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: quick_start_timeit.py
@Software: VSCode
'''

import timeit
import bisect


if __name__ == '__main__':
  data_list = list(range(10**5))
  target = 99999
  loop_time_cost = timeit.timeit(
    stmt='data_list.index(target)',  # Function to test time.
    globals=globals(),  # Using global modules.
    number=100,  # Repeat times.
  )
  half_search_time_cost = timeit.timeit(
    stmt='bisect.bisect_left(data_list, target)',
    globals=globals(),
    number=100,
  )
  print(f'Loop time cost: {loop_time_cost}.')
  print(f'Half search time cost: {half_search_time_cost}.')
  print(f'(Loop time cost) / (half search time cost): '
        f'{loop_time_cost / half_search_time_cost}.')