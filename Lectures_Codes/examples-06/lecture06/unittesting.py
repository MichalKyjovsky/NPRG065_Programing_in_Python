#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestLists(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Called before all tests in this class')

    def setUp(self):
        print('Called before each test in this class')
        self.list_to_test = ['hello', 'world' ]

    def test_instance(self):
        self.assertIsInstance(self.list_to_test, list)

    def test_len(self):
        self.assertEqual(len(self.list_to_test), 3)

    def test_indexing(self):
        self.assertEqual(self.list_to_test[0], 'hello')
        self.assertEqual(self.list_to_test[1], 'world')

    @unittest.skip
    def test_to_be_ignored(self):
        print('this test is ignored')

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_to_be_run_on_windows_only(self):
        print("we are running tests on windows")

    @unittest.skipIf(sys.platform.startswith("win"), "requires non-Windows")
    def test_to_be_run_on_non_windows_platform(self):
        print("we are NOT running tests on windows")

    def tearDown(self):
        print('Called after each test in this class')
        del self.list_to_test

    @classmethod
    def tearDownClass(cls):
        print('Called after all tests in this class')


# We can run all test in this module via
# python -m unittest unittesting.py
# or we can the following code and run the module regularly
if __name__ == '__main__':
    unittest.main()
