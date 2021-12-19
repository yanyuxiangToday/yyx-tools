# -*- coding: utf-8 -*-
'''
@Time    : /
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: /
@Software: PyCharm
'''


import pickle

testpkl = pickle.loads(open("NONLOCAL.pdparams", "rb").read())
pickle.dump(testpkl, open("NONLOCAL.pdparams_new","wb"), protocol=2)