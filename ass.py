
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from tkinter import filedialog
import wave
from scipy import *
from scipy.io.wavfile import read
import soundfile as sf
import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
from matplotlib import *
from pytest import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk, FigureCanvasTk, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import contextlib



class firstApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,PageOne,PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()







class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label= tk.Label(text="Assignment#1 \n Anas Sheikh \n 14l-4521")
        label.pack(padx=10,pady=10)
        button1 = ttk.Button(self, text="Plot Audio Signals", command=lambda: test())   #controller.show_frame(PageOne)
        button1.place(x=100,y=600)

        button2 = ttk.Button(self, text="Plot FFT of audio File", command=lambda : plotfft2())
        button2.place(x=500, y=600)

        label1= ttk.Label(self, text="Frequency   ----------->")
        label1.place(x=200, y=405)

        label2= ttk.Label(self, text="Frequency   ----------->")
        label2.place(x=590, y=500)

        time = tk.IntVar()
        time = duration()
        label3= ttk.Label(self, text=time)
        label3.place(x=500, y=480)




        '''
        button3 = ttk.Button(self, text="button3", command=lambda: controller.show_frame(PageOne))
        button3.pack(padx=10, pady=10)
        '''




class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        button4 = tk.Button(self, text="Back to Start", command=lambda: controller.show_frame(StartPage))
        button4.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button4 = tk.Button(self, text="Back to Start", command=lambda: controller.show_frame(StartPage))
        button4.pack()
        # read audio samples










def test():
    input_data = read("/Users/anasheikh/Desktop/Strawberries.wav")

    audio = input_data[1]
    # plot the first 1024 samples
    plt.plot(audio[0:1024])
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    # set the title
    plt.title("Sample Wav")
    # display the plot
    #plt.show()
    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.plot(audio[0:1024])
    canvas = FigureCanvasTkAgg(f)
    #canvas.draw()
    canvas.get_tk_widget().place(x=6, y=6)

    toolbar = NavigationToolbar2Tk(canvas)
    toolbar.update()
    canvas._tkcanvas.place(x=300,y=300)




def plotfft():
    # Seed the random number generator
    np.random.seed(1234)

    time_step = 0.02
    period = 5.

    time_vec = np.arange(0, 20, time_step)
    sig = (np.sin(2 * np.pi / period * time_vec)
           + 0.5 * np.random.randn(time_vec.size))

    plt.figure(figsize=(6, 5))
    plt.plot(time_vec, sig, label='Original signal')
    # The FFT of the signal
    sig_fft = fftpack.fft(sig)

    # And the power (sig_fft is of complex dtype)
    power = np.abs(sig_fft)

    # The corresponding frequencies
    sample_freq = fftpack.fftfreq(sig.size, d=time_step)

    # Plot the FFT power
    plt.figure(figsize=(6, 5))
    plt.plot(sample_freq, power)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('plower')

    # Find the peak frequency: we can focus on only the positive frequencies
    pos_mask = np.where(sample_freq > 0)
    freqs = sample_freq[pos_mask]
    peak_freq = freqs[power[pos_mask].argmax()]

    # Check that it does indeed correspond to the frequency that we generate
    # the signal with
    np.allclose(peak_freq, 1. / period)

    # An inner plot to show the peak frequency
    axes = plt.axes([0.55, 0.3, 0.3, 0.5])
    plt.title('Peak frequency')
    plt.plot(freqs[:8], power[:8])
    plt.setp(axes, yticks=[])
    high_freq_fft = sig_fft.copy()
    high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
    filtered_sig = fftpack.ifft(high_freq_fft)

    plt.figure(figsize=(6, 5))
    plt.plot(time_vec, sig, label='Original signal')
    plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    plt.legend(loc='best')

    plt.show()

def plotfft2():

    rate, data = wav.read("/Users/anasheikh/Desktop/agony.wav")
    fft_out = fft(data)
    t = plt.plot(data, np.abs(fft_out))
    #plt.show()
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(fft_out)
    canvas = FigureCanvasTkAgg(f)
    # canvas.draw()
    canvas.get_tk_widget().place(x=500, y=6)

    toolbar = NavigationToolbar2Tk(canvas)
    toolbar.update()
    canvas._tkcanvas.place(x=600, y=300)


def duration():
    f = sf.SoundFile("/Users/anasheikh/Desktop/strawberries.wav")
    print('samples = {}'.format(len(f)))
    print('sample rate = {}'.format(f.samplerate))
    length1 = print('seconds = {}'.format(len(f) / f.samplerate))
    print(length1)
    return length1


app = firstApp()
app.geometry("1000x1000")
app.title("My First HCI Assignment")
app.mainloop()


