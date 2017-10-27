"""Unittests for noise

Run tests using
$python -m unittest discover -t . -v
"""
import unittest
#import numpy as np
from noise import pink_matrix, white_matrix, pink_noise

class NoiseTest(unittest.TestCase):

    def test_pink_noise_negative_input(self):
        """pink_noise should throw ValueError if n <= 0
        """
        self.assertRaises(ValueError, pink_noise, 0)
        self.assertRaises(ValueError, pink_noise, -1)

    def test_pink_noise_matrix_negative_input(self):
        """pink_noise_matrix should raise ValueError if m or n <= 0
        """
        self.assertRaises(ValueError, pink_matrix, 0, 0)
        self.assertRaises(ValueError, pink_matrix, 1, 0)
        self.assertRaises(ValueError, pink_matrix, 0, 1)

    def test_white_noise_matrix_negative_input(self):
        """white_noise_matrix should raise ValueError if m or n <= 0
        """
        self.assertRaises(ValueError, white_matrix, 0, 0)
        self.assertRaises(ValueError, white_matrix, 1, 0)
        self.assertRaises(ValueError, white_matrix, 0, 1)
