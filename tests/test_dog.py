#!/usr/bin/env python
# -*- coding: latin-1 -*-

from context import demo
from demo import dog

import unittest

class TestDog(unittest.TestCase):

	def test_bark(self):
		result = dog.bark()
		expected = "woof woof"
		self.assertEqual(result, expected)

if __name__ == '__main__':
		unittest.main()		