#================== IMPORTS ==================#
import pyqtgraph as pg
import numpy as np

from fft_analyzer import FFTAnalyzer
from measurements import Measurements
from signal_generator import SignalGenerator
from datetime import datetime
from PyQt6.QtGui import QAction
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
    QPushButton,
    QToolBar,
    QMessageBox,
    QStyle
)

#================== MAIN WINDOW ==================#
class MainWindow(QMainWindow):

#------------------------------ INITIALISATION ------------------------------#
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("SignalScope")
        self.resize(1200, 700)
        self.phase = 0
        self.generator = SignalGenerator()
        self.timer = QTimer()
        self.main_layout = QHBoxLayout()
        central = QWidget()
        self.setCentralWidget(central)
        central.setLayout(self.main_layout)

        self.create_controls()
        self.create_plots()
        self.create_measurements()
        self.create_menu()
        self.create_toolbar()

        self.main_layout.addLayout(
            self.control_panel,
            1
        )
        self.main_layout.addLayout(
            self.plots_layout,
            4
        )

        self.connect_signals()
        self.update_dynamic_controls()

        self.timer.start(16)
        
#------------------------------ UI CONSTRUCTION ------------------------------#
    def create_controls(self):
        self.control_panel = QVBoxLayout()

        self.wave_label = QLabel("Waveform")
        self.control_panel.addWidget(self.wave_label)

        self.wave_selector = QComboBox()
        self.wave_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth",
            "AM Signal",
            "Signal Composer"            
        ])
        self.control_panel.addWidget(self.wave_selector)

        self.freq_label = QLabel("Frequency")
        self.control_panel.addWidget(self.freq_label)

        freq_layout, self.freq_slider, self.freq_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(freq_layout)

        self.amp_label = QLabel("Amplitude")
        self.control_panel.addWidget(self.amp_label)

        amp_layout, self.amp_slider, self.amp_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(amp_layout)

        self.time_label = QLabel("Time Window")
        self.control_panel.addWidget(self.time_label)

        time_layout, self.time_slider, self.time_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(time_layout)

        self.noise_label = QLabel("Noise")
        self.control_panel.addWidget(self.noise_label)

        noise_layout, self.noise_slider, self.noise_input = (
            self.create_slider_input(0, 100, 0)
        )
        self.control_panel.addLayout(noise_layout)

        self.wave1_label = QLabel("Waveform 1")
        self.control_panel.addWidget(self.wave1_label)

        self.wave1_selector = QComboBox()
        self.wave1_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth"
        ])

        self.control_panel.addWidget(self.wave1_selector)

        self.freq1_label = QLabel("Frequency 1")
        self.control_panel.addWidget(self.freq1_label)

        freq1_layout, self.freq1_slider, self.freq1_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(freq1_layout)

        self.amp1_label = QLabel("Amplitude 1")
        self.control_panel.addWidget(self.amp1_label)

        amp1_layout, self.amp1_slider, self.amp1_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(amp1_layout)

        self.wave2_label = QLabel("Waveform 2")
        self.control_panel.addWidget(self.wave2_label)

        self.wave2_selector = QComboBox()
        self.wave2_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth"
        ])

        self.control_panel.addWidget(self.wave2_selector)

        self.freq2_label = QLabel("Frequency 2")
        self.control_panel.addWidget(self.freq2_label)

        freq2_layout, self.freq2_slider, self.freq2_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(freq2_layout)

        self.amp2_label = QLabel("Amplitude 2")
        self.control_panel.addWidget(self.amp2_label)

        amp2_layout, self.amp2_slider, self.amp2_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(amp2_layout)

        self.wave3_label = QLabel("Waveform 3")
        self.control_panel.addWidget(self.wave3_label)

        self.wave3_selector = QComboBox()
        self.wave3_selector.addItems([
            "Sine",
            "Square",
            "Triangle",
            "Sawtooth"
        ])

        self.control_panel.addWidget(self.wave3_selector)

        self.freq3_label = QLabel("Frequency 3")
        self.control_panel.addWidget(self.freq3_label)

        freq3_layout, self.freq3_slider, self.freq3_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(freq3_layout)

        self.amp3_label = QLabel("Amplitude 3")
        self.control_panel.addWidget(self.amp3_label)

        amp3_layout, self.amp3_slider, self.amp3_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(amp3_layout)

        self.filter_label = QLabel("Filter")
        self.control_panel.addWidget(self.filter_label)

        self.filter_selector = QComboBox()
        self.filter_selector.addItems([
            "None",
            "Low Pass",
            "High Pass"
        ])
        self.control_panel.addWidget(self.filter_selector)

        self.cutoff_label = QLabel("Cutoff Frequency")
        self.control_panel.addWidget(self.cutoff_label)

        cutoff_layout, self.cutoff_slider, self.cutoff_input = (
            self.create_slider_input(1, 100, 1)
        )
        self.control_panel.addLayout(cutoff_layout)

        self.carrier_label = QLabel("Carrier Frequency")
        self.control_panel.addWidget(self.carrier_label)

        carrier_layout, self.carrier_slider, self.carrier_input = (
            self.create_slider_input(1, 100, 20)
        )
        self.control_panel.addLayout(carrier_layout)

        self.mod_label = QLabel("Modulating Frequency")
        self.control_panel.addWidget(self.mod_label)

        mod_layout, self.mod_slider, self.mod_input = (
            self.create_slider_input(1, 20, 2)
        )
        self.control_panel.addLayout(mod_layout)

        self.index_label = QLabel("Modulation Index")
        self.control_panel.addWidget(self.index_label)

        index_layout, self.index_slider, self.index_input = (
            self.create_slider_input(0, 100, 50)
        )
        self.control_panel.addLayout(index_layout)

        self.control_groups = {
            "frequency": [
                self.freq_label,
                self.freq_slider,
                self.freq_input
            ],
            "amplitude": [
                self.amp_label,
                self.amp_slider,
                self.amp_input
            ],
            "composer": [
                self.wave1_label,
                self.wave1_selector,
                self.freq1_label,
                self.freq1_slider,
                self.freq1_input,
                self.amp1_label,
                self.amp1_slider,
                self.amp1_input,
                
                self.wave2_label,
                self.wave2_selector,
                self.freq2_label,
                self.freq2_slider,
                self.freq2_input,
                self.amp2_label,
                self.amp2_slider,
                self.amp2_input,
                
                self.wave3_label,
                self.wave3_selector,
                self.freq3_label,
                self.freq3_slider,
                self.freq3_input,
                self.amp3_label,
                self.amp3_slider,
                self.amp3_input
            ],
            "am": [
                self.carrier_label,
                self.carrier_slider,
                self.carrier_input,
                self.mod_label,
                self.mod_slider,
                self.mod_input,
                self.index_label,
                self.index_slider,
                self.index_input
            ],
            "cutoff": [
                self.cutoff_label,
                self.cutoff_slider,
                self.cutoff_input
            ]
        }

        self.control_panel.addSpacing(20)

    def create_plots(self):
        self.plots_layout = QVBoxLayout()

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

        self.plots_layout.addWidget(
            self.wave_plot
        )
        self.plots_layout.addWidget(
            self.fft_plot
        )

    def create_measurements(self):
        self.rms_label = QLabel("RMS: 0")
        self.peak_label = QLabel("Peak: 0")
        self.ptp_label = QLabel("Peak-to-Peak: 0")
        self.avg_label = QLabel("Average: 0")

        self.control_panel.addWidget(self.rms_label)
        self.control_panel.addWidget(self.peak_label)
        self.control_panel.addWidget(self.ptp_label)
        self.control_panel.addWidget(self.avg_label)

    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        self.export_action = QAction("Export CSV", self)
        self.save_action = QAction("Save Plot", self)
        self.exit_action = QAction("Exit", self)

        file_menu.addAction(self.export_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        view_menu = menu.addMenu("&View")
        self.reset_view_action = QAction("Reset View", self)
        view_menu.addAction(self.reset_view_action)
        help_menu = menu.addMenu("&Help")
        self.about_action = QAction("About SignalScope", self)
        help_menu.addAction(self.about_action)

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
        def update_slider():

            text = box.text().strip()

            if text == "":
                box.setText(str(slider.value()))
                return

            try:
                value = int(text)

                value = max(min_val, min(value, max_val))

                slider.setValue(value)

            except ValueError:
                box.setText(str(slider.value()))

        box.editingFinished.connect(update_slider)

        slider_layout.addWidget(slider)
        slider_layout.addWidget(box)

        return slider_layout, slider, box

    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonIconOnly
        )
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        self.export_action.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_DialogSaveButton
            )
        )
        self.save_action.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_FileDialogDetailedView
            )
        )
        self.reset_view_action.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_BrowserReload
            )
        )
        toolbar.addAction(self.export_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.reset_view_action)
        self.export_action.setToolTip("Export CSV")
        self.save_action.setToolTip("Save Plot")
        self.reset_view_action.setToolTip("Reset View")


#------------------------------ SIGNAL CONNECTIONS ------------------------------#
    def connect_signals(self):
        self.timer.timeout.connect(self.update)
        self.wave_selector.currentIndexChanged.connect(
            self.update_dynamic_controls
        )
        self.filter_selector.currentIndexChanged.connect(
            self.update_dynamic_controls
        )
        self.export_action.triggered.connect(
            self.export_signal
        )
        self.save_action.triggered.connect(
            self.save_plot
        )
        self.reset_view_action.triggered.connect(
            self.reset_view
        )
        self.exit_action.triggered.connect(
            self.close
        )
        self.about_action.triggered.connect(
            lambda: QMessageBox.about(
                self,
                "SignalScope",
                "SignalScope v1.0\n\nBuilt with PyQt6."
            )
        )

#------------------------------ SIGNAL PROCESSING ------------------------------#
    def sync_generator_settings(self):
        g = self.generator
        g.frequency = self.freq_slider.value()
        g.amplitude = self.amp_slider.value()
        
        g.wave1 = self.wave1_selector.currentText()
        g.freq1 = self.freq1_slider.value()
        g.amp1 = self.amp1_slider.value()
        g.wave2 = self.wave2_selector.currentText()
        g.freq2 = self.freq2_slider.value()
        g.amp2 = self.amp2_slider.value()
        g.wave3 = self.wave3_selector.currentText()
        g.freq3 = self.freq3_slider.value()
        g.amp3 = self.amp3_slider.value()

        g.noise_level = self.noise_slider.value()
        g.waveform = self.wave_selector.currentText()
        g.filter_type = self.filter_selector.currentText()
        g.cutoff_freq = self.cutoff_slider.value()
        g.time_window = self.time_slider.value()
        g.carrier_freq = self.carrier_slider.value()
        g.mod_freq = self.mod_slider.value()
        g.mod_index = self.index_slider.value() / 100

    def generate_signal(self):
        g = self.generator
        t = np.linspace(
            0,
            g.time_window,
            1000
        )
        if g.waveform == "Signal Composer":
            y = g.generate_composer(
                t + self.phase
            )
        else:
            y = g.generate(
                t + self.phase
            )
        if g.filter_type != "None":
            y = g.apply_filter(
                y,
                1000
            )
        return t, y

#------------------------------ PLOT UPDATES ------------------------------#

    def reset_view(self):
        self.wave_plot.enableAutoRange()
        self.fft_plot.enableAutoRange()
        
    def update_fft(self, y):
        freq, mag = FFTAnalyzer.compute(
            y,
            1000
        )

        self.fft_curve.setData(
            freq,
            mag
        )

    def update_waveform_plot(self, t, y):
        self.curve.setData(
            t,
            y
        )
        
    def update_measurements(self, y):
        self.rms_label.setText(f"RMS: {Measurements.rms(y):.2f}")

        self.peak_label.setText(f"Peak: {Measurements.peak(y):.2f}")

        self.ptp_label.setText(
            f"Peak-to-Peak: {Measurements.peak_to_peak(y):.2f}"
        )

        self.avg_label.setText(f"Average: {Measurements.average(y):.2f}")

    def update(self):
        self.sync_generator_settings()

        t, y = self.generate_signal()

        self.t = t
        self.signal = y
        self.update_fft(y)
        self.update_measurements(y)
        self.update_waveform_plot(t, y)
        self.phase += 0.01

#------------------------------ DYNAMIC UI ------------------------------#
    def update_dynamic_controls(self):
        waveform = self.wave_selector.currentText()
        filter_type = self.filter_selector.currentText()
        visibility = {
            "frequency": waveform not in [
                "AM Signal",
                "Signal Composer"
            ],
            "amplitude": waveform != "Signal Composer",
            "am": waveform == "AM Signal",
            "composer": waveform == "Signal Composer",
            "cutoff": filter_type != "None"
        }
        for group, widgets in self.control_groups.items():
            for widget in widgets:
                widget.setVisible(visibility[group])

#------------------------------ EXPORTS ------------------------------#
        
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
        self.wave_plot.grab().save(filename)
        print("Plot exported.")


