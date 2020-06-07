import sys
import re


def word_gen(file):
    """
    Generator of the words from the standard input
    :param file: file on the standard input
    """
    for line in file:
        for word in line.split(" "):
            yield word


def justify(input_file, line_length):
    """
    Method continuously adds word by word to the
    line while the actual length of the line is lesser
    or equal to the desired line_length provided as
    parameter. Once the line is filled or the length
    of the word is greater than or equal than desired
    lenght, function justify_white_spaces is called
    on particular line.
    :param input_file: Path to the file which is meant for justification.
    :param line_length: Lenth of the line to which are going to be lines
    justified.
    """
    line_buffer = []
    last_word_contained_new_line = False
    paragraph_splitting = False
    word_separator = " "

    for word in word_gen(input_file):
        word_stripped = word.strip()
        if word == '\n' and last_word_contained_new_line:
            paragraph_splitting = True
        elif not word_stripped:
            continue
        else:
            if last_word_contained_new_line and paragraph_splitting:
                if line_buffer:
                    print(word_separator.join(line_buffer))
                last_word_contained_new_line = False
                paragraph_splitting = False
                line_buffer.clear()
                print()
            if len(word_separator.join(line_buffer)) + len(word_stripped) + 1 <= line_length:
                line_buffer.append(word_stripped)
            elif len(word) >= line_length:
                justify_white_spaces(line_buffer, line_length)
                print(word_stripped)
                line_buffer.clear()
            else:
                justify_white_spaces(line_buffer, line_length)
                line_buffer.clear()
                line_buffer.append(word_stripped)

            if word.endswith('\n'):
                last_word_contained_new_line = True
                continue
    if line_buffer:
        print(word_separator.join(line_buffer))


def justify_white_spaces(line, line_length):
    """
    Method for dividing and insertion of white space
    in accordance to JUSTIFY logic and described requirements.
    :param line: Line for JUSTIFY process.
    :param line_length: Lenght of the line,
           to which line has to be justified.
    :return: Returns either void, in case there is a line
             for justification, it will print results immediately.
    """
    if len(line) == 1:
        print(line[0])
        return
    elif not line:
        return
    else:
        lenth_difference = line_length - len(" ".join(line))
        white_spaces_for_each_hole = lenth_difference // (len(line) - 1)
        white_spaces_for_reminder = lenth_difference % (len(line) - 1)
        common_spaces = [" " * (1 + white_spaces_for_each_hole)] * (len(line) - 1)

        common_spaces[:white_spaces_for_reminder] = [common_spaces[index] + " " for index in range(len(common_spaces))
                                                     if index < white_spaces_for_reminder]
        print("".join([word + separator for word, separator in zip(line, common_spaces)]) + line[-1])


def main():
    if re.fullmatch("[1-9]+[0-9]*", sys.argv[1]):
        justify(sys.stdin, int(sys.argv[1]))
    else:
        print("Error")


if __name__ == "__main__":
    main()
