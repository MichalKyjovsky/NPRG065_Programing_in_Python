from sys import argv


def convert_text(input_file, mode):
    with open(input_file, mode='rt') as file:
        lines = file.readlines()
        if mode == '-U':
            for line in lines:
                print(line.upper(), end='')
            print()
        elif mode == '-L':
            for line in lines:
                print(line.lower(), end='')
            print()


convert_text(argv[2], argv[1])
