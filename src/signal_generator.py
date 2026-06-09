import numpy as np

class SignalGenerator:
    def __init__(self):
        self.frequency = 2
        self.amplitude = 1

    def generate_sine(self, t):
        return self.amplitude * np.sin(2*np.pi*self.frequency*t)
