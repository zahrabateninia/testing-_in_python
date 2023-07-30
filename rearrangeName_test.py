#!/usr/bin/env python3

# validating that for a given input it produces expected result
from rearrangeName import rearrange_name

import unittest

class TestRearrange(unittest.TestCase): # inherit form TestCase class 
    def test_basic(self):
        testcase = "Bateninia, Zahra"
        expected = "Zahra Bateninia"
        self.assertEqual(rearrange_name(testcase), expected) # if it is True the test will pass, if not it gives an error

    def test_edge(self):
        testcase= ""
        expected= ""
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_double_name(self):
        testcase = "Bateni, Zahra N."
        expected = "Zahra N. Bateni"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase= "Zahra"
        expected= "Zahra"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main() # will run the test for us
