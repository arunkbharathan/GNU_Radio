#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/python
export PATH=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/build/python:$PATH
export LD_LIBRARY_PATH=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/build/swig:$PYTHONPATH
/usr/bin/python2 /home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/python/qa_my_qpsk_demod_cb.py 
