from collections import Counter, defaultdict
from stats import print_histogram_2d

# This is a list of characters that are interpreted as punctuations and thus ignored.
punctuation_chars = ",;:.?!()[]<>/-'\""
trtrable = str.maketrans(punctuation_chars, " " * len(punctuation_chars))


def get_word_lengths(filename):
    '''
    Counts the number of occurrences of word lengths
    :param filename: Filename to process
    :return: Returns a Counter (i.e. dictionary of ints). They keys are integers representing different word lenghts. The values are number of occurences. E.g.:
        {
            1: 5,
            2: 4,
            4: 7
        }
    '''
    counter = Counter()

    with open(filename, 'rt') as fin:
        for line in fin:
            for word in line.translate(trtrable).split():
                counter[len(word)] += 1

    return counter


def get_word_lengths_multiple(filenames):
    '''
    Counts the number of occurrences of word lengths in multiple files
    :param filenames: List of files to process
    :return: Returns a dictionary of dictionaries. The top-level keys are integers representing different word lenghts. Second-level keys are filesnames. Values are number of occurences. E.g.:
        {
            1: {
                'filename1': 5,
                'filename2': 3
            },
            2: {
                'filename1': 4,
                'filename2': 6
            }
            4: {
                'filename1': 7,
                'filename2': 2
            }
        }
    '''
    output = defaultdict(dict)

    for filename in filenames:
        counts = get_word_lengths(filename)

        for key, count in counts.items():
            output[key][filename] = count

    return output


if __name__ == '__main__':
    import sys
    counts = get_word_lengths_multiple(sys.argv[1:])
    print_histogram_2d(counts)
