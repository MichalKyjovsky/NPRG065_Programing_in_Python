#! /usr/bin/env Python3

def permutation(prefix: str, string: str):
    if len(string) == 1:
        print(prefix + string)
    else:
        for i in range(len(string)):
            pom = string[i]
            permutation(prefix + pom, string[:i] + string[i + 1:])


permutation('', 'abcd')
