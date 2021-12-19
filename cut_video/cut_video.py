# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''


import os

def main_func(video_path, time_len, dump_path):
    cmd = 'ffmpeg -ss 00:00:00 -i {} -y -c copy -t {} {}'.format(
            video_path, time_len, dump_path)
    print(cmd)
    os.system(cmd)
    return



if __name__ == '__main__':
    video_name = 'videoplayback.mp4'
    video_path = './videos/' + video_name
    dump_path  = './videos/0_' + video_name
    time_len = '00:04:30'
    main_func(video_path, time_len, dump_path)