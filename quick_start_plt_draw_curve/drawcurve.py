# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''


# load pkg
import matplotlib.pyplot as plt

def drawCurve(txt_path):
    # open file
    with open(txt_path, 'r') as res_txt:

        # read file and save lines to var lines
        lines = res_txt.readlines()

        # ready to draw curve
        epoch_list, corr_list, score_list, position_list, armstand_list, rot_list, ss_list, tw_list = [], [], [], [], [], [], [], []

        # loop each line
        for line in lines:
            # remove blank at start and end
            line = line.strip()

            # split line by blank
            sp = line.split()

            # comput values and save to list
            epoch, corr, score, position, armstand, rot, ss, tw =\
                int(sp[1]), float(sp[7][:-1]) * 100, float(sp[10][1:-2]) * 100, float(sp[12][:-1]), float(sp[14][:-1]), float(sp[16][:-1]), float(sp[18][:-1]), float(sp[20][:-1])
            epoch_list.append(epoch)
            corr_list.append(corr)
            score_list.append(score)
            position_list.append(position)
            armstand_list.append(armstand)
            rot_list.append(rot)
            ss_list.append(ss)
            tw_list.append(tw)

        # show each list at console
        print(corr_list)
        print(score_list)
        print(position_list)
        print(armstand_list)
        print(rot_list)
        print(ss_list)
        print(tw_list)

    # file
    lr_list = []
    for epoch in epoch_list:
        if epoch < 70:
            lr_list.append(1e-4)
        elif epoch < 80:
            lr_list.append(1e-4 * 0.5)
        elif epoch < 90:
            lr_list.append(1e-4 * 0.5**2)
        else:
            lr_list.append(1e-4 * 0.5**3)

    # ready to draw
    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.plot(epoch_list, lr_list, color='red', label='lr')
    plt.legend()

    # ready curves
    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(epoch_list, corr_list, color='chartreuse', label='corr')
    ax2.plot(epoch_list, score_list, color='orange', label='score')
    ax2.plot(epoch_list, position_list, color='green', label='position')
    ax2.plot(epoch_list, armstand_list, color='blue', label='armstand')
    ax2.plot(epoch_list, rot_list, color='indigo', label='rot')
    ax2.plot(epoch_list, ss_list, color='violet', label='ss')
    ax2.plot(epoch_list, tw_list, color='brown', label='tw')
    plt.legend()

    # show
    plt.show()
    return

if __name__ == '__main__':
    # where to load txt
    txt_path = 'result/nonlocal_size112x112_fc2048x1024_clip8_batch6_bn_lr1e-4/result.txt'
    drawCurve(txt_path)
