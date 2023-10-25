#!/usr/bin/env python
# encoding: utf-8

import unittest

from rosetta_python.math_funcs import add


class TestMathFuncs(unittest.TestCase):
    def test_add(self):
        status = add(1, 1)
        self.assertEqual(status, 2)
