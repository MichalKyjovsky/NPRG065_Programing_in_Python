"""
 number_of_trees variable signs how many sub-trees are on the particular level
 e.g.
            *
           * *      one
          *   *
         * * * *    two
"""

def print_binary_tree(level: int):
    if level == 0:
        print()
    elif level == 1:
        print('*')
    else:
        print_sub_trees(level, 1)

def print_sub_trees(level: int, number_of_trees: int):
    if level > 2:
        for j in range (2 ** (level - 2)):
            print_tree_line(j, number_of_trees, level)

        print_sub_trees(level - 1, number_of_trees * 2)

    else:
        print_tree_line(0, number_of_trees, 2)
        print_tree_line(0, number_of_trees * 2, 1)

def print_tree_line(line_level: int, number_of_trees: int, level: int):
    for i in range(number_of_trees):
        if line_level == 0:
            print(( 2 ** (level - 1) - 1) * ' ', end='')
            print('*', end='')
            print((2 ** (level - 1)) * ' ', end='')
        else:
            print((2 ** (level - 1) - line_level - 1) * ' ', end='')
            print('*', end='')
            print((line_level * 2 -1) * ' ', end='')
            print('*', end='')
            print((2 ** (level - 1) - line_level) * ' ', end='')

    print()



print_binary_tree(4)