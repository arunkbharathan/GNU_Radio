# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

class funct:
    def __init__(self,a=1,b=1,c=1):
        self.a = a
        self.b = b
        self.c = c
    def work(self):
        return self.a**self.b-self.c
    
def main():
    a,b,c =  np.ogrid[0:1:24j,0:1:12j,0:1:6j]
    m=funct(a,b,c)
    result = m.work()
    integral = result.mean()
    print "Approximation:", integral
    print "Exact:", np.log(2) - 0.5
    
if __name__ == "__main__":
    
    main()

    


    

# <codecell>

 np.ogrid[0:1:24j,0:1:12j,0:1:6j]

# <codecell>

np.ogrid[1:5:20j]

# <codecell>

np.ogrid?

# <codecell>


