import tkinter
from tkinter import *

import numpy as np

from scipy import signal
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import butter, lfilter

from math import pi
import serial
import time
import matplotlib

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

top = tkinter.Tk()
 # setting the dimensions of the main window
top.geometry("500x500")
   
def avg(list):
    return sum(list)/len(list)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def do():
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('/dev/cu.usbmodem101', 9800, timeout=1)
    time.sleep(2)
    
    timestamp = list() #get the time to figure out the frequency at which for gets data    
    data = []
    counter = 0 #counts the data appended without error in order to make the time vector
    num_samples = 200
    for i in range(num_samples):
        line = ser.readline()   # read a byte string
        if line:
            timestamp.append(time.time())
            string = line.decode()  # convert the byte string to a unicode string
            #try except to catch value error, counter for # of data appended
            try:
                num = int(string) # convert the unicode string to an int
                data.append(num*(3.3/682)) # add int to data converted to voltage (mV) list
                counter += 1;
            except ValueError:
                print('value Error \n')
                pass
            
    ser.close()
    
    #analyse recording frequency
    recording_intervals = list()
    counter = 0 #counter to not calculate interval in the first recoding
    for i in range(0, len(timestamp)):
        if(counter == 0):
            counter += 1
        else:
            if counter>0:
                recording_intervals.append(timestamp[i] - timestamp[i-1])
    avg_period = avg(recording_intervals)
    avg_freq = 1/avg_period #freq is 1/sampling_period
    fs = avg_freq
    t = np.linspace(0, avg_period, num_samples, endpoint=False)
    sample = data
    
    #plotting voltage reading vs time
    plt.figure(figsize=(18,4))
    plt.plot(t, sample) #t_sample gives error
    plt.title('Potentiometer Reading vs. Time') 
    plt.xlabel('Time (ms)')
    plt.ylabel('Signal Amplitude (mV)')
    plt.grid()
    plt.show()
    
    #plotting fourier transform of the filtered signal (convolved with the butterworth filter)
    convolution = butter_bandpass_filter(sample, 8, 13, fs, order=5)
    plt.figure(figsize=(18,4))
    plt.plot(t, convolution, alpha=0.4) #he quitado t
    plt.title('Filtered signal vs. Time') 
    plt.xlabel('Time (ms)')
    plt.ylabel('Signal Amplitude (mV)')
    plt.grid()
    plt.show()
    
    #plotting power of the signal using the welch method
    f, power_signal = signal.welch(convolution, fs)
    plt.semilogy(f, power_signal)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.grid()
    plt.show()
    
    fig = Figure(figsize=(6,6))
    a = fig.add_subplot(111)
    a.plot(f, power_signal, color='blue')

    a.set_title ("my_plot", fontsize=16)
    # a.label('frequency [Hz]')
    # a.ylabel('PSD [V**2/Hz]')

    canvas = FigureCanvasTkAgg(fig, master= top)
    canvas.get_tk_widget().pack()
    canvas.draw()
        
    #only need to filter the power fot the 8-13Hz freq band
    out_freq_pow = list()
    for i in range(8,13):
        out_freq_pow.append(power_signal[i])
    return out_freq_pow

    #Curve analysis vs time performed in GUI
    
state_key = 0 #refers to the current button state
    
def readVoltageCallBack():
   #tkinter.tkMessageBox.showinfo( "Lets begin!")
   state_key = 1
   for i in range(0, 1): #does 100*avg_period secs of reading
       out = do()
       print(out)
   exit()

def exitCallBack():
   #tkinter.tkMessageBox.showinfo( "Goodbye!")
   exit()
    
def stopVoltageReadingCallBack():
    state_key = 2
    exit()
    


B = tkinter.Button(top, text ="Start Voltage Reading", command = readVoltageCallBack)
C = tkinter.Button(top, text ="Exit", command = exitCallBack)
D = tkinter.Button(top, text ="Stop Voltage Reading", command = stopVoltageReadingCallBack)
plot_button = tkinter.Button(master = top, height = 2, width = 10, text = "myplot")

B.pack()
C.pack()
D.pack()
plot_button.pack()

top.mainloop()


