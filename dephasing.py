# Routines for the computation of dephasing rates
# TODO: check what rows/cols denote in input, i.e. q-values or energy

import numpy as np
import matplotlib.pyplot as plt
from noise import white_matrix, pink_matrix
from dfluct import dfluct_spectrum
from autocorr import autocorr

def check_input_type(input):
    if not (type(input).__module__ == np.__name__):
        raise TypeError("Input must be of type numpy.ndarray")

def check_if_empty(input):
    if not input.size:
        raise ValueError("Input must be non-empty")

def dephasing_rate(energy, noise_spectrum, eels_spectrum, kT = 0.0257):
    """Computes the dephasing rate

    Args
    ----
    energy : array-like
        energy scale

    noise_spectrum : array-like
        power spectrum of system fluctuations

    eels_spectrum : array-like
        electron energy-loss spectrum

    kT : float
        Boltzmann constant at given temperature

    Returns
    -------
    array-like

    Notes
    -----
    For details see D. Cohen et. al., The dephasing rate formula
    in the many body context (2009)
    """
    for arr in (energy, noise_spectrum, eels_spectrum):
        check_input_type(arr)
        check_if_empty(arr)
    assert(noise_spectrum.shape == eels_spectrum.shape)

    # Ensure energy scale is linear for fft
    interp_energy = np.linspace(min(energy), max(energy), len(energy))
    dfluct_spec = dfluct_spectrum(energy, eels_spectrum)
    # integrand is convolution of noise spectrum and charge-density
    # fluctuation spectral density
    integrand = np.zeros(len(eels_spectrum))
    for i in range(len(integrand)):
        integrand[i] = noise_spectrum[i] * np.exp(-interp_energy[i]/kT) \
            * dfluct_spec[i]
    # np.sum(arr) equivalent to summing over all dimensions
    return  np.sum(integrand)
