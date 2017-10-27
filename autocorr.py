#Computes autocorrelation function

import numpy as np

def autocorr(data, method="data"):
    """
    Compute autocorrelation function.

    Args
    ----
    data: numpy array

    method: string, "data" or "pow"
        Specify method used, "data" computes autocorrelation
        from autocorrelation of time-series, "pow" computes
        autocorrelation from inverse fft of power spectrum.
    """
    if not (type(data).__module__ == np.__name__):
        raise TypeError("Input must be of type numpy.ndarray")
    if (np.count_nonzero(data) == 0):
        raise ValueError("Input must be nonzero numpy.ndarray")

    if method == "data":
        data = np.array([i - np.mean(data) for i in data])
        autocorr = np.correlate(data, data, mode='full') / np.sum(data**2)
        autocorr = autocorr[len(autocorr)/2:]

    elif method == "pow":
        # Specification of np.fft.ifft requires data to be symmetric
        # about zero frequency
        if np.array_equal(data[1:len(data)/2 + 1], data[len(data)/2 + 1:][::-1]):
            autocorr = np.fft.ifft(data)
        else:
            data = np.append(data, data[1:][::-1])
            autocorr = np.fft.ifft(data)
            autocorr = autocorr[:len(autocorr)/2 + 1]
    else:
        raise ValueError("Argument method must be in (\"data\", \"pow\").")
        
    return autocorr
