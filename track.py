import os
import wave
import threading # for looping tracks
import sys

import pyaudio # to play the looped tracks
import simpleaudio as sa # to play simple tracks -> should maybe move all to pyaudio?

# helper function
def play_wav(name):
    ''' Play audio file name and return its playing object'''
    w = sa.WaveObject.from_wave_file(name)
    pl = w.play()
    # will make the code wait rathe than execute the lines below
#    pl.wait_done()
    return pl



class Track(threading.Thread):
    '''
    looped track
    '''


    def __init__(self, filepath) :
        super(Track, self).__init__()
        self.filepath = filepath
        self.loop = True # when set false, the track will stop playing
        self.chunk = 1024

    def run(self):
        ''' overridden '''
        # start playing
        wf = wave.open(self.filepath, 'rb')
        pl = pyaudio.PyAudio()

        # Open Output Stream (basen on PyAudio tutorial)
        stream = pl.open(format = pl.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True)

        # PLAYBACK LOOP
        while self.loop:
            data = wf.readframes(self.chunk)
            stream.write(data)

            if data == b'' : # If file is over then rewind.
                wf.rewind()

        stream.close()
        pl.terminate()



    def stop(self):
        self.loop = False
