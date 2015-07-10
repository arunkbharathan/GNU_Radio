""" Testing GDB, yay """ 

import os
from gnuradio import gr
from numpy import array
from gnuradio import blocks
import tutorial_cpp

class SquareThat(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, name="square_that")
        # "Construct the Iphase and Qphase components" 
        Iphase = array([ 1, -1, -1,  1])
        Qphase = array([ 1,  1, -1, -1])
        src_data = Iphase + 1j*Qphase;
        # "Enable Gray code" 
        gray_code =  True;
        # "Determine the expected result" 
        expected_result = (0,1,3,2)
        # "Create a complex vector source" 
        src = blocks.vector_source_c(src_data)
        qpsk_demod = tutorial_cpp.my_qpsk_demod_cb(gray_code)
       # "Instantiate the binary sink" 
        dst = blocks.vector_sink_b();
        # "Construct the flowgraph" 
        self.connect(src,qpsk_demod)
        self.connect(qpsk_demod,dst)
        # "Create the flow graph" 
        self.run ()
        # check data
        result_data = dst.data()
        
  
        

def main():
    """ go, go, go """ 
    top_block = SquareThat()
    top_block.run()

if __name__ == "__main__":
    print 'Blocked waiting for GDB attach (pid = %d)' % (os.getpid(),)
    raw_input ('Press Enter to continue: ')
    main()

