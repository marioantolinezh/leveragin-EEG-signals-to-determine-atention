# levering-attention-using-EEG-signals

Our goal is to design an algorithm that captures attention disruption by processing and analyzing Alpha waveband signals comming from the brain (obatined by an EEG circuit that will pre-process and amplify the waves coming from the brain). This circuit will be connected to an Arduino board that will use Serial Communication to send the data to a .py (after descarting Matlab.......) program running the main algorithm in a PC. We aim acchieving as best real time data transfer and accurate signal processing as possible by means of manipulating memory management and resources optimization.     

The program is composed of three independent files which put togeather form a connected chain, and each has a specific function:
  
  a) 'commiunications.ino' is the arduino file in charge of converting the analog to digital voltage and stablishing a serial communication with the pc through the usb cable. 
  
  b) 'main.py' is the main program which is supposed to have the final joint code which is for the moment separated in its parts:
    b.1) 'prueba_gui.py' has the GUI structure development
    b.2) 'real_time_plotter.py' has other data transfer rates which are yet to optimize
    
    The goal of separating this files is having a better understand and performing an optimization of the resources.


Progress Report:

  
