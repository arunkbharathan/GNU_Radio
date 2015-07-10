#!/usr/bin/env python
# Copyright Rondeau Research, 2014

from gnuradio import gr, digital
from gnuradio import filter
from gnuradio import blocks
import sys

import scipy
from scipy import fftpack
from matplotlib import pyplot as plt
import matplotlib

def main():
    N = 10000
    fs = 100e3
    Ts = 1.0/fs
    t = scipy.arange(0, N*Ts, Ts)

    # When playing with the number of channels, be careful about the
    # filter specs and the channel map of the synthesizer set below.
    # The two synthesis filterbanks must also each have an even number
    # of channels.
    nchans = 6
    nchans0 = 4
    nchans1 = nchans - nchans0

    # Build the filters
    bw = fs/2  # Bandwidth of the channel
    tb = fs/5  #20e3
    proto_taps = filter.firdes.low_pass_2(1, nchans*fs,
                                          bw, tb, 80,
                                          filter.firdes.WIN_BLACKMAN_hARRIS)

    # Each synthesis filter is based on the number of channels it will
    # recombine.
    syn0_taps = filter.firdes.low_pass_2(nchans/2, nchans0*fs,
                                         bw, tb, 80,
                                         filter.firdes.WIN_BLACKMAN_hARRIS)
    syn1_taps = filter.firdes.low_pass_2(nchans/2, nchans1*fs,
                                         bw, tb, 80,
                                         filter.firdes.WIN_BLACKMAN_hARRIS)

    tpc = int(scipy.ceil(len(proto_taps)/float(nchans)))
    print "Filter length: ", len(proto_taps)
    print "Taps/Channel: {0} ({1})".format(tpc, len(proto_taps)/float(nchans))

    # Construct the filterbanks
    channelizer = filter.pfb.channelizer_ccf(nchans, proto_taps, 2)
    synthesizer0 = filter.pfb_synthesizer_ccf(nchans0, syn0_taps, True)
    synthesizer1 = filter.pfb_synthesizer_ccf(nchans1, syn1_taps, True)

    synthesizer0.set_channel_map([ 7, 0, 1, 2, 3, 4, 5, 6])

    nfft = 10000

    src = blocks.vector_source_c(10*[0,] + [1,] + (nfft-11)*[0,], False)
    snk0 = blocks.vector_sink_c()
    snk1 = blocks.vector_sink_c()

    tb = gr.top_block()
    tb.connect(src, channelizer)
    tb.connect(synthesizer0, snk0)
    tb.connect(synthesizer1, snk1)

    snks = []

    # Plug the first nchans0 channels from the channelizer to the
    # first synthesis filterbank.
    for i in xrange(nchans0):
        snks.append(blocks.vector_sink_c())
        tb.connect((channelizer,i), snks[i])
        tb.connect((channelizer,i), (synthesizer0,i))

    # Now connect the last nchans - nchans0 channels into the second
    # synthesis filterbank.
    j = 0
    for i in xrange(nchans0, nchans):
        snks.append(blocks.vector_sink_c())
        tb.connect((channelizer,i), snks[i])
        tb.connect((channelizer,i), (synthesizer1,j))
        j += 1
    tb.run()

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    fig1 = plt.figure(1, figsize=(12,10), facecolor='w')
    sp11 = fig1.add_subplot(1,1,1)
    H = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(proto_taps, nfft))))
    freq = scipy.linspace(-2*nchans*fs/2, 2*fs*nchans/2, nfft)
    sp11.plot(freq, H, linewidth=3)
    sp11.grid()
    sp11.set_xlim([-2*nchans*fs/2, 2*fs*nchans/2])
    sp11.set_ylim([-160, 20])
    sp11.set_xlabel("Frequency (Hz)", fontsize=18, fontweight='bold')
    sp11.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')

    # Plot the results. We will plot each channelizer output on one
    # subfigure and the output of each synthesis filterbank in two
    # other subfigures so that we can properly represent the frequency
    # domain or each.
    fig2 = plt.figure(2, figsize=(12,10), facecolor='w')
    data = []
    sp21 = plt.subplot2grid((2,2), (0,0), colspan=2)
    sp22 = plt.subplot2grid((2,2), (1,0))
    sp23 = plt.subplot2grid((2,2), (1,1))
    for i in xrange(nchans):
        data.append(scipy.array(snks[i].data()))

        X = 10.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(data[0], nfft))))

        freq = scipy.linspace(-2*fs/2, 2*fs/2, nfft)

        if(i == nchans/2):
            f0 = scipy.linspace(fs*(nchans/2 - 1), fs*(nchans/2), nfft/2)
            f1 = scipy.linspace(-fs*(nchans/2), -fs*(nchans/2 - 1), nfft/2)
            p = sp21.plot(f0, X[0:nfft/2], linewidth=2)
            sp21.plot(f1, X[nfft/2:nfft], color=p[0].get_color(), linewidth=2)
        else:
            x = i
            if(x > nchans/2):
                x -= nchans
            f0 = scipy.linspace(-fs, fs, nfft)
            f0 = f0 + x*fs
            sp21.plot(f0, X, linewidth=2)

    data_s0 = scipy.array(snk0.data())
    Y0 = 10.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(data_s0, nfft))))
    data_s1 = scipy.array(snk1.data())
    Y1 = 10.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(data_s1, nfft))))
    freq0 = scipy.linspace(-2*nchans0*fs/2, 2*fs*nchans0/2, nfft)
    freq1 = scipy.linspace(-2*nchans1*fs/2, 2*fs*nchans1/2, nfft)
    sp22.plot(freq0, Y0, linewidth=3)
    sp23.plot(freq1, Y1, linewidth=3)

    sp21.grid()
    sp21.set_xticks(map(lambda x: x*fs, range(-nchans/2, nchans/2+1)))
    #sp21.set_xticklabels([-nchans*fs/2/1000, -nchans*fs/4/1000, 0, nchans*fs/4/1000, fs*nchans/2/1000])
    sp21.set_xticklabels(map(lambda x: x*fs/1000.0, range(-nchans/2, nchans/2+1)))

    sp22.grid()
    sp22.set_xlim([-2*nchans0*fs/2, 2*nchans0*fs/2])
    sp22.set_ylim([-80, 5])
    sp22.set_xticks(map(lambda x: x*fs, range(-2*nchans0/2, 2*nchans0/2+1, 2)))
    sp22.set_xticklabels(map(lambda x: x*fs/1000.0, range(-2*nchans0/2, 2*nchans0/2+1, 2)))

    sp23.grid()
    sp23.set_xlim([-2*nchans1*fs/2, 2*nchans1*fs/2])
    sp23.set_ylim([-80, 5])
    sp23.set_xticks(map(lambda x: x*fs, range(-2*nchans1/2, 2*nchans1/2+1, 1)))
    sp23.set_xticklabels(map(lambda x: x*fs/1000.0, range(-2*nchans1/2, 2*nchans1/2+1, 1)))

    sp21.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp21.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    sp22.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp22.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    sp23.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp23.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')

    fig1.tight_layout()
    fig2.tight_layout()

    #fig1.savefig("2x_prototype_filter.png",
    #             dpi=300, format='png',
    #             facecolor='w', edgecolor='w')
    #
    fig2.savefig("2x_chan_and_synth.png",
                 dpi=300, format='png',
                 facecolor='w', edgecolor='w')


    plt.show()

if __name__ == "__main__":
    main()
