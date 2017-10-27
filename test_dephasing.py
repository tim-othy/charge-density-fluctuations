"""Unittests for dephasing

Run tests using
$python -m unittest discover -t . -v
"""
import unittest
import numpy as np
from dephasing import dephasing_rate

class DephasingTest(unittest.TestCase):

    def setUp(self):
        self.empty_data = np.array([])
        self.good_data = np.array([1, 2, 3])
        self.non_np_data = [1, 2, 3]
        self.wrong_size = np.array([2, 4])

    def test_dephasing_rate_empty_input(self):
        """dephasing_rate should throw ValueError for
        empty energy input"""
        self.assertRaises(ValueError, dephasing_rate, self.empty_data,
                            self.good_data, self.good_data)
        self.assertRaises(ValueError, dephasing_rate, self.good_data,
                            self.empty_data, self.good_data)
        self.assertRaises(ValueError, dephasing_rate, self.good_data,
                            self.good_data, self.empty_data)
        self.assertRaises(ValueError, dephasing_rate, self.empty_data,
                            self.empty_data, self.empty_data)

    def test_dephasing_different_size_data(self):
        """dephasing_rate should throw ValueError if noise_spectrum
        and eels_spectrum have different sizes"""
        self.assertRaises(AssertionError, dephasing_rate, self.good_data,
                            self.good_data, self.wrong_size)
        self.assertRaises(AssertionError, dephasing_rate, self.good_data,
                            self.wrong_size, self.good_data)

    def test_dephasing_wrong_data_type(self):
        """dephasing_rate should throw TypeError if energy, noise_spectrum,
        or eels_spectrum are a type other then np.ndarray"""
        self.assertRaises(TypeError, dephasing_rate, self.non_np_data,
                            self.good_data, self.good_data)
        self.assertRaises(TypeError, dephasing_rate, self.good_data,
                            self.non_np_data, self.good_data)
        self.assertRaises(TypeError, dephasing_rate, self.good_data,
                            self.good_data, self.non_np_data)
        self.assertRaises(TypeError, dephasing_rate, self.non_np_data,
                            self.non_np_data, self.non_np_data)
