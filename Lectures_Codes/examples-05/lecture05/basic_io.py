#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from getpass import getpass

# Let's open a file for reading and print it to stdout
with open('basic_io.py') as f:
    read_data = f.read()
    print('-- BEGINNING OF FILE --')
    print(read_data)
    print('-- END OF FILE --')

print(f'{f.name} is {"closed" if f.closed else "opened"}')


# The above code reads all the file content to the memory, but we do not need it.
# The file object support iteration over lines.
with open('basic_io.py') as f:
    print('-- BEGINNING OF FILE --')
    for line in f:
        print(line, end='')      # WARNING: line is returned with the new-line character
    print('-- END OF FILE --')


# Let's open two files and copy the content. Second file is opened for writing (see its mode).
with open('basic_io.py') as fin, open('tmp/copy_basic_io.py', mode='w') as fout:
    read_data = fin.read()
    fout.write(read_data)


# For writing to a textual file, we can use print
with open('tmp/formatted.txt', mode='w') as fout:
    for var in range(100):
        print(f'int: {var:2d};  hex: {var:2x};  oct: {var:3o};  bin: {var:7b}', file=fout)


# We can write data that are read from the user
with open('tmp/read_from_user.txt', mode='w') as fout:
    print('Provide login names and passwords for users')
    while True:
        name = input('User name (type <Enter> to finish): ')
        if name == '':
            break
        # WARNING: getpass() cannot work properly in IDE
        #          To test getpass(), uncomment the following line, comment the next one and run the script outside IDE
        # passwd = getpass('User password: ')
        passwd = input('User password: ')
        print(f'{name} {passwd}', file=fout)
