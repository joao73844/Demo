#!/usr/bin/env python
# -*- coding: latin-1 -*-

from context import demo

import unittest

class TestFetch(unittest.TestCase):
	""" Tests for the interface of the module (demo.__init__.py) """
	def test_bark(self):
		result = demo.fetch_ball()
		expected = "fetch ball"
		self.assertEqual(result, expected)

	def test_fetch_ball(self):
		result = demo.fetch_ball()
		expected = "fetch ball"
		self.assertEqual(result, expected)

if __name__ == '__main__':
		unittest.main()		