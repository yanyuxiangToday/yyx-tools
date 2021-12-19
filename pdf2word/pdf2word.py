# -*- coding: utf-8 -*-
"""
@Time    : 2021/9/8
@Author  : Yanyuxiang
@Email   : yanyuxiangtoday@163.com
@FileName: pdf2docx.py
@Software: PyCharm
"""

from pdf2docx import Converter, parse


def go1(pdf_file, docx_file):
    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

def go2(pdf_file, docx_file):
    # convert pdf to docx
    parse(pdf_file, docx_file)

if __name__ == '__main__':
    pdf_file = 'input.pdf'
    docx_file = 'output.docx'
    # go1(pdf_file, docx_file)
    go2(pdf_file, docx_file)
