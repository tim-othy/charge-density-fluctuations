"""Unittests for dfluct

Run tests using
$python -m unittest discover -t . -v
"""
import unittest
import numpy as np
from dfluct import dfluct_spectrum, dfluct_auto

class DfluctTest(unittest.TestCase):

    def test_dfluct_spectrum_empty_input(self):
        """dfluct_spectrum should raise ValueError for empty energy or eels
        """
        self.assertRaises(ValueError, dfluct_spectrum, [], range(3))
        self.assertRaises(ValueError, dfluct_spectrum, range(3), [])

    def test_dfluct_spectrum_nonequal_input_lenth(self):
        """dfluct_spectrum should raise ValueError if energy and eels
        are of different lengths
        """
        self.assertRaises(ValueError, dfluct_spectrum, range(3), range(5))

    def test_dfluct_auto_empty_input(self):
        """dfluct_auto should raise ValueError for empty energy or eels
        """
        self.assertRaises(ValueError, dfluct_auto, [], range(3))
        self.assertRaises(ValueError, dfluct_auto, range(3), [])

    def test_dfluct_auto_nonequal_input_lenth(self):
        """dfluct_auto should raise ValueError if energy and eels
        are of different lengths
        """
        self.assertRaises(ValueError, dfluct_auto, range(3), range(5))
