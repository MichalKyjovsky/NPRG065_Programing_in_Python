#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: pathlib, explicit usage of windows/posix path, common path features
from pathlib import PurePosixPath
from pathlib import PureWindowsPath
from pathlib import Path

# It is possible to explicitly use either windows or posix path

win_path = PureWindowsPath("some", "windows", "path")
print(f"Windows Path: {win_path}")

posix_path = PurePosixPath("some", "posix", "path")
print(f"Posix Path: {posix_path}")

# Or use current native path

print("\nDirectory listing")
path = Path("..")
for p in path.iterdir():
    print(p)

print("\nNavigating")
path = Path(".")
path = path / ".." / "foo" / "bar"
print(path)

print("\nExpansion")
print(list(p.glob('../**/*.py')))

print("\nResolution")
path = Path(".").resolve()
print(path)

print("\nPath properties")
path = Path(__file__)
print(f"path: {path}")
print(f"drive: {path.drive}")
print(f"root: {path.root}")
print(f"anchor: {path.anchor}")
print(f"parent: {path.parent}")
print(f"parents: {[x for x in path.parents]}")
print(f"name: {path.name}")
print(f"suffix: {path.suffix}")
print(f"suffixes: {path.suffixes}")
print(f"stem: {path.stem}")
print(f"possix: {path.as_posix()}")
print(f"uri: {path.as_uri()}")
print(f"absolute: {path.is_absolute()}")
print(f"exists: {path.exists()}")
#print(f"owner: {path.owner()}")
#print(f"group: {path.group()}")
print(f"dir: {path.is_dir()}")
print(f"file: {path.is_file()}")
print(f"symlink: {path.is_symlink()}")

print("\nPredefined paths")
print(f"home: {Path.home()}")
print(f"working directory: {Path.cwd()}")

print("\nActions")
test = Path("test")
print(f"stat: {path.stat()}")
test.touch()
test.unlink()
test.mkdir()
test.rmdir()
#test.symlink_to(__file__)
#test.unlink()

print("\nAccess")
test = Path("test")
with test.open("w") as file:
    file.write("foo")

print(test.read_bytes())
print(test.read_text())
test.write_bytes("foo".encode())
test.write_text("foo")
test.unlink()
