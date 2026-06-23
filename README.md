# SignalScope



SignalScope is a Python-based signal visualization and analysis application developed as an Electronics and Communication Engineering (ECE) project. It allows users to generate, visualize, analyze, and process signals in real time through an interactive graphical interface.



---



## Screenshot



![SignalScope](assets/signalscope\_v0.8.png)



## Features



### Signal Generation



Supported waveforms:



* Sine Wave

* Square Wave

* Triangle Wave

* Sawtooth Wave

* Multi-Tone Signal Generator



### Signal Controls



* Adjustable Frequency

* Adjustable Amplitude

* Adjustable Noise Level

* Adjustable Time Window

* Numeric input boxes for precise parameter control



### Multi-Tone Signals



Generate composite signals using three independent frequency components:



The frequency controls are displayed dynamically only when Multi-Tone mode is selected.



### Signal Processing



Digital filters:



* Low Pass Filter

* High Pass Filter



The Cutoff Frequency control is automatically displayed when a filter is enabled.



### Analysis Tools



* Real-Time Waveform Visualization

* FFT Spectrum Analysis



### Signal Measurements



The application continuously computes:



* RMS Value

* Peak Value

* Peak-to-Peak Value

* Average Value



### User Interface



* Interactive PyQt6 GUI

* Real-time parameter updates

* Dynamic control visibility

* Numeric parameter entry

* Dark-themed plotting area



---



## Technologies Used



* Python 3.14

* PyQt6

* NumPy

* SciPy

* Matplotlib



---



## Installation



Clone the repository:



```bash

git clone https://github.com/VedaantP-05/SignalScope.git

cd SignalScope

```



Install dependencies:



```bash

pip install numpy scipy matplotlib pyqt6 pyqtgraph

```



Run the application:



```bash

python src/main.py

```



---



## Version History



### v0.1



* Initial release



### v0.3



* Added waveform controls and measurements



### v0.4



* Added FFT spectrum analyser



### v0.5



* Added multi-tone signal generation



### v0.6



* Added noise slider



### v0.7



* Added digital filters



### v0.8



* Added numeric input boxes beside sliders

* Added dynamic UI visibility

* Added Time Window control



---



## Author



*\*Vedaant\*\*

B.Tech Electronics and Communication Engineering

Delhi Technological University (DTU)



---



SignalScope is an educational project aimed at understanding signal generation, digital signal processing concepts, FFT analysis, filtering, and GUI development using Python.

