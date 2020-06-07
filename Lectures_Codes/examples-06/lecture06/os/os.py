#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES: os interface, system info, environment, lightweight process management
import os
import signal

print("\n### Basic system information")
print(f"Operating sistem simple name: \"{os.name}\"")
#print(f"Operation sysrtem specific name: \"{os.uname()}\"")


print("\n### Environment")
print(f"Environment as string: \"{os.environ}\"")
#print(f"Environment as bytes: \"{os.environb}\"")

print(f"Get env value for key \"foo\": \"{os.getenv('foo', 'default : foo not defined yet')}\"")
print(f"Set env value for key \"foo\" to \"bar\" # 1")
os.putenv('foo', 'bar')

print(f"Get env value for key \"foo\": \"{os.getenv('foo', 'default : foo defined byt environ not updated')}\"")
print(f"Set env value for key \"foo\" to \"bar\" # 2")
os.environ['foo'] = 'bar'

print(f"Get env value for key \"foo\": \"{os.getenv('foo', 'default : assigning to os.environmrnt fileds is prefered')}\"")


print("\n### Process management")
print(f"Path where binaries are serched for: \"{os.get_exec_path()}\"")
#print(f"Current user name: \"{os.getlogin()}\"")

print("Print current diorectory using call to external program")
if os.name == "posix":
    os.system("ls")
else:
    os.system("dir")

pid = os.getpid()
print(f"PID of the current process is {pid}")

print("Kill process using PID, kill this process")
os.kill(pid, signal.SIGINT)