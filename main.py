import sounddevice as sd
import soundfile as sf
from tkinter import *


def Voice():
    fs = 48000

    duration = 5
    myrecording = sd.rec(int(duration*fs),
                         samplerate=fs, channels=2)
    return sf.write('my_Aufio_file.flac', myrecording, fs)

master = Tk()
Label(master, text=' Voice Recoder : ').grid(row=0,
                                             sticky=W, rowspan=5)

Button(master, text='Start', command=Voice).grid(row=0,
                                                 column=2,
                                                 columnspan=2,
                                                 rowspan=2,
                                                 padx=5,
                                                 pady=5)

mainloop()
