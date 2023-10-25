#!/usr/bin/env python
# encoding: utf-8

import pathlib
import unittest

from rosetta_python.main import word_statistics

FIXTURE_FOLDER = pathlib.Path(__file__).parent


class TestMain(unittest.TestCase):
    def test_word_count(self):
        file_path = FIXTURE_FOLDER / "fixtures" / "word_count_test_file.txt"
        word_count = word_statistics(file_path)
        self.assertEqual(word_count, 6)
