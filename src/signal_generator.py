import numpy as np
from scipy import signal


class SignalGenerator:

    def __init__(self):
        self.freq1 = 5
        self.freq2 = 20
        self.freq3 = 50
        self.amplitude = 1
        self.waveform = "Sine"

    def generate(self, t):

        if self.waveform == "Sine":
            return self.amplitude * np.sin(
                2 * np.pi * self.frequency * t
            )

        elif self.waveform == "Square":
            return self.amplitude * signal.square(
                2 * np.pi * self.frequency * t
            )

        elif self.waveform == "Triangle":
            return self.amplitude * signal.sawtooth(
                2 * np.pi * self.frequency * t,
                width=0.5
            )

        elif self.waveform == "Sawtooth":
            return self.amplitude * signal.sawtooth(
                2 * np.pi * self.frequency * t
            )

        return np.zeros_like(t)

    def generate_multitone(self, t):
        y1 = self.amplitude * np.sin(
            2 * np.pi * self.freq1 * t
        )
        y2 = self.amplitude * np.sin(
            2 * np.pi * self.freq2 * t
        )
        y3 = self.amplitude * np.sin(
            2 * np.pi * self.freq3 * t
        )

        return y1 + y2 + y3

        
