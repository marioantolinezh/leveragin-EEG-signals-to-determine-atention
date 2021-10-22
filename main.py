import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from math import pi


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('/dev/cu.usbmodem14201', 9800, timeout=1)
time.sleep(2)

data = []
for i in range(50):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
ser.close()

# build the plot
plt.plot(data)
plt.xlabel('Time(ms)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()

sampling_freq = 2000
sample_duration = 0.1
t = np.arange(0.0, sample_duration, 1/sampling_freq)
sample = data

plt.figure(figsize=(18,4))
plt.plot(t, sample)
plt.xlabel('time (s)')
plt.ylabel('signal')
plt.show()


#fir filter
filter = signal.firwin(400, [0.01, 0.06], pass_zero=False)
plt.plot(filter)
plt.show()

#fourier transform
fft_sample = signal.convolve(sample, filter, mode='same')
plt.figure(figsize=(18,4))
plt.plot(t, y, alpha=0.4)
plt.plot(t, y_clean, '--', color='green')
plt.plot(t, y2)
plt.show()

#the noisy signal (semi-transparent blue)
#the original clean signal (dashed green)
#the filtered signal (solid orange)



#references:
#https://pythonforundergradengineers.com/python-arduino-potentiometer.html
#https://www.daanmichiels.com/blog/2017/10/filtering-eeg-signals-using-scipy/
#https://www.tutorialspoint.com/python/python_gui_programming.htm


