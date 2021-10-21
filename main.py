%STEPS TO FOLLOW
%load data
%sample time domain data (generate time ve4ctor)
%power spectrum representation (using fft)
%
%
%
%
%
%

load EEG1_1c31; % loading data
Ts=2; % sampling period
Fs=500; %sampling frequency
[N,nu]=size(data); %obtain size of data
t=(1:N)*Ts; %generates time vector
plot(t, data)
title('EEG DATA')
xlabel('voltage (mV)')
ylabel('Time (ms)')
h1=figure
plot(t,data(:,1), 'b-') %if various channels:data is a multicolumn vector...
figure(h1);
hold on

% part-2
y=fft(data); % fft of data
ps1=abs(y).^2;% power spectrum using fft
freq=(1:N)*Fs/N;%frequency vector

%power spectrum using fft method
h2=figure
plot(freq,20*log(ps1),'b')
title('POWER SPECTRUM USING FFT METHOD')
xlabel('Frequency (Hz))')
ylabel('Power (dB)')

%power spectrum using pwelch method
[ps2,freq]=pwelch(data,chebwin(128,100),[],N,Fs);
% plotting half of the power spectrum with 50
% overlap and chebwin window of length 128
h3=figure
plot(freq,10*log10(ps2),'r')
title('POWER SPECTRUM USING PWELCH METHOD')
ylabel('Power (dB)')
xlabel('Time (ms)')

%SPECTROGRAM of channel 1
[S1,F,T] = spectrogram(data(:,1),chebwin(128,100),0,Fs);
S1=abs(S1);
h5=figure;
mesh(T,F,S1);
xlabel('Time (sec)','FontSize',14);
ylabel('Frequency (Hz)','FontSize',14);
zlabel('FastFourierTransform','FontSize',14);



%ALPHA BAND PASS FILTER (8-12)

Fs = 500;  % Sampling Frequency
Fstop1 = 7.5;             % First Stopband Frequency
Fpass1 = 8;               % First Passband Frequency
Fpass2 = 12;              % Second Passband Frequency
Fstop2 = 12.5;            % Second Stopband Frequency
Dstop1 = 0.0001;          % First Stopband Attenuation
Dpass  = 0.057501127785;  % Passband Ripple
Dstop2 = 0.0001;          % Second Stopband Attenuation
dens   = 20;              % Density Factor

% Calculate the order from the parameters using FIRPMORD.
[N, Fo, Ao, W] = firpmord([Fstop1 Fpass1 Fpass2 Fstop2]/(Fs/2), [0 1 ...
                          0], [Dstop1 Dpass Dstop2]);
% Calculate the coefficients using the FIRPM function.
b3  = firpm(N, Fo, Ao, W, {dens});
Hd3 = dfilt.dffir(b3);
x3=filter(Hd3,data);
h13=figure
plot(t,x3,'r')
title('waveform for ALPHA band')
xlabel('Time (sec)','FontSize',14);
ylabel('Frequency (Hz)','FontSize',14);


%FREQUENCY SPECTRUM OF ALPHA BAND
L=10;
Fs=500;
NFFT = 2^nextpow2(L); % Next power of 2 from length of x3
Y3 = fft(x3,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2);
% Plot single-sided amplitude spectrum ALPHA
h14=figure
plot(f,2*abs(Y3(1:NFFT/2)))
title('Single-Sided Amplitude Spectrum of ALPHA x3(t)')
xlabel('Frequency (Hz)')
ylabel('|Y3(f)|')
v
