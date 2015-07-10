import sys
sys.path.append("..")

from pydsp import Signal
import pydsp.misc as misc
import pydsp.Modulation as Modulation
import pydsp.Window as Window
import pydsp.Filter as Filter
import math
import random
from pydsp.misc import *
import oss
import os
import string
import struct

deg0 = 1+0j
deg90 = 0+1j
deg180 = -1+0j
deg270 = 0-1j

# The symbols corresponding to the 4 possible phases
phasetable = [deg0, deg90, deg180, deg270]

# The constellation is using a gray-code to lessen the impact of errors
# so the constellation looks like this:
#       Dibit  |  Phase difference
#      --------+------------------
#         00   |   0deg
#         01   |  90deg
#         10   | 270deg
#         11   | 180deg
# This means that if a symbol is mistaken for it's neighbor, it will only
# cause a one-bit error.
pskconstellation = [0, 1, 3, 2]

def psksend(fs, freq, baudrate, data):
    # Calculate some useful values
    fs = float(fs)
    freq = float(freq)
    baudrate = float(baudrate)
    samplesperbaud = int(fs / baudrate)   
    siglen = fs / baudrate * len(data) * 4

    # Prepend start-sequence to data
    # This is used to give us a signal to identify the start of data
    # The signal generates 90deg shifts, then a 180deg phase-shift
    # which tells the receiver that data is coming.
    data = "\x66"*100 + "\x67"+data

    # Encode the data string into dibits
    # The order is big-endian, ie highest bits first 
    dibits = []
    for d in data:
        d = ord(d)
        dibits.append((d >> 6) & 3)
        dibits.append((d >> 4) & 3)
        dibits.append((d >> 2) & 3)
        dibits.append((d) & 3)

    # Encode the dibits as a differential 4-PSK baseband signal
    # We assume that a baud is an integer number of samples!
    bb_sig = []
    lastphase = 0
    for d in dibits:
        p = lastphase + pskconstellation[d]
        p %= 4
        bb_sig += [phasetable[p]] * samplesperbaud
        lastphase = p


    # Pulse-shape the baseband signal using a square-root raised-cosine filter
    # After filtering by the same filter in the receiver the net result
    # will be a raised-cosine filter
    f = Filter.FIR(fs, cplx=True)
    f.make_rrc(baudrate, 0.5, gain=0.25)
    bb_shaped = f.filter(bb_sig)

    # Upconvert the signal to 'freq' for transmission.
    m = Modulation.Quadrature(fs)
    out = m.modulate(bb_shaped, freq)

    return bb_sig, bb_shaped, out.signal


# Generate a data signal with a part of a H.P. Lovecraft poem
# Then save it in a file
fs = 44100
carrier_freq = 10000
baudrate = 2321
filename = 'outfile'

bs, bb, o = psksend(fs = fs,            # Sample frequency
                    freq = carrier_freq, # Carrier frequency
                    baudrate = baudrate,
                    data =
"""   Through the ghoul-guarded gateways of slumber,
      Past the wan-mooned abysses of night,
   I have lived o'er my lives without number,
      I have sounded all things with my sight;
   And I struggle and shriek ere the daybreak, being driven to madness
   with fright.
"""
)


f = open(filename, "w")
f.write("; Sample Rate "+str(fs)+"\n")
t = 0
for s in o:
    t += 1.0 / fs
    f.write(str(t) + " " + str(s)+"\n")

# Pad with 0's
for i in range(0, fs*3):
    t += 1.0 / fs
    f.write(str(t) + " 0\n")

f.close()

a = oss.open_audio("/dev/dsp",os.O_WRONLY )
a.format(oss.AFMT_S16_LE)
a.stereo(False)
a.speed(fs)
ss = string.join([struct.pack("h", n * 32767) for n in o], '')
a.write(ss)
a.sync()
