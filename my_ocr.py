#!/bin/env python2
from __future__ import unicode_literals
from __future__ import print_function

import sh
import sys, os.path, os

def med_ocr(filename, 
        tessconf = '~/.tesseract/config', 
        unpaper = False):
    pgm1 = '/tmp/' + filename + '.pgm'
    pgm2 = '/tmp/' + sys.argv[1] + '_2.pgm'
    txt = filename

    if os.path.exists(pgm1):
        os.remove(pgm1)

    if os.path.exists(pgm2):
        os.remove(pgm2)

    if os.path.exists(txt+'.txt'):
        os.remove(txt+'.txt')
    if unpaper:
        print('Converting the {0} into pgm...'.format(sys.argv[1]))
        sh.convert(sys.argv[1], pgm1)

        print('Unpaper the {0} to {1}'.format(pgm1,pgm2))
        sh.unpaper(pgm1, pgm2)
    
        print('tesseract -l chi_sim {0} {1} {2}'.format(pgm2,
            txt,tessconf))
        print(sh.tesseract('-l','chi_sim',pgm2,txt,
            tessconf))
    else:
        print('tesseract -l chi_sim {0} {1} {2}'.format(pgm2,
            txt,tessconf))
        sh.tesseract('-l', 'chi_sim', filename, txt, tessconf)
    
    return txt + '.txt'

if __name__ == '__main__':
    med_ocr(sys.argv[1]) 

