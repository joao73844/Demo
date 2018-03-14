#!/usr/bin/env python
# -*- coding: latin-1 -*-

from context import demo
from demo import fetch

import unittest

class TestFetch(unittest.TestCase):

	def test_fetch_ball(self):
		result = fetch.fetch_ball()
		expected = "fetch ball"
		self.assertEqual(result, expected)

if __name__ == '__main__':
		unittest.main()		