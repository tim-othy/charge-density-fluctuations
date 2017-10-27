# Contains routines for the computation of quantities related to
# charge-density fluctuations
# TODO: check units of dfluct_spectrum
import numpy as np
from autocorr import autocorr


def dfluct_spectrum(energy, eels, kT = 0.0257, kpoints = 291):
    """Computes the spectral density associated with charge-density
    fluctuations from the eels spectrum

    Args
    ----
    energy : array-like
        energy scale

    eels : array-like
        electron energy-loss spectrum

    kT : float
        Boltzmann constant at given temperature

    kpoints : int
        k-point samples

    Returns
    -------
    array-like

    Notes
    -----
    For details see T.P. Mehay et al., Investigation of density fluctuations
    in graphene using the fluctuation-dissipation relations, Computational
    Condensed Matter (2017), http://dx.doi.org/10.1016/j.cocom.2017.08.08
    """
    # Interpolate since gpaw energy scale is nonlinear
    interp_energy = np.linspace(min(energy), max(energy), len(energy))
    interp_eels = np.interp(interp_energy, energy, eels)

    # Start at 1 to avoid singularity at zero energy
    for i in range(1, len(interp_energy)):
        eels[i] = -eels[i] / (np.exp(-interp_energy[i]/kT) - 1)

    # Fundamental charge
    e = 1.6e-19

    return np.array(map(lambda x: pow(kpoints, -2)/(2*e**2)*x, eels))

def dfluct_auto(energy, eels):
    """
    Computes the charge-density autocorrelation function using the eels
    spectrum

    Args
    ----
    energy : array-like
        energy scale

    eels : array-like
        electron energy-loss spectrum

    Returns
    -------
    array-like
        real part of autocorrelation function associated with charge-density
        fluctuations

    """
    # Following prefactor has to do with units in equation, i.e. converting
    # to eV and incorporating Planck constant
    return float(6.582118487e-16)*autocorr(dfluct_spectrum(energy, eels), method="pow").real
