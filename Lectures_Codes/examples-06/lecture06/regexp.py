#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: regular expression example of search, match, escape, findall, split. Direct and compiled usage.
import re

# Match start of the string
match = re.match(".*pattern", "input to be matched for pattern at its beginning")
print(f"Pattern matched at {match.span()}, match is \"{match.group()}\".")

# Match anywhere in string
match = re.search("string", "some random string to be searched by patter string")
print(f"Pattern matched at {match.span()}, match is \"{match.group()}\".")

# Test match for success
if re.search("pqr", "abcdefghijklmnopqrstuvwxyz"):
    print("Match found !!!")
else:
    print("No match")

# Use expression to split the text
split = re.split(",| |;|-|:|\.|/|\\\\", "some,text that;needs-to be:split.by/multiple\patterns")
for s in split:
    print(f"split part: \"{s}\"")

# Match multiple occurrences easily
print(re.findall("[^ ]+", "Some sentence in which we would like to find all words"))

# Escaping control characters, search for ((*)) occurrences
print(re.search("\(\(\*\)\)", "aaaaa ((*)) bbbbb").group())

# Manual escaping is sometimes inconvenient or not possible at all
search_for = "((*))"
escaped = re.escape(search_for)
print(re.search(escaped, "aaaaa ((*)) bbbbb").group())

# Compile regular expression to optimize performance
# Standard calls are compiled on fly and cached for later use, so this is not
# necessary in most cases.
up_case_word_with_underscores = re.compile("[A-Z_]+")
print(up_case_word_with_underscores.match("UPCASE lowcase UP_CASE").group())
print(up_case_word_with_underscores.findall("lowcase UPCASE lowcase UP_CASE"))

# Use expression for substitution
print(re.sub(" +", "_", "Replace  spaces       in text  with   underscores. Contract multiple spaces to one."))

# Referencing matched groups
string = "random text, name: John, surname: Doe, random text"
match = re.search(".*name: (.*),.*surname: (.*),.*", string)
print(f"First matched group: {match.group(1)}")
print(f"Matched groups: {match.groups()}")

# Referencing matched groups by name
match = re.search(".*name: (?P<first>.*),.*surname: (?P<last>.*),.*", string)
print(f"First name: {match.group('first')}")
print(f"Groups as dictionary: {match.groupdict()}")
