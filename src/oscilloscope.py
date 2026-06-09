import pyqtgraph as pg

class Oscilloscope:
    def __init__(self):
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("k")
        self.plot_widget.showGrid(
            x = True,
            y = True
        )
        self.curve = self.plot_widget.plot(
            pen = 'y'
        )
