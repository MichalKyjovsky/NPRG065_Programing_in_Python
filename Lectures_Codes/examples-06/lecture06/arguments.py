#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: Argument parsing example
from argparse import ArgumentParser

parser = ArgumentParser(description='Sample argument parsing program.')

# Add positional argument
parser.add_argument("foo", type=str,
                    default="Default foo value",
                    help="provide some string as foo argument")
# Type is checked amd mismatch results in exception. Help is used in
# auto-generated help.

# Add optional argument
parser.add_argument("-b", "--bar", type=int,
                    default=123, help="Provide value for optional numeric bar argument")

# Add required arguments
parser.add_argument("--required", required=True, action="store_true",
                    help="This argument must be passed")

# Add boolean argument
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Specify to make output more verbose")

# Add counted argument
parser.add_argument("-o", "--one-more", action="count", default=0,
                    help="Define number by passing this argument multiple times")
# It may be good idea to provide default=0 as None is default count it value
# is not provided.

# Add appended argument
parser.add_argument("-a", "--accumulate", action="append",
                    help="Provide multiple values that will be combined into a list")

# Add multi argument
parser.add_argument("-d", "--double", nargs=2,
                    help="Provide 2 values to this argument")
# Note: nargs can be set to '*', then any number of arguments is accepted
# Note: nargs can be set to '+', then any positive number of arguments is accepted

# Add choice argument
parser.add_argument("--choice", choices=["yes", "no"], required=True,
                    help="Choose \"yes\" or \"no\"")

# Example usage
args = parser.parse_args("FOO_VAL --bar 888 --required --verbose -o --one-more -o -o --accumulate a -a b -a c --double x y --choice yes".split())

# Real usage, parse program arguments
# args = parser.parse_args()

print("Parsed arguments:")
for arg in vars(args):
    print(f"{arg}: {getattr(args, arg)}")
