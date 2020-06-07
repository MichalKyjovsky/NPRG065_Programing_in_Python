#!/usr/bin/env python3

import sys

try:
    f = open(sys.argv[1], 'r')
except OSError as ex:
    print('cannot open', sys.argv[1])
    print(ex)
else:
    print('File has', len(f.readlines()), 'lines')
    f.close()
