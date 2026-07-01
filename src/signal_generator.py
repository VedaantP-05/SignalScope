import numpy as np
from scipy import signal

class SignalGenerator:

    def __init__(self):
        self.wave1 = "Sine"
        self.freq1 = 5
        self.amp1 = 1
        self.wave2 = "Sine"        
        self.freq2 = 20
        self.amp2 = 1
        self.wave3 = "Sine"
        self.freq3 = 50
        self.amp3 = 1
        self.amplitude = 1
        self.waveform = "Sine"
        self.noise_level = 0
        self.filter_type = "None"
        self.cutoff_freq = 50
        self.time_window = 1
        self.carrier_freq = 20
        self.mod_freq = 2
        self.mod_index = 0.5

    def generate_wave(self, waveform, frequency, amplitude, t):
        if waveform == "Sine":
            return amplitude * np.sin(
                2 * np.pi * frequency * t
            )
        elif waveform == "Square":
            return amplitude * signal.square(
                2 * np.pi * frequency * t
            )
        elif waveform == "Triangle":
            return amplitude * signal.sawtooth(
                2 * np.pi * frequency * t,
                width=0.5
            )
        elif waveform == "Sawtooth":
            return amplitude * signal.sawtooth(
                2 * np.pi * frequency * t
            )
        return np.zeros_like(t)

    def generate(self, t):
        y = self.generate_wave(
            self.waveform,
            self.frequency,
            self.amplitude,
            t
        )

        noise = np.random.normal(
            0,
            self.noise_level / 100,
            len(t)
        )

        return y + noise

    def generate_composer(self, t):
        y1 = self.generate_wave(
            self.wave1,
            self.freq1,
            self.amp1,
            t
        )

        y2 = self.generate_wave(
            self.wave2,
            self.freq2,
            self.amp2,
            t
        )

        y3 = self.generate_wave(
            self.wave3,
            self.freq3,
            self.amp3,
            t
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

        
