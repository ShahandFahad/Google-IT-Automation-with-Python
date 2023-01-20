##!usr/bin/env python3  -> chmod +x rearrange_test.py -> become executable
# inorder to make a test file user '_test' suffex
from rearrange import rearrange_name
import unittest

# make custom class and inherit it from unittest.TestCase class


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()  # run the test
