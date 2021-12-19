# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''


import pickle
import os

def main_func(dir_path, dump_path):
    train_path = os.path.join(dir_path, 'train_split_0.pkl')
    test_path = os.path.join(dir_path, 'test_split_0.pkl')
    train_word = pickle.load(open(train_path, 'rb'), encoding='utf-8')
    test_word = pickle.load(open(test_path, 'rb'), encoding='utf-8')
    print('len train samples is {}, len test samples is {}, all samples is {}'.format(len(train_word), len(test_word), len(train_word) + len(test_word)))

    anno_path = os.path.join(dir_path, 'final_annotations_dict.pkl')
    anno_word = pickle.load(open(anno_path, 'rb'), encoding='utf-8')
    print('len final_annotations_dict is {}'.format(len(anno_word)))

    cap_path = os.path.join(dir_path, 'final_captions_dict.pkl')
    cap_path = pickle.load(open(cap_path, 'rb'), encoding='utf-8')
    return

if __name__ == '__main__':
    path = '/Users/hardyyan/Documents/pycharmProj/diving/MTL-AQA-master/MTL-AQA_dataset_release/Ready_2_Use_backup'
    dump_path = '/Users/hardyyan/Documents/pycharmProj/diving/MTL-AQA-master/MTL-AQA_dataset_release/Ready_2_Use'
    main_func(path, dump_path)