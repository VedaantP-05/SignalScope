import pyqtgraph as pg
import numpy as np

from datetime import datetime
from PyQt6.QtCore import (
    Qt,
    QTimer
)
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSlider,
    QComboBox,
    QLineEdit,
    QPushButton
)
from fft_analyzer import FFTAnalyzer
from measurements import Measurements
from signal_generator import SignalGenerator

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.phase = 0
        self.generator = SignalGenerator()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16) 

        self.setWindowTitle("SignalScope")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        control_panel = QVBoxLayout()
        

        control_panel.addWidget(QLabel("Frequency"))

        freq_layout, self.freq_slider, self.freq_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(freq_layout)


        control_panel.addWidget(QLabel("Amplitude"))

        amp_layout, self.amp_slider, self.amp_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(amp_layout)
        

        control_panel.addWidget(QLabel("Noise"))

        noise_layout, self.noise_slider, self.noise_input = \
            self.create_slider_input(0, 100, 0)
        control_panel.addLayout(noise_layout)


        self.freq1_label = QLabel("Frequency 1")
        control_panel.addWidget(self.freq1_label)
        
        freq1_layout, self.freq1_slider, self.freq1_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(freq1_layout)

        self.freq2_label = QLabel("Frequency 2")
        control_panel.addWidget(self.freq2_label)
        
        freq2_layout, self.freq2_slider, self.freq2_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(freq2_layout)

        self.freq3_label = QLabel("Frequency 3")
        control_panel.addWidget(self.freq3_label)
        
        freq3_layout, self.freq3_slider, self.freq3_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(freq3_layout)


        control_panel.addWidget(QLabel("Waveform"))

        self.wave_selector = QComboBox()

        self.wave_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth",
            "Multi-Tone"
        ])
        control_panel.addWidget(self.wave_selector)

        self.multitone_widgets = [
            self.freq1_label,
            self.freq1_slider,
            self.freq1_input,

            self.freq2_label,
            self.freq2_slider,
            self.freq2_input,

            self.freq3_label,
            self.freq3_slider,
            self.freq3_input
        ]

        self.wave_selector.currentIndexChanged.connect(self.update_multitone_controls)
        self.update_multitone_controls()


        control_panel.addWidget(QLabel("Filter"))

        self.filter_selector = QComboBox()
        self.filter_selector.addItems([
            "None",
            "Low Pass",
            "High Pass"
        ])

        control_panel.addWidget(self.filter_selector)

        self.cutoff_label  = QLabel("Cutoff Frequency")
        control_panel.addWidget(self.cutoff_label)
        
        cutoff_layout, self.cutoff_slider, self.cutoff_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(cutoff_layout)

        self.cutoff_widgets = [
            self.cutoff_label,
            self.cutoff_slider,
            self.cutoff_input
        ]

        self.filter_selector.currentTextChanged.connect(self.update_filter_controls)
        self.update_filter_controls()


        control_panel.addWidget(QLabel("Time Window"))

        time_layout, self.time_slider, self.time_input = \
            self.create_slider_input(1, 100, 1)
        control_panel.addLayout(time_layout)


        self.export_button = QPushButton("Export CSV")
        
        self.export_button.clicked.connect(self.export_signal)
        control_panel.addWidget(self.export_button)


        self.screenshot_btn = QPushButton("Save Plot")
        
        control_panel.addWidget(self.screenshot_btn)
        self.screenshot_btn.clicked.connect(
            self.save_plot
        )

        control_panel.addSpacing(20)

        self.rms_label = QLabel("RMS: 0")
        self.peak_label = QLabel("Peak: 0")
        self.ptp_label = QLabel("Peak-to-Peak: 0")
        self.avg_label = QLabel("Average: 0")

        control_panel.addWidget(self.rms_label)
        control_panel.addWidget(self.peak_label)
        control_panel.addWidget(self.ptp_label)
        control_panel.addWidget(self.avg_label)       

        plots_layout = QVBoxLayout()

        self.wave_plot = pg.PlotWidget()

        self.wave_plot.setBackground("k")

        self.wave_plot.showGrid(
            x=True,
            y=True
        )

        self.curve = self.wave_plot.plot(
            pen='y'
        )

        self.fft_plot = pg.PlotWidget()

        self.fft_plot.setBackground("k")

        self.fft_plot.showGrid(
            x=True,
            y=True
        )

        self.fft_curve = self.fft_plot.plot(
            pen='c'
        )

        plots_layout.addWidget(
            self.wave_plot
        )

        plots_layout.addWidget(
            self.fft_plot
        )

        main_layout.addLayout(
            control_panel,
            1
        )

        main_layout.addLayout(
            plots_layout,
            4
        )

    def update(self):

        self.generator.frequency = self.freq_slider.value()
        self.generator.freq1 = self.freq1_slider.value()
        self.generator.freq2 = self.freq2_slider.value()
        self.generator.freq3 = self.freq3_slider.value()
        self.generator.amplitude = self.amp_slider.value()
        self.generator.noise_level = self.noise_slider.value()
        self.generator.waveform = self.wave_selector.currentText()
        self.generator.filter_type = self.filter_selector.currentText()
        self.generator.cutoff_freq = self.cutoff_slider.value()
        self.generator.time_window = self.time_slider.value()

        t = np.linspace(
            0,
            self.generator.time_window,
            1000
        )

        if self.generator.waveform == "Multi-Tone":
            y = self.generator.generate_multitone(
                t + self.phase
            )
        else:
            y = self.generator.generate(
                t + self.phase
            )

        if self.generator.filter_type != "None":
            y = self.generator.apply_filter(
                y,
                1000
            )

        self.t = t
        self.signal = y

        freq, mag = FFTAnalyzer.compute(
            y,
            1000
        )

        self.fft_curve.setData(
            freq,
            mag
        )

        self.rms_label.setText(f"RMS: {Measurements.rms(y):.2f}")

        self.peak_label.setText(f"Peak: {Measurements.peak(y):.2f}")

        self.ptp_label.setText(f"Peak-to-Peak: {Measurements.peak_to_peak(y):.2f}")

        self.avg_label.setText(f"Average: {Measurements.average(y):.2f}")

        self.curve.setData(
            t,
            y
        )

        self.phase += 0.01

    def create_slider_input(self, min_val, max_val, default):
        slider_layout = QHBoxLayout()

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(min_val, max_val)
        slider.setValue(default)

        box = QLineEdit(str(default))
        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        box.setFixedWidth(50)

        slider.valueChanged.connect(
            lambda v: box.setText(str(v))
        )

        box.editingFinished.connect(
            lambda: slider.setValue(int(box.text()))
        )

        slider_layout.addWidget(slider)
        slider_layout.addWidget(box)

        return slider_layout, slider, box

    def update_multitone_controls(self):
        visible = (
            self.wave_selector.currentText() == "Multi-Tone"
        )

        for widget in self.multitone_widgets:
            widget.setVisible(visible)

    def update_filter_controls(self):
        visible = (
            self.filter_selector.currentText() != "None"
        )

        for widget in self.cutoff_widgets:
            widget.setVisible(visible)

    def export_signal(self):
        filename = datetime.now().strftime("signal_%Y%m%d_%H%M%S.csv")
        np.savetxt(
            filename,
            np.column_stack((self.t, self.signal)),
            delimiter=",",
            header="Time,Amplitude",
            comments="",
            fmt="%.6f"
        )
        print("Signal exported.")

    def save_plot(self):
        filename = datetime.now().strftime("plot_%Y%m%d_%H%M%S.png")
        self.fft_plot.grab().save(filename)
        print("Plot exported.")
