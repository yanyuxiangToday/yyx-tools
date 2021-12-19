# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''

import os
import cv2

def get_video_info(videoPath):
    '''
    this func get and print video info using cv2
    :param videoPath: path to video
    :return: fps, total frames, image width, image height
    '''

    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frameCnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('info fps {:^9}, frameCnt {:^9}, width {:^5}, height {:^5}, time len {:0>2d}:{:0>2d}:{:0>2d}'.format(fps, frameCnt, width, height, int((frameCnt / fps) // 3600), int(((frameCnt / fps) % 3600 ) // 60), int(((frameCnt / fps) % 3600) % 60)))
    return fps, frameCnt, width, height

def extract_frames(videoPath, dumpDir, ffmpeg, minResize):
    '''
    this func extract frames from videoPath and dump to dumpDir
    :param videoPath:
    :param dumpDir:
    :param ffmpeg:
    :param minResize:
    :return: None
    '''

    # get video info
    fps, frameCnt, width, height = get_video_info(videoPath)

    # create a folder using video name under dumpPath
    dumpPath = os.path.join(dumpDir, '{}'.format(videoPath.split('/')[-1].split('.')[0]))
    if os.path.isdir(dumpPath):
        if len(os.listdir(dumpPath)) == frameCnt:
            print('this has been extract frames already, not repeat')
            return
    else:
        os.makedirs(dumpPath)

    # image name template
    imageNameTemplate = '%07d.png'
    dumpTo = os.path.join(dumpPath, imageNameTemplate)

    # if resize or not
    if minResize:
        if width <= height:
            rate = float(width) / float(minResize)
            resizeWidth = minResize
            resizeHeight = int(height / rate)
        else:
            rate = float(height) / float(minResize)
            resizeWidth = int(width / rate)
            resizeHeight = minResize
    else:
        resizeWidth = width
        resizeHeight = height

    # print cmd and call cmd
    cmd = '{} -i "{}" -q:v 2 -f image2 -vsync 0 -y -s {}*{} "{}"'.format(ffmpeg, videoPath, resizeWidth, resizeHeight, dumpTo)
    print(cmd)
    os.system(cmd)
    assert len(os.listdir(dumpPath)) == frameCnt

    return

def main(videoDirPath, framesDumpDir, minResize):
    '''

    :param videoDirPath: where to load video
    :param framesDumpDir: where to dump png
    :param minResize: if you need resize, give this param. else None
    :return: None; we will extract frames at func: extractFrames
    '''

    # get video list
    videoNames = os.listdir(videoDirPath)
    if '.DS_Store' in videoNames:
        videoNames.remove('.DS_Store')

    # ffmpeg cmd
    ffmpeg = 'ffmpeg'

    # extract frames one by one
    for singleVideoName in videoNames:
        singleVideoPath = os.path.join(videoDirPath, singleVideoName)
        try:
            print('\n----------------------------------------------------------------------------------------------------')
            print('now extract video: {}'.format(singleVideoPath))
            extract_frames(singleVideoPath, framesDumpDir, ffmpeg, minResize)
            print('done')
        except:
            raise Exception('cant extract frames from path {}, please check your path'.format(singleVideoPath))
    return


if __name__ == '__main__':
    # path to video folder
    video_dir = 'path/to/video/dir'

    # path to dump frame folder
    dump_dir = 'path/to/dump'

    # if you need resize image
    min_resize = None

    # go
    main(video_dir, dump_dir, min_resize)
