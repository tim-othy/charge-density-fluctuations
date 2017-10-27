#Contains routines for the generation of 1/f and white noise processes

import numpy as np
import matplotlib.pyplot as plt
import functools
import scipy


def pink_matrix(n, m):
    """Generates n by m matrix of 1/f noise

    Args
    ----
    n, m : int
        rows, columns of matrix

    Returns
    -------
    array-like
        matrix containing 1/f noise
    """
    if n <= 0 or m <= 0:
        raise ValueError("Inputs must be greater than zero")
    return [abs(pink_noise(n)) for i in range(m)]


def white_matrix(n, m):
    """Generates n by m matrix of white noise

    Args
    ----
    n, m : int
        rows, columns of matrix

    Returns
    -------
    array-like
        matrix containing white noise
    """
    if n <= 0 or m <= 0:
        raise ValueError("Inputs must be greater than zero")
    return np.random.random((n, m))

def pink_noise(n):
    """Generates 1/f (pink) noise

    Args
    ----
    n : int
        number of samples to produce

    Returns
    -------
    np.ndarray
        array containing 1/f noise.

    Notes
    -----
    * The following uses n*2 due to the symmetry of the FFT
    * h is array containing coefficients for coloured noise generation
    * output is a convolution of h coefficients with white noise process

    See "Discrete simulation of colored noise and stochastic
    processes and 1/f/sup/spl alpha//power law noise generation"
    by NJ Kasdin for detailed explanation of this algorithm.
    """
    if n <= 0:
        raise ValueError("Input must be greater than zero")

    h = np.zeros(n*2)
    h[0] = 1
    for i in range(1, n*2):
        h[i] = (0.5 + i - 1) * h[i-1] / float(i)
    h = np.fft.fft(h)

    noise = np.random.normal(0, 1, size=n*2)
    noise = np.fft.fft(noise)

    for i in range(0, n*2, 2):
        if i < 2:
            noise[i] = noise[i] * h[i]
        else:
            noise[i] = noise[i] * h[i] - noise[i+1]*h[i+1]
            noise[i+1] = noise[i] * h[i+1] - noise[i+1]*h[i]

    noise = np.fft.ifft(noise)
    return noise[:n] / max(noise)

if __name__ == "__main__":

    wnoise = white_matrix(1000, 1001)
    pnoise = pink_matrix(1000, 1000)
    #wnoise_spec = abs(np.fft.fft(wnoise))
    #np.delete(wnoise_spec, -1, axis=0)
    #np.delete(wnoise_spec, 0, axis=0)

    plt.subplot(2, 2, 1)
    plt.imshow(wnoise)
    plt.colorbar()

    plt.subplot(2, 2, 2)
    plt.imshow(pnoise)
    plt.colorbar()

    wnoise_spec = abs(np.fft.fft2(wnoise))
    wnoise_spec = [channel[1:] for channel in wnoise_spec]
    plt.subplot(2, 2, 3)
    plt.imshow(np.fft.fftshift(wnoise_spec))
    plt.colorbar()

    pnoise_spec = abs(np.fft.fft2(pnoise))
    pnoise_spec = [channel[1:] for channel in pnoise_spec]
    plt.subplot(2, 2, 4)
    plt.imshow(np.fft.fftshift(pnoise_spec))
    plt.colorbar()

    #plt.imshow(np.fft.fftshift(abs(np.fft.fft(pmatrix))))
    #plt.imshow(np.fft.fftshift(abs(np.fft.fft2(np.random.random((1000, 1000))))))
    #plt.imshow(pmatrix)
    #pmat = np.column_stack((gen_pink_noise(1000), gen_pink_noise(1000)))
    #plt.imshow(np.fft.fftshift(abs(np.fft.fft(pmatrix))))
    plt.show()
