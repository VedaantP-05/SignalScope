import sys
import numpy as np

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

from signal_generator import SignalGenerator
from main_window import MainWindow
from measurements import Measurements
from fft_analyzer import FFTAnalyzer

app = QApplication(sys.argv)

generator = SignalGenerator()

window = MainWindow()

window.show()

phase = 0

timer = QTimer()


def update():

    global phase

    generator.frequency = window.freq_slider.value()

    generator.freq1 = window.freq1_slider.value()

    generator.freq2 = window.freq2_slider.value()

    generator.freq3 = window.freq3_slider.value()

    generator.amplitude = window.amp_slider.value()

    generator.noise_level = window.noise_slider.value()

    generator.waveform = window.wave_selector.currentText()

    generator.filter_type = window.filter_selector.currentText()

    generator.cutoff_freq = window.cutoff_slider.value()

    t = np.linspace(
        0,
        1,
        1000
    )

    if generator.waveform == "Multi-Tone":
        y = generator.generate_multitone(
            t + phase
        )
    else:
        y = generator.generate(
            t + phase
        )

    if generator.filter_type != "None":
        y = generator.apply_filter(
            y,
            1000
        )   

    freq, mag = FFTAnalyzer.compute(
        y,
        1000
    )

    window.fft_curve.setData(
        freq,
        mag
    )

    window.rms_label.setText(
        f"RMS: {Measurements.rms(y):.2f}"
    )

    window.peak_label.setText(
        f"Peak: {Measurements.peak(y):.2f}"
    )

    window.ptp_label.setText(
        f"Peak-to-Peak: {Measurements.peak_to_peak(y):.2f}"
    )

    window.avg_label.setText(
        f"Average: {Measurements.average(y):.2f}"
    )

    window.curve.setData(
        t,
        y
    )

    phase += 0.01


timer.timeout.connect(update)

timer.start(16)

sys.exit(app.exec())
