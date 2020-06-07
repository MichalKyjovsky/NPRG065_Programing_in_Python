# FEATURES: package installation

# This is an installer for myhellopackage and its subpackages

# First we import setup from setuptools
from setuptools import setup

# Execute setup. It does everything automatically, we just need to tell which
# packages to install. It also parses commandline arguments in order to enable
# the user to choose where to install. Apart from other stuff it enable to list
# PIP dependencies that has to be also installed using "install_requires".
setup(name='myhello',
      version='1.2.3',
      description='Test package',
      author='John Doe',
      author_email='john@doe.com',
      url='http://mypackage.doe.com',
      packages=['myhellopackage', 'myhellopackage.greetings'],
      install_requires=['markdown']
      )

# In order to execute the install run the setup.py (this file) with arguments:
#
# System wide install, requires root access:
#
# python3 setup.py install
#
#
# User local install, should work without special permissions
#
# python3 setup.py install --user
#
# Or even better create a virtual environment, activate it and install in it
#
# virtualenv a_directory
# source a_directory/bin/activate
# python3 setup.py install


# Once the setups is completed (either locally or globally) it should be
# possible to import the myhellopackage.greetings.hello and call
# hello.say_hello() from any python3 application in the system.

# Python 3.6.10 (default, Mar  4 2020, 09:50:16)
# [GCC 8.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from myhellopackage.greetings import hello
# Initializing package myhellopackage ...
# Initializing package myhellopackage.greetings ...
# Initializing module myhellopackage.greetings.hello ...
# >>> hello.say_hello()
# Hello from myhellopackage.greetings.hello
# >>>
