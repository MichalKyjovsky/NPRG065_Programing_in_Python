#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: os interface, file related api
import os
import stat

print("\n### Current working directory")
cwd = os.getcwd()
print(f"Current working directory is \"{os.getcwd()}\"")
print("Going one level up")
os.chdir("../")
print(f"Current working directory is \"{os.getcwd()}\"")
print("Resetting to original value")
os.chdir(cwd)
print(f"Current working directory is \"{os.getcwd()}\"")


print("\n### Links")
print("Create hardlink to source code of this script")
# May not work on windows
# os.link(__file__, "hardlink")


print("Create symlink to source code of this script")
# May not work on windows
# os.symlink(__file__, "symlink")


print("\n### List directory")
print(os.listdir("../"))


print("\n### Stat file")
print(os.stat(__file__))


print("\n### File manipulation")
print("Make directory foo")
os.mkdir("foo")


print("Make directory recursive")
os.makedirs("foo/bar")


print("Rename file or directory")
os.rename("foo", "bar")
os.renames("bar", "foo")  # Create directory structure first


print("Delete file or directory")
try:
    os.remove("symlink")
except FileNotFoundError:
    pass
try:
    os.remove("hardlink")
except FileNotFoundError:
    pass

os.rmdir("foo/bar")  # Remove one directory
os.removedirs("foo")  # Recursive


print("List directory content")
for item in os.listdir("."):
    print(item)


print("List directory content")
for item in os.scandir("."):
    print(f"{item.name} {item.path} {item.stat()}")


print("List directory content")
for dir_path, dir_names, file_names in os.walk("../"):
    print(f"Path: {dir_path}")
    print(f"Dirs: {dir_names}")
    print(f"Files: {file_names}")
