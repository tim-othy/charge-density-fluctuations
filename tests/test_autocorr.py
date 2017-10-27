"""Unittests for dfluct

Run tests using
$python -m unittest discover -t . -v
"""
import unittest
import numpy as np
from autocorr import autocorr

class AutocorrTest(unittest.TestCase):

    def setUp(self):
        self.empty_data = np.array([])
        self.input_data = np.array([1, 2, 3])
        self.pow_spec = abs(np.fft.fft(self.input_data))
        self.non_np_data = [1, 2, 3]


    def test_autocorr_empty_input(self):
        """autocorr should raise ValueError for empty input
        """
        self.assertRaises(ValueError, autocorr, self.empty_data)


    def test_autocorr_non_np_input(self):
        """autocorr should raise TypeError for non np.ndarray input
        """
        self.assertRaises(TypeError, autocorr, self.non_np_data)


    def test_autocorr_output_type_method_data(self):
        """autocorr should return type np.ndarray
        """
        self.assertIsInstance(autocorr(self.input_data, method="data"),
            np.ndarray)


    def test_autoccorr_output_type_method_pos(self):
        """autocorr should return type np.ndarray
        """
        self.assertIsInstance(autocorr(self.input_data, method="pow"),
            np.ndarray)


    def test_autocorr_bad_method(self):
        """autocorr should raise ValueError for incorrect method parameter
        """
        self.assertRaises(ValueError, autocorr, self.input_data, "method")
