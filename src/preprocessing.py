import numpy as np
from scipy.signal import butter, filtfilt

def normalize_signal(signal):
    return signal / np.max(np.abs(signal))

def bandpass_filter(signal, fs, lowcut=100, highcut=2000, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

def preprocess_signal(signal, fs):
    signal = normalize_signal(signal)
    signal = bandpass_filter(signal, fs)
    return signal

