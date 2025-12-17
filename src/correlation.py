import numpy as np

def compute_correlation_map(signals):
    num_channels = signals.shape[0]
    corr_map = np.zeros((num_channels, signals.shape[1]))

    for i in range(num_channels):
        corr_map[i, :] = np.corrcoef(signals[i], signals)[0, 1:]

    return corr_map
