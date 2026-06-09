import numpy as np


class FFTAnalyzer:

    @staticmethod
    def compute(signal, sample_rate):

        N = len(signal)

        fft = np.fft.fft(signal)

        freq = np.fft.fftfreq(
            N,
            d=1/sample_rate
        )

        magnitude = np.abs(fft)

        return (
            freq[:N//2],
            magnitude[:N//2]
        )
