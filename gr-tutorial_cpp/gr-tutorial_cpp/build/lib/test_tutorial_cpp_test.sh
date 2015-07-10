#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/lib
export PATH=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/build/lib:$PATH
export LD_LIBRARY_PATH=/home/arun/Desktop/gr-tutorial_cpp/gr-tutorial_cpp/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-tutorial_cpp 
