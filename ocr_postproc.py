# -*- coding:utf8 -*-
from __future__ import unicode_literals

from misc.MedDBAPI import MedDB

import jieba
import re

def test_name_search(word, match = 'equal'):
    db = MedDB()
    if match == 'equal':
        return db.query(db.Jianchazhibiao.zhibiao_name).filter(db.Jianchazhibiao.zhibiao_name == word).all()

    elif match == 'like':
        result =db.query(db.Jianchazhibiao.zhibiao_name).filter(db.Jianchazhibiao.zhibiao_name.like('%{0}%'.format(word))).all()
        if result:
            return [x[0] for x in result]
        else:
            return result
    
    else:
        return None


def post_proc(txtin):
    db = MedDB()
    with open(txtin) as f:
        txt_lines = f.readlines()

    blank_line = re.compile('^ *$')
    blanks = re.compile(' +')

    for k, line in enumerate(txt_lines):
        if blank_line.match(line):
            continue
        words = line.decode('utf-8').split(' ')

        words_matched = False
        words_part_matched = False

        for word in words:
            if test_name_search(word):
                words_matched = True 
                print('Bingo! No.{0} : {1}'.format(k, word))
                break

        if words_matched:
            # delete the blanks and cut the words
            temp = blanks.sub('', line.decode('utf-8'))
            words = jieba.cut(temp)
            candi_words = set()

            for word in words:
                temp = test_name_search(word, match = 'like')
                if not temp:
                    continue
                words_part_matched = True
                 
                if not candi_words:
                    candi_words = set(temp)
                else:
                    candi_words = candi_words.intersection(set(temp))     
               
            if words_part_matched:
                print('parted Bingo No.{0}: {1}'.format(k,' '.join(candi_words)))                
                
    
if __name__ == '__main__':
    post_proc('/home/lxq/prog/python/cq-med/temp/OCR/image2.txt')
