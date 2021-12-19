# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''


import argparse
import ast

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', type=ast.literal_eval, help="just test", default=None)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    print(args.test)
