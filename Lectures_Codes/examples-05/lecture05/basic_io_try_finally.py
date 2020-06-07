#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    f = open('basic_io.py')
    read_data = f.read()
    print('-- BEGINNING OF FILE --')
    print(read_data)
    print('-- END OF FILE --')
finally:
    try:
        f.close()
    except:
        pass
