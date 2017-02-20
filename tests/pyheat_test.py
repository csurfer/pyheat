#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pyheat tests
~~~~~~~~~~

Usage from git root:

    >>> python setup.py test
"""

import os
import unittest

from pyheat import PyHeat


class PyHeatTest(unittest.TestCase):

    def setUp(self):
        data_path = os.path.dirname(os.path.realpath(__file__))
        self.pyheat = PyHeat(data_path + '/test_program.py')

    def test_pyheat_show(self):
        """Basic test to check pyheat class works end to end."""
        self.pyheat.create_heatmap()
        self.pyheat.show_heatmap(blocking=False)

    def tearDown(self):
        self.pyheat.close_heatmap()


if __name__ == '__main__':
    unittest.main()
