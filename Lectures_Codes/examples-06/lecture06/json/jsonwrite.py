#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: store JSON to file or string
import json


# Sample configuration data
class Config:
    def __init__(self):
        self.version = 1234
        self.tasks = ["load", "process", "store"]
        self.mapping = dict([(1, "a"), (2, "b")])


config = Config()

# Dump JSON as string
print(json.dumps(config.__dict__))

# Store JSON in file
with open("out.json", "w") as file:
    json.dump(config.__dict__, file)
