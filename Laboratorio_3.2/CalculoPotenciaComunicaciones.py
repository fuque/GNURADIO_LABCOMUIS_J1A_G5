#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: CalculoPotenciaComunicaciones
# Author: J1B_G5
# Copyright: Modulos_J1BG5
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Modulos_J1B



from gnuradio import qtgui

class CalculoPotenciaComunicaciones(gr.top_block, Qt.QWidget):

    def __init__(self, l_vect=1024):
        gr.top_block.__init__(self, "CalculoPotenciaComunicaciones", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("CalculoPotenciaComunicaciones")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "CalculoPotenciaComunicaciones")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.l_vect = l_vect

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.fft_vxx_0 = fft.fft_vfc(l_vect, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, l_vect)
        self.blocks_nlog10_ff_1 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 30)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1/(2*135115.625))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(l_vect)
        self.PotenciaLogaritmicaDbw = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaLogaritmicaDbw.set_update_time(0.10)
        self.PotenciaLogaritmicaDbw.set_title("Potencia Logaritmica (Dbm)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(Dbw)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaLogaritmicaDbw.set_min(i, -1)
            self.PotenciaLogaritmicaDbw.set_max(i, 1)
            self.PotenciaLogaritmicaDbw.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaLogaritmicaDbw.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaLogaritmicaDbw.set_label(i, labels[i])
            self.PotenciaLogaritmicaDbw.set_unit(i, units[i])
            self.PotenciaLogaritmicaDbw.set_factor(i, factor[i])

        self.PotenciaLogaritmicaDbw.enable_autoscale(True)
        self._PotenciaLogaritmicaDbw_win = sip.wrapinstance(self.PotenciaLogaritmicaDbw.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaLogaritmicaDbw_win)
        self.PotenciaLogaritmicaDbm = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaLogaritmicaDbm.set_update_time(0.10)
        self.PotenciaLogaritmicaDbm.set_title("Potencia Logaritmica (Dbm)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(Dbm)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaLogaritmicaDbm.set_min(i, -1)
            self.PotenciaLogaritmicaDbm.set_max(i, 1)
            self.PotenciaLogaritmicaDbm.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaLogaritmicaDbm.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaLogaritmicaDbm.set_label(i, labels[i])
            self.PotenciaLogaritmicaDbm.set_unit(i, units[i])
            self.PotenciaLogaritmicaDbm.set_factor(i, factor[i])

        self.PotenciaLogaritmicaDbm.enable_autoscale(True)
        self._PotenciaLogaritmicaDbm_win = sip.wrapinstance(self.PotenciaLogaritmicaDbm.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaLogaritmicaDbm_win)
        self.PotenciaLinealW = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaLinealW.set_update_time(0.10)
        self.PotenciaLinealW.set_title("Potencia Lineal (W)")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['(W)', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaLinealW.set_min(i, -1)
            self.PotenciaLinealW.set_max(i, 1)
            self.PotenciaLinealW.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaLinealW.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaLinealW.set_label(i, labels[i])
            self.PotenciaLinealW.set_unit(i, units[i])
            self.PotenciaLinealW.set_factor(i, factor[i])

        self.PotenciaLinealW.enable_autoscale(False)
        self._PotenciaLinealW_win = sip.wrapinstance(self.PotenciaLinealW.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaLinealW_win)
        self.Modulos_J1B_SumaVectorJ1B_0 = Modulos_J1B.SumaVectorJ1B(l_vect)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulos_J1B_SumaVectorJ1B_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.Modulos_J1B_SumaVectorJ1B_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.PotenciaLinealW, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.PotenciaLogaritmicaDbm, 0))
        self.connect((self.blocks_nlog10_ff_1, 0), (self.PotenciaLogaritmicaDbw, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "CalculoPotenciaComunicaciones")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_l_vect(self):
        return self.l_vect

    def set_l_vect(self, l_vect):
        self.l_vect = l_vect

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--l-vect", dest="l_vect", type=intx, default=1024,
        help="Set Longitud FFT [default=%(default)r]")
    return parser


def main(top_block_cls=CalculoPotenciaComunicaciones, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(l_vect=options.l_vect)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
