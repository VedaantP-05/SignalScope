import sys
import numpy as np

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

from signal_generator import SignalGenerator
from oscilloscope import Oscilloscope

app = QApplication(sys.argv)
generator = SignalGenerator()
scope = Oscilloscope()

scope.plot_widget.setWindowTitle(
    "SignalScope v0.1"
)
scope.plot_widget.resize(900,500)
scope.plot_widget.show()

timer = QTimer()
phase = 0

def update():
    global phase

    t = np.linspace(
        phase,
        phase+1,
        1000
    )
    y = generator.generate_sine(t)
    scope.curve.setData(t, y)
    phase += 0.02

timer.timeout.connect(update)
timer.start(16)
sys.exit(app.exec())
