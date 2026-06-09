from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSlider,
    QComboBox
)

from PyQt6.QtCore import Qt

import pyqtgraph as pg


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SignalScope v0.2")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        control_panel = QVBoxLayout()

        control_panel.addWidget(QLabel("Frequency"))

        self.freq_slider = QSlider(Qt.Orientation.Horizontal)
        self.freq_slider.setMinimum(1)
        self.freq_slider.setMaximum(20)
        self.freq_slider.setValue(2)

        control_panel.addWidget(self.freq_slider)

        control_panel.addWidget(QLabel("Amplitude"))

        self.amp_slider = QSlider(Qt.Orientation.Horizontal)
        self.amp_slider.setMinimum(1)
        self.amp_slider.setMaximum(10)
        self.amp_slider.setValue(1)

        control_panel.addWidget(self.amp_slider)

        control_panel.addWidget(QLabel("Waveform"))

        self.wave_selector = QComboBox()

        self.wave_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth"
        ])

        control_panel.addWidget(self.wave_selector)

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
