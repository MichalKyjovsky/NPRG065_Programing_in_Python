#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FEATURES: JSON read example
import json

# Open JSON source file
with open("sample.json") as file:
    # Parse configuration
    config = json.load(file)

    # Access whole document
    print(config)

    # Access particular options
    print(config['connection']['server'])
    print(config['options']['components'])


# Load JSON from string
config = json.loads('{"letters":["a","b","c"]}')
print(config)
