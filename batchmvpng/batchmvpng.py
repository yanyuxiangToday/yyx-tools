# -*- coding: utf-8 -*-
'''
@Time    : 2021/8/19
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: batchmvpng.py
@Software: PyCharm
'''

import os
import yyx_tools as yt
import shutil
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--end_num',        type=str,  default='0002134')
    parser.add_argument('--src_folder',     type=str,  default='BanMaKanShiJie139')
    parser.add_argument('--add_tail',       type=bool, default=False)
    parser.add_argument('--data_dir',       type=str,  default='/Volumes/yyx_mobile_ssd/projects_data/yfd/yyx_video_compress_gain/banmaaike/data/ori_extra_frames')
    args = parser.parse_args()
    return args

def find_dst_folder(args):
    '''
    最后会生成一个格式为 {args.src_folder}_part{n} 的字符串，后续的file会dump到这个文件夹下

    如果之前已经有部分part，则尾数自动加一
    '''

    folder_list = os.listdir(args.data_dir)
    src_folder_len = len(args.src_folder)
    m_list = [folder for folder in folder_list if folder[:src_folder_len] == args.src_folder]
    m_list.remove(args.src_folder)
    yt.list.rm_elem(m_list)
    if m_list:
        m_list = sorted(m_list, key=lambda k:int(k.split('part')[-1]))
        if args.add_tail:
            return m_list[-1]
        else:
            return f'{args.src_folder}_part{int(m_list[-1].split("part")[-1]) + 1}'
    else:
        return f'{args.src_folder}_part0'

def find_start_num(args):
    src_image_list = os.listdir(os.path.join(args.data_dir, args.src_folder))
    yt.list.rm_elem(src_image_list)
    src_image_list.sort()
    return int(src_image_list[0][:-4])

def batch_mv_png(args):
    # 自动生成要dump的文件夹名，格式为{args.src_folder}_part{n}
    dst_folder = find_dst_folder(args)
    src_dir = os.path.join(args.data_dir, args.src_folder)
    dst_dir = os.path.join(args.data_dir, dst_folder)

    # 自动找到起始文件，默认是找到当前文件夹的第一个文件
    start_num = find_start_num(args)

    # 由于一个视频至少要75帧，因此判断要大于75
    end_num = int(args.end_num)
    if not end_num - start_num >= 75 and not args.add_tail:
        os.system(f'open {args.data_dir}')
        raise Exception(f'less than 75 iterm, now count is {end_num - start_num}')

    # 当args.add_tail==True的时候，不会新建文件夹，而是会将当前要移动的序列转移到上一个part中
    add_tail = True if os.path.isdir(dst_dir) else False
    pre_count = len(os.listdir(dst_dir)) if add_tail else 0
    yt.checkdir(dst_dir)

    # loop，移动文件
    for png_num in range(start_num, end_num + 1):
        src_path = os.path.join(src_dir, str(png_num).zfill(7) + '.png')
        assert os.path.exists(src_path)
        print(f'mv {src_path} to {shutil.move(src_path, dst_dir)}')

    # print log
    print('-' * 10)
    print(f'dump to {dst_folder}')
    print(f'deal with {start_num} to {end_num}')
    if add_tail:
        print('add tail')
        print(f'iterms should be {end_num - start_num + pre_count + 1}')
    else:
        print('create new')
        print(f'iterms should be {end_num - start_num + 1}')

    # 如果当前文件夹的所有文件都被清空，则删除当前文件夹
    # WARNING! rm -rf
    # if len(os.listdir(src_dir)) == 0 or os.listdir(src_dir) == ['.DS_Store']:
    #     os.system(f'rm -rf {src_dir}')
    return

if __name__ == '__main__':
    args = get_args()
    batch_mv_png(args)
