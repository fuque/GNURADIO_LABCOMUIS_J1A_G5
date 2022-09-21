#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 UIS.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
import math
from gnuradio import gr

class SumaVectorJ1B(gr.sync_block):
	"""
	docstring for block SumaVectorJ1B
	"""
	def __init__(self, Param1):
		self.Param1 = Param1
		gr.sync_block.__init__(self,
		name="SumaVectorJ1B",
		in_sig=[(numpy.float32,int(self.Param1))],
		out_sig=[numpy.float32, ])


	def work(self, input_items, output_items):
		in0 = input_items[0]
		out = output_items[0]
		# <+signal processing here+>
		for i in range(len(in0)):
			out[i] = math.fsum(in0[i,:])
		return len(output_items[0])
