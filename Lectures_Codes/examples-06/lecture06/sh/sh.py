#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: shutils examples, mostly file copy
import shutil
import os

print("\nCopy data from one file descriptor to another one by chunks")
src_fd = open("src.data", "r")
dst_fd = open("out.data", "w")
shutil.copyfileobj(src_fd, dst_fd, length=32)

print("\nCopy file content without metadata")
shutil.copyfile("src.data", "out.nometadata")
print("After copyfile")
print(os.stat("src.data"))
print(os.stat("out.nometadata"))

print("\nCopy metadata from file to file")
shutil.copymode("src.data", "out.nometadata")
print("After copymode")
print(os.stat("src.data"))
print(os.stat("out.nometadata"))

print("\nCopy file status")
shutil.copystat("src.data", "out.nometadata")
print("After copystat")
print(os.stat("src.data"))
print(os.stat("out.nometadata"))

print("\nCopy file including permissions")
shutil.copy("src.data", "out.keeppermissions")
print("After copy")
print(os.stat("src.data"))
print(os.stat("out.keeppermissions"))

print("\nCopy file including permissions and other metadata")
# Some metadata can still be missed if not supported
shutil.copy2("src.data", "out.keepall")
print("After copy2")
print(os.stat("src.data"))
print(os.stat("out.keepall"))

print("\nCopy structure, ignore patterns")
ignore_pattern = shutil.ignore_patterns("foo")
try:
    shutil.copytree("src", "out", symlinks=True, ignore=ignore_pattern, copy_function=shutil.copy)
except FileExistsError as e:
    print("Destination already exists")

print("\nMove structure")
shutil.move("out", "move")

print("\nRemove tree")
shutil.rmtree("move")

print("\nDisk usage")
print(shutil.disk_usage("."))

print("\nSupported archive formats")
print(f"pack: {shutil.get_archive_formats()}")
print(f"unpack: {shutil.get_unpack_formats()}")

print("\nMake archive")
archive = shutil.make_archive("src", "zip", "src")
print(archive)

print("\nUnpack archive")
shutil.unpack_archive(archive, "out")
