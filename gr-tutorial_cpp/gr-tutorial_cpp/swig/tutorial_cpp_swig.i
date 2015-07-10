/* -*- c++ -*- */

#define TUTORIAL_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "tutorial_cpp_swig_doc.i"

%{
#include "tutorial_cpp/my_qpsk_demod_cb.h"
%}


%include "tutorial_cpp/my_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(tutorial_cpp, my_qpsk_demod_cb);
