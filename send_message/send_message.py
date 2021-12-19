# -*- coding: utf-8 -*-
'''
@Time    : 2021/8/30
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: send_message.py
@Software: PyCharm
'''


import itchat

def main():
    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    # itchat.send('这是来自python程序的一条消息', toUserName='filehelper')
    return


if __name__ == '__main__':
    main()
