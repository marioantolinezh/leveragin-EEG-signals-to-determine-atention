import serial

# Import matplotlib and set the 'Qt4Agg' backend to support interactive mode on Windows and macOS
import matplotlib
#matplotlib.use('Qt4Agg')

# Activate interactive mode
import matplotlib.pyplot as plt
#plt.ion()

import numpy as np
plt.ion()
fig=plt.figure()


i=0
x=list()
y=list()
i=0
ser = serial.Serial('/dev/cu.usbmodem14201',9600)
ser.close()
ser.open()

while True:

    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())

    plt.scatter(i, float(data.decode()))
    i += 1
    plt.show()
    plt.pause(0.0001)  # Note this correction



#Ref: https://github.com/HighVoltages/Python-arduino-realtime-graph/blob/master/Python%20code/realtime.py 
