#!/usr/bin/env python3

# Example of printing out a multiplication table of a given number


def print_row(row_idx, size):
    """
    Prints out one row of the multiplication table. Aligns numbers to right.
    :param row_idx: Index of the row (starting from 0)
    :param size: Number of entries to print on the row
    """
    for col_idx in range(size):
        value = (col_idx + 1) * (row_idx + 1)
        print(f"{value:>5}", end="")


def print_multiplication_table(size):
    """
    Prints out a 2D multiplication table of given size.
    :param size: Number of rows/columns
    """
    for row_idx in range(size):
        print_row(row_idx, size)
        print()


print_multiplication_table(10)
