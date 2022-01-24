# leveraging-attention-using-EEG-signals

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
	To solve this error, we are goint to take previously into account the last execution program avg_frequency (for not and making it simple I will assume previous avg_period was 0.098 seconds). For the upper passband cutoff frequency to be < fs/2, f_cutoff_2 must be < 10.1/2, this is, < 5.05. As we want an upper passband cutoff frequency of 8Hz (for the alpha waveband), we nedd a f_cutoff_2 < 8.1, this means 8.1 = fs/2, and this means fs = (must be) 16.2. For this goal, avg_period must be equal to 1/fs, that is, 61 milliseconds, while the actual sampling_period is 98ms. We need to achieve a higher sampling frequency by modifying Arduino's code, else a higher sampling rate ADC will be needed. 
	- After doing some tests, incrementing the baud rate and trying to optimize the ADC data rate, I understood it is working at its maximum frequency, which is about 10Hz. The only solution wil be geting a new and faster ADC. 
	
To do:
	-error handling ()
	-optimise code by using functions in repetitive activities
	-take into account previous program frequency
	
	
	
11/12
	- https://blog.wildan.us/2017/11/03/arduino-fast-er-sampling-rate/ gave me the solution to my problem! I was blocked bc I could not find a way to increase the sampling rate bc I thought the clk PSC (main pre-scaler) was by default at its minimum value, but is apparently 125. So the original microprocessor ATmega328P main clk has a speed of 16MHz, and is actually working at 16MHz/PSC= 8MHz. The prescaled ADC was working at 125KHz (since each conversion takes 13 clk cicles). 
	- However, by changing the PSC value to its minimum, this is, PSC = 2, we would achieve the highest theoretical sampling rate of 615KHz. Actually, prescale values below 16 are not recommended because the ADC clock is rated. Anyway, the PSC configuration is actually not accessible in the Elegoo Uno R3 board so another option has to be considered. In the before mentioned source, the following is mentiond: 
	
	"So, in order to get the higher sampling rate of Arduino, we need to access the hardware by writing some value to the arduino register. We also need to avoid using ordinary analogRead() functions because that functions will ‘blocks’. Why is it? So, when we call analogRead(), it waits until the conversion is done. Any other process will not run until the conversion is done, which we know that the conversion itself also takes time. Solution ? INTERRUPTS!"

	Then, and ISR can be used to achieve 76 KHz. The arduino code works and its integration with the main.py code works too although the number of samples read should be increased to have a representative meassurement. However, UnicodeDecodeError and ValueError exceptions come up when trying to get the data, there is something happening when opening the serial port in the arduino and closing it, that afterwards it just shows unicode strings that are not parsable or able to decode. 
	
To do:
	-Yesterday's
	-Higher adc data resolution (at least 19 bits would be needed) although a 16bits approximation would fit too (less accuracy). 
	
15/12
	-Integration was successfully done and aimed resolution fullfilled.
	-Tests have been done confirming the algorithms accuracy-.
