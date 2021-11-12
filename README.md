# levering-attention-using-EEG-signals

Our goal is to design an algorithm that captures attention disruption by processing and analyzing Alpha waveband signals comming from the brain (obatined by an EEG circuit that will pre-process and amplify the waves coming from the brain). This circuit will be connected to an Arduino board that will use Serial Communication to send the data to a .py (after descarting Matlab.......) program running the main algorithm in a PC. We aim acchieving as best real time data transfer and accurate signal processing as possible by means of manipulating memory management and resources optimization.     

The program is composed of three independent files which put togeather form a connected chain, and each has a specific function:
  
  a) 'commiunications.ino' is the arduino file in charge of converting the analog to digital voltage and stablishing a serial communication with the pc through the usb cable. 
  
  b) 'main.py' is the main program which is supposed to have the final joint code which is for the moment separated in its parts:
    b.1) 'prueba_gui.py' has the GUI structure development
    b.2) 'real_time_plotter.py' has other data transfer rates which are yet to optimize
    
The goal of separating this files is having a better understand and performing an optimization of the resources.


Progress Report:
10/24
	- I am able to separate the frequency bands and observe variations int he obtained voltage amplitude in certain 		frequency band due to an increment of activity 
	- all this is done yet in one measurement with a sample frequency of 2000Hz 
  
  
To do
	- plot the original time signal with voltage measurements in the y axis (not simple steps) => see ADC range and error
	- algorithm that analyses the morphology of the frequency wave and see when the amplitude is higher and with what rate 		it changess
	- try other sampling rates and compare acccuracy
	- implement this in github
	- translate all the program to a continuous time plotting + GUI that shows increment rate of attention (amplitude of the signal in the alpha waveband)
  

11/10
	-With a confirmed sampling frequency of 0.11 seconds, I am able to compute the Fourier Transform of 200 samples, convolve the signal with the pass band filter (f1 = 8Hz and f2 = 1)
	
To do:
	-error handling ()
	-optimise code by using functions in repetitive activities
	
11/11
	- After computing frequency automatically for the 200 samples, I noticed the sampling frequency is about 10 Hz. This means a problem for the passband filter since the fir raises an error: "Invalid cutoff frequency: frequencies must be greater than 0 and less than fs/2."
	To solve this error, we are goint to take previously into account the last execution program avg_frequency (for not and making it simple I will assume previous avg_period was 0.098 seconds). For the upper passband cutoff frequency to be < fs/2, f_cutoff_2 must be < 10.1/2, this is, < 5.05. As we want an upper passband cutoff frequency of 8Hz (for the alpha waveband), we nedd a f_cutoff_2 < 8.1, this means 8.1 = fs/2, and this means fs = (must be) 16.2. For this goal, avg_period must be equal to 1/fs, that is, 61 milliseconds, while the actual sampling_period is 98ms. We need to achieve a higher sampling frequency by modifying Arduino's code. 
	
To do:
	-error handling ()
	-optimise code by using functions in repetitive activities
	-take into account previous program frequency
