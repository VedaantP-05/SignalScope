import numpy as np

class Measurements:
    @staticmethod
    def rms(signal):
        return np.sqrt(np.mean(signal**2))
    @staticmethod
    def peak(signal):
        return np.max(signal)
    @staticmethod
    def peak_to_peak(signal):
        return np.max(signal) - np.min(signal)
    @staticmethod
    def average(signal):
        return np.mean(signal)
