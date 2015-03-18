# -*- coding:utf8 -*-
from __future__ import unicode_literals

from misc.MedDBAPI import MedDB

import jieba

#if __name__ == '__main__':

def post_proc(txtin, txtout):
    db = MedDB()
    with open(txtin) as f:
        txt_lines = f.readlines()
    for line in txt_lines:
        words = jieba.cut()
        for word in words:

