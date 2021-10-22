import tkinter
from tkinter import messagebox as tkMessageBox

import serial
import time
import matplotlib
import matplotlib.pyplot as plt

top = tkinter.Tk()

def readVoltageCallBack():
   #tkMessageBox.showinfo( "Hello Python", "Hello World");
   # make sure checking the port name!!
   ser = serial.Serial('/dev/cu.usbmodem14201', 9800, timeout=1)
   time.sleep(2)

   data = []
   for i in range(300):
        line = ser.readline()   # read a byte string
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            num = int(string) # convert the unicode string to an int
            print(num)
            data.append(num) # add int to data list
   ser.close()

    # build the plot
   plt.plot(data)
   plt.xlabel('Time (ms)') ##ms?
   plt.ylabel('Potentiometer Reading')
   plt.title('Potentiometer Reading vs. Time')
   plt.show()

def exitCallBack():
    tkMessageBox.showinfo( "Goodbye!");
    exit();

B = tkinter.Button(top, text ="Read Voltage", command = readVoltageCallBack)
C = tkinter.Button(top, text ="Exit", command = exitCallBack)

B.pack()
C.pack()

top.mainloop()

#until figure is closed is not able to read...?
