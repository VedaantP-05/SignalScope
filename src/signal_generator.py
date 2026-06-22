import numpy as np
from scipy import signal


class SignalGenerator:

    def __init__(self):
        self.freq1 = 5
        self.freq2 = 20
        self.freq3 = 50
        self.amplitude = 1
        self.waveform = "Sine"
        self.noise_level = 0
        self.filter_type = "None"
        self.cutoff_freq = 50
        self.time_window = 1

    def generate(self, t):

        if self.waveform == "Sine":
            y = self.amplitude * np.sin(
                2 * np.pi * self.frequency * t
            )

        elif self.waveform == "Square":
            y = self.amplitude * signal.square(
                2 * np.pi * self.frequency * t
            )

        elif self.waveform == "Triangle":
            y = self.amplitude * signal.sawtooth(
                2 * np.pi * self.frequency * t,
                width=0.5
            )

        elif self.waveform == "Sawtooth":
            y = self.amplitude * signal.sawtooth(
                2 * np.pi * self.frequency * t
            )

        else:
            y = np.zeros_like(t)

        noise = np.random.normal(
            0,
            self.noise_level / 100,
            len(t)
        )

        return y + noise

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

        noise = np.random.normal(
            0,
            self.noise_level / 100,
            len(t)
        )

        return y1 + y2 + y3 + noise

    def apply_filter(self, y, sample_rate):
        if self.filter_type == "None":
            return y
        nyquist = sample_rate / 2
        normal_cutoff = max(self.cutoff_freq / nyquist, 0.01)
        
        b, a = signal.butter(
            4,
            normal_cutoff,
            btype = "low" if self.filter_type == "Low Pass"
            else "high"
        )

        return signal.filtfilt(
            b,
            a,
            y
        )

        
