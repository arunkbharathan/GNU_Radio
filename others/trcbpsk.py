#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Trcbpsk
# Generated: Sat Mar 28 19:24:16 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import sip
import sys

from distutils.version import StrictVersion
class trcbpsk(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Trcbpsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Trcbpsk")
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

        self.settings = Qt.QSettings("GNU Radio", "trcbpsk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 16
        self.nfilts = nfilts = 32
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.qpsk_0 = qpsk_0 = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 2, 2, 1, 1).base()
        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.qam = qam = digital.constellation_rect(([3.0-4.0j, -3.0-4.0j, -3.0+4.0j, 3.0+4.0j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pcs = pcs = 0.2
        self.lms = lms = 0.000001
        self.fll = fll = 0.034
        self.excess_bw = excess_bw = 0.35
        self.cl = cl = 0.34
        self.carr_freq = carr_freq = 8000
        self.bpsk = bpsk = digital.constellation_rect(([-1, 1]), ([0, 1]), 2, 2, 1, 1, 1).base()
        self.agc = agc = 7

        ##################################################
        # Blocks
        ##################################################
        self._pcs_layout = Qt.QVBoxLayout()
        self._pcs_label = Qt.QLabel("ClockSync LBW")
        self._pcs_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._pcs_slider.setRange(0.0, 1, 0.01)
        self._pcs_slider.setValue(self.pcs)
        self._pcs_slider.setMinimumHeight(200)
        self._pcs_slider.valueChanged.connect(self.set_pcs)
        self._pcs_label.setAlignment(Qt.Qt.AlignTop)
        self._pcs_layout.addWidget(self._pcs_slider)
        self._pcs_layout.addWidget(self._pcs_label)
        self.top_grid_layout.addLayout(self._pcs_layout, 0,3,3,1)
        self._lms_layout = Qt.QVBoxLayout()
        self._lms_label = Qt.QLabel("LMS Gain")
        self._lms_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._lms_slider.setRange(0.000001, 0.1, 0.0001)
        self._lms_slider.setValue(self.lms)
        self._lms_slider.setMinimumHeight(200)
        self._lms_slider.valueChanged.connect(self.set_lms)
        self._lms_label.setAlignment(Qt.Qt.AlignTop)
        self._lms_layout.addWidget(self._lms_slider)
        self._lms_layout.addWidget(self._lms_label)
        self.top_grid_layout.addLayout(self._lms_layout, 0,4,3,1)
        self._fll_layout = Qt.QVBoxLayout()
        self._fll_label = Qt.QLabel("FLL LBW")
        self._fll_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._fll_slider.setRange(0.0, 6.28/10.0, 0.0001)
        self._fll_slider.setValue(self.fll)
        self._fll_slider.setMinimumHeight(200)
        self._fll_slider.valueChanged.connect(self.set_fll)
        self._fll_label.setAlignment(Qt.Qt.AlignTop)
        self._fll_layout.addWidget(self._fll_slider)
        self._fll_layout.addWidget(self._fll_label)
        self.top_grid_layout.addLayout(self._fll_layout, 0,5,3,1)
        self._cl_layout = Qt.QVBoxLayout()
        self._cl_label = Qt.QLabel("CL LBW")
        self._cl_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._cl_slider.setRange(0.0, 1.0, 0.01)
        self._cl_slider.setValue(self.cl)
        self._cl_slider.setMinimumHeight(200)
        self._cl_slider.valueChanged.connect(self.set_cl)
        self._cl_label.setAlignment(Qt.Qt.AlignTop)
        self._cl_layout.addWidget(self._cl_slider)
        self._cl_layout.addWidget(self._cl_label)
        self.top_grid_layout.addLayout(self._cl_layout, 0,6,3,1)
        self._agc_layout = Qt.QVBoxLayout()
        self._agc_label = Qt.QLabel("agc")
        self._agc_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._agc_slider.setRange(0, 10, 0.1)
        self._agc_slider.setValue(self.agc)
        self._agc_slider.setMinimumHeight(200)
        self._agc_slider.valueChanged.connect(self.set_agc)
        self._agc_label.setAlignment(Qt.Qt.AlignTop)
        self._agc_layout.addWidget(self._agc_slider)
        self._agc_layout.addWidget(self._agc_label)
        self.top_grid_layout.addLayout(self._agc_layout, 0,2,3,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024/2, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10/2)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        
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
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0,0,1,1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, pcs, (rrc_taps), nfilts, 16, 1.5, sps/4)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(4, excess_bw, 45, fll)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(cl, 4, False)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=False,
          log=False,
          )
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(11, 1, lms, sps/4)
        self._carr_freq_layout = Qt.QVBoxLayout()
        self._carr_freq_label = Qt.QLabel("carr_freq")
        self._carr_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Vertical, Qwt.QwtSlider.LeftScale, Qwt.QwtSlider.BgSlot)
        self._carr_freq_slider.setRange(0, 22000, 1000)
        self._carr_freq_slider.setValue(self.carr_freq)
        self._carr_freq_slider.setMinimumHeight(200)
        self._carr_freq_slider.valueChanged.connect(self.set_carr_freq)
        self._carr_freq_label.setAlignment(Qt.Qt.AlignTop)
        self._carr_freq_layout.addWidget(self._carr_freq_slider)
        self._carr_freq_layout.addWidget(self._carr_freq_label)
        self.top_grid_layout.addLayout(self._carr_freq_layout, 0,1,3,1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000)), True)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, agc)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_fll_band_edge_cc_0, 0))    
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "trcbpsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.set_taps((self.rrc_taps))

    def get_qpsk_0(self):
        return self.qpsk_0

    def set_qpsk_0(self, qpsk_0):
        self.qpsk_0 = qpsk_0

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_qam(self):
        return self.qam

    def set_qam(self, qam):
        self.qam = qam

    def get_pcs(self):
        return self.pcs

    def set_pcs(self, pcs):
        self.pcs = pcs
        Qt.QMetaObject.invokeMethod(self._pcs_slider, "setValue", Qt.Q_ARG("double", self.pcs))
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.pcs)

    def get_lms(self):
        return self.lms

    def set_lms(self, lms):
        self.lms = lms
        Qt.QMetaObject.invokeMethod(self._lms_slider, "setValue", Qt.Q_ARG("double", self.lms))
        self.digital_cma_equalizer_cc_0.set_gain(self.lms)

    def get_fll(self):
        return self.fll

    def set_fll(self, fll):
        self.fll = fll
        self.digital_fll_band_edge_cc_0.set_loop_bandwidth(self.fll)
        Qt.QMetaObject.invokeMethod(self._fll_slider, "setValue", Qt.Q_ARG("double", self.fll))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_cl(self):
        return self.cl

    def set_cl(self, cl):
        self.cl = cl
        Qt.QMetaObject.invokeMethod(self._cl_slider, "setValue", Qt.Q_ARG("double", self.cl))
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.cl)

    def get_carr_freq(self):
        return self.carr_freq

    def set_carr_freq(self, carr_freq):
        self.carr_freq = carr_freq
        Qt.QMetaObject.invokeMethod(self._carr_freq_slider, "setValue", Qt.Q_ARG("double", self.carr_freq))

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk

    def get_agc(self):
        return self.agc

    def set_agc(self, agc):
        self.agc = agc
        Qt.QMetaObject.invokeMethod(self._agc_slider, "setValue", Qt.Q_ARG("double", self.agc))
        self.analog_agc2_xx_0.set_gain(self.agc)

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
    tb = trcbpsk()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
