# SignalScope

SignalScope is a Python-based signal visualization and analysis application developed as a personal Electronics and Communication Engineering (ECE) project. It enables users to generate, visualize, analyze, and process signals in real time through an interactive desktop interface.

---

## Screenshot

![SignalScope](https://github.com/VedaantP-05/SignalScope/blob/main/assets/signalscope_v1.0.png?raw=true)

---

## Features

### Signal Generation
- Sine Wave
- Square Wave
- Triangle Wave
- Sawtooth Wave
- Signal Composer (3 independent signal components)
- Amplitude Modulation (AM)

### Signal Controls
- Adjustable Frequency
- Adjustable Amplitude
- Adjustable Noise Level
- Adjustable Time Window
- Numeric input boxes for precise parameter control
- Dynamic UI controls

### Signal Processing
- Low-Pass Filter
- High-Pass Filter
- Real-time filtering
- FFT Spectrum Analysis

### Signal Analysis
- Real-Time Waveform Visualization
- RMS Measurement
- Peak Measurement
- Peak-to-Peak Measurement
- Average Value Measurement

### Export
- Export generated signals to CSV
- Export waveform plots as PNG
- Automatic timestamped filenames

### User Interface
- Interactive PyQt6 GUI
- Menu Bar
- Toolbar
- Reset View
- Dynamic control visibility
- Dark-themed plotting area

---

## Technologies Used

- Python
- PyQt6
- PyQtGraph
- NumPy
- SciPy

---

## Installation

Clone the repository:

```bash
git clone https://github.com/VedaantP-05/SignalScope.git
cd SignalScope
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/main.py
```

---

## Version History

| Version | Highlights |
|---------|------------|
| **v0.1** | Initial Signal Generator |
| **v0.3** | Waveform Controls & Measurements |
| **v0.4** | FFT Spectrum Analyzer |
| **v0.5** | Multi-Tone Signal Generation |
| **v0.6** | Noise Slider |
| **v0.7** | Digital Filters |
| **v0.8** | Numeric Inputs & Dynamic UI |
| **v0.9** | CSV/PNG Export & Timestamped Files |
| **v1.0** | Signal Composer, AM Modulation, Menu Bar, Toolbar & UI Improvements |

---

## Roadmap

### v1.1
- Collapsible control panels
- FM Modulation
- Save/Load Sessions
- Improved plot customization
- Keyboard shortcuts

### Future Plans
- Arduino Integration
- Live Oscilloscope Mode
- Spectrogram
- Waterfall Display
- Sensor Dashboard

---

## Author

**Vedaant**  
B.Tech Electronics and Communication Engineering  
Delhi Technological University (DTU)

---

SignalScope is an educational project focused on learning digital signal processing (DSP), signal generation, filtering, FFT analysis, and desktop application development using Python.
