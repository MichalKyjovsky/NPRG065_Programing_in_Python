'''
Assignment: Create a function that given a string computes frequency of every single character a-z.
(The case is ignored.). Create a morse-like code based on the computed frequencies.
Print out a histogram of the frequencies along with the computed morse-like code.

Sample output:
a --->   -- ( 8.095%): *************************************************************************
b ---> ...- ( 1.640%): ***************
c --->  -.- ( 4.365%): ***************************************
d --->  --. ( 3.222%): *****************************
e --->    . (11.120%): ****************************************************************************************************
f ---> .-.. ( 0.982%): *********
g ---> ..-- ( 1.074%): **********
h ---> .-.- ( 0.543%): *****
i --->    - (10.681%): ************************************************************************************************
j ---> .--- ( 0.081%): *
k ---> -... ( 0.000%):
l --->  ... ( 5.924%): *****************************************************
m --->  .-- ( 4.734%): *******************************************
n --->  .-. ( 5.762%): ****************************************************
o --->  -.. ( 4.457%): ****************************************
p --->  --- ( 2.402%): **********************
q ---> ..-. ( 1.247%): ***********
r --->  ..- ( 5.878%): *****************************************************
s --->   -. ( 8.291%): ***************************************************************************
t --->   .- ( 8.568%): *****************************************************************************
u --->   .. ( 9.042%): *********************************************************************************
v ---> .... ( 1.686%): ***************
w ---> -..- ( 0.000%):
x ---> .--. ( 0.208%): **
y ---> -.-. ( 0.000%):
'''


def list_max(lst):
    """
    Finds an item in a list that has a maximal value. Returns the index of the item and the value. It ignores items
    that have value None. If the list is empty or contains only None items, it returns None, None.
    :param lst: List to search
    :return: Pair of index (starting from 0) and the value. If no maximum was found, returns None, None
    """
    max_idx = None
    max_val = None
    idx = 0
    for idx, val in enumerate(lst):
        if val is not None and (max_val is None or max_val < val):
            max_idx = idx
            max_val = val

    return max_idx, max_val


a_ord = ord('a')
z_ord = ord('z')
alpha_count = z_ord - a_ord


def compute_frequencies(input_str):
    """
    Computes frequencies of English characters a-z (26 characters in total). Ignores the case -- i.e. counts both "a" and "A"
    as an occurence of "a"
    :param input_str: Input string
    :return: Array of 26 frequencies corresponding (in order) to letters "a".."z". The frequency is a floating number
    0..1. If the input string contains any letters "a".."z", the sum of the array is 1.
    """
    freqs = [0] * alpha_count
    total = 0

    lc_str = input_str.lower()

    for ch in lc_str:
        ch_ord = ord(ch)
        if ch_ord >= a_ord and ch_ord <= z_ord:
            freqs[ch_ord - a_ord] += 1
            total += 1

    for idx in range(alpha_count):
        freqs[idx] = freqs[idx] / total

    return freqs


def compute_morse_like_code(freqs):
    """
    Given an array of frequencies, computes morse-like symbols for letters "a".."z". The assignment of symbols follows
    the rule that a less frequent letter cannot have a shorter symbol than a more frequent letter.
    :param freqs: Array of frequencies as returned by compute_frequencies
    :return: Array of 26 morse-like symbols corresponding (in order) to letters "a".."z".
    """
    symbol = '.'

    def get_next_symbol():
        """
        Returns a morse-like symbol that follows the symbol stored in "symbol" variable. It generates symbols in the following
        order: ., -, ..,  .-,  -.,  --, ..., ..-, .-., .--, etc.
        :return:
        """
        new_symbol = ''
        for idx in range(len(symbol) - 1, -1, -1):
            if symbol[idx] == '.':
                new_symbol = symbol[0:idx] + '-' + new_symbol
                break
            else:
                new_symbol = '.' + new_symbol
        else:
            new_symbol = '.' + new_symbol

        return new_symbol

    morse_code = [0] * alpha_count

    # Iterate through the frequencies in descending order.
    # NOTE that the solution below is sub-optimal. It might be better to sort the array first and then traverse it.
    # However, we do it here in a sub-optimal way to practice the construct we learned so far.
    freqs = list(freqs)  # make a copy of freqs because we are going to modify it as part of the loop below

    max_idx, _ = list_max(freqs)
    while max_idx is not None:
        freqs[max_idx] = None
        morse_code[max_idx] = symbol
        symbol = get_next_symbol()

        max_idx, _ = list_max(freqs)

    return morse_code


def print_morse_code_with_histogram(freqs, morse_code):
    _, max_freq = list_max(freqs)

    idx = 0
    while idx < alpha_count:
        stars = '*' * round(freqs[idx] / max_freq * 100)
        print(f'{chr(idx + a_ord)} ---> {morse_code[idx]:>4} ({freqs[idx] * 100:6.3f}%): {stars}')
        idx += 1


sample_text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ac enim nec felis euismod placerat eu ac quam. Aliquam posuere at elit accumsan tristique. Praesent sed volutpat mauris, nec sodales lacus. In a sapien urna. Aliquam erat volutpat. Aliquam eget erat vel diam ultricies consequat. Etiam orci sapien, lobortis ac laoreet eget, aliquet ac eros. Suspendisse varius vitae nisi vel rutrum. Curabitur luctus auctor ex, quis euismod massa scelerisque ac. Praesent rhoncus mollis est. Proin vel tincidunt enim. Nulla egestas, dolor sit amet sollicitudin ullamcorper, nunc nunc aliquet mauris, vel sodales ipsum ante vel nulla. Proin vitae dui pulvinar, consequat odio ac, sollicitudin erat. Sed auctor scelerisque lacus quis ornare. Praesent faucibus est turpis, vitae efficitur libero pharetra et. Nunc sed sodales magna. Donec iaculis metus vestibulum metus lobortis aliquam. Maecenas egestas nisi vitae nunc mollis, a eleifend nulla iaculis. Quisque viverra dui sit amet ligula vulputate placerat a eget libero. Sed pulvinar ipsum quis ante volutpat facilisis vel at nisl. Vestibulum in nisi sit amet lorem imperdiet mollis eget a nibh. Aliquam faucibus tincidunt elit at dapibus. Quisque id faucibus ligula. Duis at nunc at nulla volutpat interdum. Morbi sit amet lorem a dui aliquet finibus. Vestibulum ut eros magna. In vel hendrerit sapien. Morbi rutrum ligula eu porttitor congue. Vestibulum purus libero, viverra nec erat sit amet, faucibus dictum magna. Cras ultrices mattis risus vel rutrum. Curabitur sit amet mollis lectus. Quisque imperdiet nibh eget lacus pretium, in tempor nibh mattis. Etiam rutrum quam quis leo molestie, vitae iaculis justo elementum. Integer aliquet, tortor eget aliquet dictum, elit ex efficitur tellus, elementum rutrum ante elit quis dolor. Nunc ac tortor tincidunt, aliquet mauris sit amet, vestibulum ex. Maecenas faucibus, nibh at luctus porta, ante ex blandit lacus, eget dignissim massa eros ut est. Integer vulputate dignissim magna. Vestibulum euismod arcu non laoreet elementum. Praesent feugiat eget orci vel semper. Donec hendrerit facilisis arcu id suscipit. Sed ut lacus sit amet odio faucibus mattis semper ac quam. Fusce efficitur turpis quis nulla volutpat, vel tristique felis bibendum. Sed in ligula tempor, finibus nisi iaculis, blandit nunc. Curabitur vulputate volutpat lacus a varius. Aenean eget malesuada risus.
Donec tellus libero, dapibus quis ornare ac, interdum sit amet ex. Nulla auctor maximus ex, nec dapibus augue feugiat vel. Nam quis tempor leo, nec ultricies tellus. Nullam eget purus libero. Maecenas egestas tellus non pharetra vestibulum. Nunc dictum eu purus cursus sodales. Phasellus eget rhoncus velit. Fusce vestibulum purus velit, in pulvinar velit interdum in. Aliquam facilisis dictum quam eget dapibus. Duis vel odio varius, rhoncus dolor ac, ultricies diam. Sed aliquam ipsum ac ex auctor porttitor. Duis ut metus sed turpis dictum dignissim varius at augue. Pellentesque gravida, purus et rutrum pretium, quam tortor laoreet orci, et dictum enim orci sit amet lorem. Donec sed sapien condimentum, imperdiet diam a, ultricies velit. Vivamus a eros risus. Donec ac ex nunc. Sed consequat rhoncus felis id dictum. Quisque placerat bibendum augue, blandit cursus nisi rutrum id. Curabitur sollicitudin aliquam egestas. Donec ac varius nulla. Curabitur ac tellus ex. Phasellus interdum tincidunt ultrices. Nunc ac eros sagittis, hendrerit mauris nec, lacinia quam. In eros mauris, scelerisque faucibus nulla ut, varius iaculis orci. Nulla lectus lorem, tempor ut placerat eu, pretium id nisi. Aenean quis nunc ut ex luctus ornare sed et nulla. Integer molestie tellus massa, id tincidunt ante lacinia ut. Integer tempus finibus tempus. Etiam purus risus, luctus at elit vitae, scelerisque condimentum turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent dapibus sagittis finibus. Mauris elit mi, egestas ut euismod placerat, sodales quis augue. Ut eu arcu sed justo laoreet pretium. Mauris eget blandit orci. Morbi bibendum enim eu malesuada finibus. Vivamus quis laoreet metus, et ullamcorper massa. Ut finibus ornare rutrum.
Fusce eget pulvinar tellus, sed facilisis diam. In sem nulla, aliquet ut turpis sit amet, imperdiet placerat nibh. Fusce in ornare lorem. Etiam ut aliquet nisi, quis interdum quam. Vivamus mattis consectetur massa id suscipit. Proin efficitur et ante a vulputate. Integer molestie sodales malesuada. Praesent convallis elementum ipsum at imperdiet. Nulla in sagittis eros. Morbi ut porttitor libero. Aliquam scelerisque erat tellus, a maximus eros hendrerit nec. In eleifend laoreet tellus sed posuere. Sed ut pellentesque felis, egestas rhoncus dolor. Duis ac leo tincidunt, ornare ipsum vitae, lobortis est. Aliquam imperdiet felis ac sem facilisis pharetra. Maecenas commodo arcu dolor, id vestibulum dolor vulputate nec. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer lacinia lacus at nunc porttitor ultrices vel a mauris. Aliquam pulvinar interdum accumsan. Sed posuere lorem a velit bibendum varius. Aliquam nec leo ultricies elit condimentum vestibulum et nec sem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi ornare libero posuere mauris commodo porttitor quis tincidunt sapien. Praesent in purus leo. Ut dictum rhoncus malesuada. Etiam congue id metus eget volutpat. Praesent libero tortor, efficitur mattis tincidunt sit amet, aliquet a arcu. Vestibulum sed nisi nec metus vestibulum faucibus. Proin sodales lobortis sapien sed condimentum. Phasellus hendrerit rhoncus sem, et scelerisque dolor fermentum eget. Praesent vel ullamcorper lorem, sit amet dictum purus. Quisque varius, quam sit amet sagittis porttitor, augue nibh egestas justo, vitae varius nisi mauris id elit. Phasellus nec ante commodo, efficitur metus et, posuere libero. Sed aliquet posuere accumsan. Maecenas cursus, eros eu sodales dignissim, dolor massa pharetra risus, ac tempus turpis dui a ex. Morbi sit amet justo vitae odio ultricies tincidunt. Nunc imperdiet mauris vel tellus laoreet, ac vehicula turpis aliquet. Proin viverra convallis quam non iaculis. In hac habitasse platea dictumst. Praesent aliquet urna eu viverra fermentum. Donec et justo laoreet justo ultrices consectetur. In lacinia enim tellus, ut laoreet nisi mattis sed.
Etiam at ipsum felis. Cras maximus fringilla viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed sit amet lacinia lacus. In id arcu vitae lectus aliquet euismod non non ipsum. Phasellus nulla sapien, pharetra nec lectus at, rhoncus tristique eros. Curabitur hendrerit consectetur lacus vitae viverra. Donec bibendum vulputate pharetra. Sed pellentesque convallis orci et ultricies. Etiam faucibus ultricies dignissim. Vestibulum condimentum ex eget magna ultricies, condimentum finibus nibh laoreet. Nunc ac imperdiet leo, sit amet dictum turpis. Quisque convallis urna eget sollicitudin lobortis. Vestibulum leo lorem, egestas eu enim non, convallis fringilla velit. Nam in urna dui. Suspendisse potenti. Duis non dui non orci consectetur mollis nec pulvinar dolor. Pellentesque fermentum ultricies velit eget commodo. Praesent condimentum vehicula commodo. Sed sit amet porta est, eu dapibus dolor. Morbi id mauris odio. Sed molestie ut odio eu tincidunt. Nulla facilisi. Vestibulum tempus tempus libero sit amet venenatis. Maecenas id lorem id arcu venenatis suscipit ac varius tortor. Morbi non risus egestas eros posuere blandit vel vitae felis. Phasellus sollicitudin, turpis faucibus laoreet euismod, arcu felis mattis risus, quis varius diam dui ut nulla. Ut lacus enim, feugiat ac feugiat et, elementum nec nisl. Curabitur lobortis neque quam, et commodo orci faucibus vitae. Nam imperdiet justo ac lacus venenatis porttitor. Donec lobortis nunc id vehicula vestibulum. Cras eu dui massa. Praesent nisl felis, maximus sit amet turpis in, tincidunt ullamcorper lorem. In quis neque id libero porttitor convallis. Praesent nec ligula id risus venenatis gravida. Nulla tempus sapien neque, id aliquet lacus interdum sed. Integer sed nulla sagittis, sagittis sapien in, tincidunt leo. Nam sit amet mattis leo. Maecenas porttitor diam eu vestibulum bibendum.
Phasellus a tempus nisl. Curabitur interdum gravida elit id volutpat. Curabitur vitae pulvinar lacus. Nulla ac arcu imperdiet, bibendum urna et, commodo dolor. Sed scelerisque a eros id convallis. Fusce eu ultrices enim. Nunc finibus molestie lacus, non eleifend dui molestie eget. Ut vitae ligula non odio pellentesque egestas a sit amet orci. Nulla sem ante, accumsan nec placerat nec, pretium vel urna. Aenean ut blandit nibh. Aliquam tincidunt dapibus dui in mollis. Morbi id sollicitudin dui, ac congue velit. Vivamus vitae dui a nibh tincidunt placerat sed sit amet felis. Sed ultricies dui ac velit ornare, sit amet finibus urna porta. Donec porttitor ipsum urna, sit amet varius tellus blandit a. In vitae neque posuere, pellentesque lorem at, semper purus. Suspendisse id lorem egestas, malesuada diam quis, iaculis velit. Nam lacinia in dolor id cursus. Donec ultricies volutpat congue. Morbi a odio ac risus condimentum aliquet. Duis faucibus lectus lectus, ac consequat urna aliquam sit amet. Morbi ut euismod libero. Proin condimentum tellus suscipit dolor bibendum, et rutrum orci suscipit. In vestibulum rutrum tellus, in ultricies orci euismod consectetur. Aliquam a diam efficitur, commodo ipsum bibendum, pulvinar velit. Vivamus pretium pharetra velit at porttitor. Pellentesque tristique bibendum enim, ac dignissim turpis faucibus ut. In vulputate turpis eget orci ultricies porta. Nam ac ex magna. Donec pellentesque convallis varius. Curabitur aliquam, massa eget luctus sollicitudin, magna sem venenatis mauris, sit amet maximus dolor neque dapibus orci. Proin finibus feugiat placerat. Maecenas malesuada felis lectus, non auctor libero fermentum aliquet. Pellentesque facilisis enim sem, sit amet viverra nunc suscipit non. Nam tincidunt interdum eleifend. Nulla dapibus, mi vel tincidunt semper, nulla leo accumsan sem, ornare efficitur tellus nunc a dolor. Duis hendrerit velit id libero fringilla, eget molestie mi euismod. Sed condimentum diam at mauris bibendum scelerisque. Curabitur ac metus condimentum, consequat dui a, lobortis sapien. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur magna nisl, finibus quis feugiat eget, facilisis nec odio. Duis in eros rhoncus arcu condimentum tincidunt sed id mauris.
"""

freqs = compute_frequencies(sample_text)

morse_code = compute_morse_like_code(freqs)

print_morse_code_with_histogram(freqs, morse_code)
