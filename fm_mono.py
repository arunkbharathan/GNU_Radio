#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Fm Mono
# Generated: Sun Apr 12 13:24:45 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import baz
import sip
import sys

from distutils.version import StrictVersion
class fm_mono(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Mono")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Mono")
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

        self.settings = Qt.QSettings("GNU Radio", "fm_mono")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 10
        self.samp_rate = samp_rate = 1152000
        self.range1 = range1 = 88.1
        self.quad_rate = quad_rate = 288000
        self.audio_rate = audio_rate = 48000

        ##################################################
        # Blocks
        ##################################################
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
        self._volume_counter.setRange(0, 500, 1)
        self._volume_counter.setNumButtons(2)
        self._volume_counter.setValue(self.volume)
        self._volume_tool_bar.addWidget(self._volume_counter)
        self._volume_counter.valueChanged.connect(self.set_volume)
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0, 500, 1)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_layout.addLayout(self._volume_layout)
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
          
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=int(quad_rate/audio_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
        	1024*2, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	quad_rate, #bw
        	"Quad", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        
        if float == type(float()):
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.low_pass_filter_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, audio_rate, 15000, 20000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/quad_rate), firdes.low_pass(
        	1, samp_rate, 100e3, 0.6e6, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(audio_rate, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=quad_rate,
        	audio_decimation=1,
        )
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=audio_rate, tau=75e-6)
        self.analog_agc2_xx_1 = analog.agc2_ff(1e-1, 1e-2, 1.0, 1)
        self.analog_agc2_xx_1.set_max_gain(volume)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_fm_deemph_0, 0), (self.low_pass_filter_1, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.analog_agc2_xx_1, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_fm_deemph_0, 0))    
        self.connect((self.rtl2832_source_0, 0), (self.low_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_mono")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.analog_agc2_xx_1.set_max_gain(self.volume)
        Qt.QMetaObject.invokeMethod(self._volume_counter, "setValue", Qt.Q_ARG("double", self.volume))
        Qt.QMetaObject.invokeMethod(self._volume_slider, "setValue", Qt.Q_ARG("double", self.volume))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtl2832_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 0.6e6, firdes.WIN_HAMMING, 6.76))

    def get_range1(self):
        return self.range1

    def set_range1(self, range1):
        self.range1 = range1
        Qt.QMetaObject.invokeMethod(self._range1_counter, "setValue", Qt.Q_ARG("double", self.range1))
        Qt.QMetaObject.invokeMethod(self._range1_slider, "setValue", Qt.Q_ARG("double", self.range1))
        self.rtl2832_source_0.set_frequency(self.range1*1e6)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.quad_rate)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.audio_rate, 15000, 20000, firdes.WIN_HAMMING, 6.76))

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
    tb = fm_mono()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
