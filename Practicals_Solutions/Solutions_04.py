def printfile(filename):
    """
    The function prints a textual file split by words, i.e. each word on the new line.
    The word separators are white characters (space, new line, tab,...).
    :param filename: The name of the input file
    """
    try:
        f = open(filename, mode='r')
    except:
        print('Error opening file ' + filename)
        return

    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            print(word)


def countwords(filename):
    """
    The function counts number of individual words in a given file.
    :param filename: The name of the file to be processed.
    :return: nothing
    """
    from string import punctuation

    with open(filename, mode='r') as f:
        counts = dict()
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                w = word.strip(punctuation)
                try:
                    counts[w] += 1
                except:
                    counts[w] = 1

        print(counts)


def wrapfile(filename, width, output=''):
    """
    The function prints a textual file aligned to a maximal given width (maximal number of characters on the line),
    i.e., the text is aligned to left.
    :param output: The filename to output to, if none is provided, stdout is used.
    :param filename: The name of the file to be processed.
    :param width: The desired width.
    """
    from sys import stdout
    from os import linesep

    if output == '':
        fout = stdout
    else:
        fout = open(output, 'wt')

    with open(filename, 'rt') as f:
        lines = f.readlines()
        current_length = 0
        for line in lines:
            words = line.split()
            if len(words) == 0:  # new paragraph
                print(linesep, file=fout)
                current_length = 0
            else:
                for word in words:
                    if current_length + len(word) + 1 > width:  # the current word does not fit any more
                        print(file=fout)
                        current_length = 0
                    else:
                        if current_length > 0:  # this is not the first word on the line, insert a space
                            print(' ', end='', file=fout)
                            current_length += 1

                    print(word, end='', file=fout)
                    current_length += len(word)


def adduser(login):
    """
    Adds a new user to 'passwd' file.
    :param login: the login of the added user
    :return: nothing
    """

    # constants to make the access more readable
    LOGIN = 0
    PASSWORD = 1
    UID = 2
    GUID = 3
    FULL_NAME = 4
    HOME_DIR = 5
    SHELL = 6

    with open('passwd', 'rt') as f:
        lines = f.readlines()

    # parse the passwd file into lists
    userinfo = [item.split(':') for item in lines]
    logins = [user[LOGIN] for user in userinfo]
    uids = [int(user[UID]) for user in userinfo]
    home_dirs = [user[HOME_DIR] for user in userinfo]

    # check the login
    if login in logins:
        print('The login {} is already used.'.format(login))
        return

    # Get and test UID
    newuid = max(uids) + 1  # The default value is the maximum UID already present + 1

    while True:
        uid = input('Enter a UID (default {}): '.format(newuid))
        if uid == '':
            uid = newuid
            break
        else:
            if int(uid) in uids:
                print('This UID is already used, please enter another one.')
            else:
                uid = int(uid)
                break

    full_name = input('Enter full name: ')

    # The homedir
    new_home_dir = '/home/' + login
    home_dir = input('Enter a home directory (default {}): '.format(new_home_dir))
    if home_dir == '':
        home_dir = new_home_dir

    # The shell
    new_shell = '/bin/bash'
    shell = input('Enter the shell (default {}): '.format(new_shell))
    if shell == '':
        shell = new_shell

    # Add the new record to passwd
    # We expect the file to
    with open('passwd', 'at') as f:  # open f for (a)ppending in the (t)ext mode
        from os import linesep
        f.write('{0}:x:{1}:1000:{2}:{3}:{4}'.format(login, uid, full_name, home_dir, shell) + linesep)

    print("User successfully added.")


# The main
# printfile('lipsum.txt')
# countwords('lipsum.txt')
wrapfile('lipsum.txt', 60, output='wrapped_file.txt')

from sys import argv
if len(argv) != 2:
    print('Exactly one argument with the login name to add is required.')
else:
    adduser(argv[1])