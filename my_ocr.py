#!/bin/env python2
from __future__ import unicode_literals
from __future__ import print_function

import sh
import sys, os.path, os

if __name__ == '__main__':
    pgm1 = '/tmp/' + sys.argv[1] + '.pgm'
    pgm2 = '/tmp/' + sys.argv[1] + '_2.pgm'
    txt = sys.argv[1]

    if os.path.exists(pgm1):
        os.remove(pgm1)

    if os.path.exists(pgm2):
        os.remove(pgm2)

    if os.path.exists(txt+'.txt'):
        os.remove(txt+'.txt')

    print('Converting the {0} into pgm...'.format(sys.argv[1]))
    sh.convert(sys.argv[1], pgm1)

    print('Unpaper the {0} to {1}'.format(pgm1,pgm2))
    sh.unpaper(pgm1, pgm2)
    
    print('tesseract -l chi_sim {0} {1} ~/.tesseract/config'.format(pgm2,txt))
    print(sh.tesseract('-l','chi_sim',pgm2,txt,'~/.tesseract/config'))

