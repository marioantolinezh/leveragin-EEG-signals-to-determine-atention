import serial
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


plt.close('all')
fig=plt.figure(1)
plt.ion()


i=0
x=list()
y=list()

ser = serial.Serial('/dev/cu.usbmodem14101',9600)
ser.close()
ser.open()

sampling_freq = 2000
sample_duration = 0.1
t = np.arange(0.0, sample_duration, 1/sampling_freq)

filter = signal.firwin(400, [0.01, 0.06], pass_zero=False)


while True:
        data = ser.readline()
        decoded_data = data.decode()
        stripped = float(data[0:4])
        voltage = stripped*(3.3/682) #convert to voltage (mV)
        x.append(voltage)
        y.append(i*0.1)
    
        plt.cla()
        plt.plot(y, x)
        plt.xlabel("Time [ms]")
        plt.ylabel("Voltage [mV]")
        plt.pause(0.1) 
        plt.show()
        i+=0.1
        
        sample = x[-200:]
        if(len(sample) == 200):
            fft_sample = signal.convolve(np.array(sample), filter, mode='same') #sample filtered
            fig=plt.figure(2)
            plt.ion()
            plt.plot(t, fft_sample)
            plt.xlabel('frequency (hz)')
            plt.ylabel('amplitude (mV)')
            plt.pause(0.1)
            plt.show()


#Ref: https://github.com/HighVoltages/Python-arduino-realtime-graph/blob/master/Python%20code/realtime.py 
