# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals

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

def get_test_value(line, num=0, pattern=re.compile('[\d\.]+'),totalnum=3):
    '''get the test value of the specific line.
    num is which digits is the value.
    pattern is a compiled regex for search the digits'''
    
    result = pattern.findall(line)
    
    LEN = len(result)
    
    if LEN > 3:
        for k, item in enumerate(result):
            if item.endswith('.') and k< LEN-1:
                result[k] = result[k] + result[k+1]
                result.pop(k+1)
            
    if len(result) == 3:
        return float(result[num])
    else:
        return result[num]

def post_proc(txtin):
    db = MedDB()
    with open(txtin) as f:
        txt_lines = f.readlines()

    blank_line = re.compile('^ *$')
    blanks = re.compile(' +')
    digits_pat = re.compile('[\d\.]+')

    result = {}
    
    for k, line in enumerate(txt_lines):
        if blank_line.match(line):
            continue
        words = line.decode('utf-8').split(' ')

        words_matched = False
        words_part_matched = False

        for word in words:
            if test_name_search(word):
                words_matched = True
                result[word] = get_test_value(line)
                print('Bingo! No.{0} : {1}'.format(k, word))
                break

    return result
'''
        if not words_matched:
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
                print('parted Bingo No.{0}: {1}'.format(k,' '.join(candi_words)))                '''
                
    
if __name__ == '__main__':
    result = post_proc('/home/lxq/python/cq-med/temp/OCR/image2.txt')
    for k, v in result.iteritems():
        print(k, v)
