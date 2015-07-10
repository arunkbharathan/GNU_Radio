#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Stereo Fm
# Generated: Thu Apr 23 14:42:35 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital;import cmath
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import baz
import math
import sip
import sys

from distutils.version import StrictVersion
class stereo_fm(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Stereo Fm")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Stereo Fm")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "stereo_fm")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.demod_rate = demod_rate = 192000
        self.audio_decimation = audio_decimation = 4
        self.audio_rate = audio_rate = demod_rate / audio_decimation
        self.width_of_transition_band = width_of_transition_band = audio_rate /32
        self.volume = volume = 1
        self.stereo_carr_loop_bw = stereo_carr_loop_bw = 2.0*math.pi*10/100
        self.samp_rate = samp_rate = 1000e3
        self.range1 = range1 = 88.1
        self.max_freq = max_freq = 2.0*math.pi*(80)*1e3/demod_rate
        self.loop_bw = loop_bw = 2.0*math.pi*28/100

        ##################################################
        # Blocks
        ##################################################
        self._range1_layout = Qt.QVBoxLayout()
        self._range1_tool_bar = Qt.QToolBar(self)
        self._range1_layout.addWidget(self._range1_tool_bar)
        self._range1_tool_bar.addWidget(Qt.QLabel("Tune"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._range1_counter = qwt_counter_pyslot()
        self._range1_counter.setRange(88, 108, 0.1)
        self._range1_counter.setNumButtons(2)
        self._range1_counter.setValue(self.range1)
        self._range1_tool_bar.addWidget(self._range1_counter)
        self._range1_counter.valueChanged.connect(self.set_range1)
        self._range1_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._range1_slider.setRange(88, 108, 0.1)
        self._range1_slider.setValue(self.range1)
        self._range1_slider.setMinimumWidth(200)
        self._range1_slider.valueChanged.connect(self.set_range1)
        self._range1_layout.addWidget(self._range1_slider)
        self.top_layout.addLayout(self._range1_layout)
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_layout.addWidget(self._volume_tool_bar)
        self._volume_tool_bar.addWidget(Qt.QLabel("Volume"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._volume_counter = qwt_counter_pyslot()
        self._volume_counter.setRange(0.000001, 100, 0.01)
        self._volume_counter.setNumButtons(2)
        self._volume_counter.setValue(self.volume)
        self._volume_tool_bar.addWidget(self._volume_counter)
        self._volume_counter.valueChanged.connect(self.set_volume)
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0.000001, 100, 0.01)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_layout.addLayout(self._volume_layout)
        self.stereo_carrier_pll_recovery = analog.pll_refout_cc(stereo_carr_loop_bw, -2.0*math.pi*18990/demod_rate, -2.0*math.pi*19010/demod_rate)
        self.stereo_carrier__filter = filter.fir_filter_fcc(1, firdes.complex_band_pass(
        	1, demod_rate, -19020, -18980, width_of_transition_band, firdes.WIN_HAMMING, 6.76))
        self.stereo_carr_gen = blocks.multiply_vcc(1)
        self.rtl2832_source_0 = baz.rtl_source_c(defer_creation=True, output_size=gr.sizeof_gr_complex)
        self.rtl2832_source_0.set_verbose(True)
        self.rtl2832_source_0.set_vid(0x0)
        self.rtl2832_source_0.set_pid(0x0)
        self.rtl2832_source_0.set_tuner_name("")
        self.rtl2832_source_0.set_default_timeout(0)
        self.rtl2832_source_0.set_use_buffer(True)
        self.rtl2832_source_0.set_fir_coefficients(([]))
        
        self.rtl2832_source_0.set_read_length(0)
        
        
        
        
        if self.rtl2832_source_0.create() == False: raise Exception("Failed to create RTL2832 Source: rtl2832_source_0")
        
        
        self.rtl2832_source_0.set_sample_rate(samp_rate)
        
        self.rtl2832_source_0.set_frequency(range1*1e6)
        
        
        
        self.rtl2832_source_0.set_auto_gain_mode(True)
        self.rtl2832_source_0.set_relative_gain(True)
        self.rtl2832_source_0.set_gain(1)
          
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, 192000, 2375/2, 0.4, 100))
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=demod_rate,
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(True)
        self.qtgui_const_sink_x_1.enable_grid(True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.fm_demod = analog.pll_freqdet_cf(loop_bw, max_freq, -max_freq)
        self.digital_mpsk_receiver_cc_0 = digital.mpsk_receiver_cc(2, 0, 1*cmath.pi/100.0, -0.06, 0.06, 0.5, 0.05, demod_rate/ 2375.0, 0.001, 0.005)
        self.RDS_signal_gen = blocks.multiply_vcc(1)
        self.RDS_sig_filter = filter.fir_filter_fcc(1, firdes.complex_band_pass(
        	1, demod_rate,  57000 - 1500, 57000 + 1500, width_of_transition_band, firdes.WIN_HAMMING, 6.76))
        self.RDS_carr_gen = blocks.multiply_vcc(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.RDS_carr_gen, 0), (self.RDS_signal_gen, 0))    
        self.connect((self.RDS_sig_filter, 0), (self.RDS_signal_gen, 1))    
        self.connect((self.RDS_signal_gen, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.digital_mpsk_receiver_cc_0, 0), (self.qtgui_const_sink_x_1, 0))    
        self.connect((self.fm_demod, 0), (self.RDS_sig_filter, 0))    
        self.connect((self.fm_demod, 0), (self.stereo_carrier__filter, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.fm_demod, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_mpsk_receiver_cc_0, 0))    
        self.connect((self.rtl2832_source_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.stereo_carr_gen, 0), (self.RDS_carr_gen, 1))    
        self.connect((self.stereo_carrier__filter, 0), (self.stereo_carrier_pll_recovery, 0))    
        self.connect((self.stereo_carrier_pll_recovery, 0), (self.RDS_carr_gen, 0))    
        self.connect((self.stereo_carrier_pll_recovery, 0), (self.stereo_carr_gen, 1))    
        self.connect((self.stereo_carrier_pll_recovery, 0), (self.stereo_carr_gen, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "stereo_fm")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_demod_rate(self):
        return self.demod_rate

    def set_demod_rate(self, demod_rate):
        self.demod_rate = demod_rate
        self.set_max_freq(2.0*math.pi*(80)*1e3/self.demod_rate)
        self.set_audio_rate(self.demod_rate / self.audio_decimation)
        self.stereo_carrier__filter.set_taps(firdes.complex_band_pass(1, self.demod_rate, -19020, -18980, self.width_of_transition_band, firdes.WIN_HAMMING, 6.76))
        self.stereo_carrier_pll_recovery.set_max_freq(-2.0*math.pi*18990/self.demod_rate)
        self.stereo_carrier_pll_recovery.set_min_freq(-2.0*math.pi*19010/self.demod_rate)
        self.RDS_sig_filter.set_taps(firdes.complex_band_pass(1, self.demod_rate,  57000 - 1500, 57000 + 1500, self.width_of_transition_band, firdes.WIN_HAMMING, 6.76))
        self.digital_mpsk_receiver_cc_0.set_omega(self.demod_rate/ 2375.0)

    def get_audio_decimation(self):
        return self.audio_decimation

    def set_audio_decimation(self, audio_decimation):
        self.audio_decimation = audio_decimation
        self.set_audio_rate(self.demod_rate / self.audio_decimation)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_width_of_transition_band(self.audio_rate /32)

    def get_width_of_transition_band(self):
        return self.width_of_transition_band

    def set_width_of_transition_band(self, width_of_transition_band):
        self.width_of_transition_band = width_of_transition_band
        self.stereo_carrier__filter.set_taps(firdes.complex_band_pass(1, self.demod_rate, -19020, -18980, self.width_of_transition_band, firdes.WIN_HAMMING, 6.76))
        self.RDS_sig_filter.set_taps(firdes.complex_band_pass(1, self.demod_rate,  57000 - 1500, 57000 + 1500, self.width_of_transition_band, firdes.WIN_HAMMING, 6.76))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        Qt.QMetaObject.invokeMethod(self._volume_counter, "setValue", Qt.Q_ARG("double", self.volume))
        Qt.QMetaObject.invokeMethod(self._volume_slider, "setValue", Qt.Q_ARG("double", self.volume))

    def get_stereo_carr_loop_bw(self):
        return self.stereo_carr_loop_bw

    def set_stereo_carr_loop_bw(self, stereo_carr_loop_bw):
        self.stereo_carr_loop_bw = stereo_carr_loop_bw
        self.stereo_carrier_pll_recovery.set_loop_bandwidth(self.stereo_carr_loop_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtl2832_source_0.set_sample_rate(self.samp_rate)

    def get_range1(self):
        return self.range1

    def set_range1(self, range1):
        self.range1 = range1
        self.rtl2832_source_0.set_frequency(self.range1*1e6)
        Qt.QMetaObject.invokeMethod(self._range1_counter, "setValue", Qt.Q_ARG("double", self.range1))
        Qt.QMetaObject.invokeMethod(self._range1_slider, "setValue", Qt.Q_ARG("double", self.range1))

    def get_max_freq(self):
        return self.max_freq

    def set_max_freq(self, max_freq):
        self.max_freq = max_freq
        self.fm_demod.set_max_freq(self.max_freq)
        self.fm_demod.set_min_freq(-self.max_freq)

    def get_loop_bw(self):
        return self.loop_bw

    def set_loop_bw(self, loop_bw):
        self.loop_bw = loop_bw
        self.fm_demod.set_loop_bandwidth(self.loop_bw)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = stereo_fm()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
