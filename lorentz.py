# Compute dielectric function and eels for lorentz oscillator model

import numpy as np
import math as m
import random

def dielectric(w, w0=1, gamma=1, w_p=1):
    """
    Compute dielectric function

    Parameters:
        w: array like, frequency grid
        w0: resonant frequency
        gamma: broadening parameter of Lorentzian
    """
    if not (type(w).__module__ == np.__name__):
        raise TypeError("Input must be of type numpy.ndarray.")
    if (np.count_nonzero(w) == 0):
        raise ValueError("Input must be nonzero numpy.ndarray.")

    def imag_dielectric(w, w0, gamma, w_p):
        return gamma*w*(w_p**2) / ((w0**2 - w**2)**2 + (w*gamma)**2)

    def real_dielectric(w, w0, gamma, w_p):
        return 1 + (w0**2 - w**2)*(w_p**2) / ((w0**2 - w**2)**2 + (w*gamma)**2)

    return real_dielectric(w, w0, gamma, w_p) - 1j * imag_dielectric(w, w0, gamma, w_p)

def lorentz_eels(w, w0=1, gamma=1, w_p=1):
    """Compute eels spectrum for Lorentz model

    Parameters:
        w: array-like, frequency grid
        w0: resonant frequency
        gamma: broadening parameter or Lorentzian
    """
    return (-1/dielectric(w, w0, gamma, w_p)).imag

def lorentzian_origin(x, y0, xc, w, A):
    """Compute lorentzian function"""
    return y0 + (2*A/np.pi) * (w/(4*(x-xc)**2 + w**2))
