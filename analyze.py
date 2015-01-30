import numpy as np
import sys
from matplotlib import pyplot as plt

# some comments about what this script does
# which will certainly conflict with what netscruff
# is typing because I have ignored the instructions about 
# multi-line comments

def analyze(filename, outputfile):
    data = np.loadtxt(fname=filename, delimiter=',')
    
    plt.figure(figsize=(10.0, 3.0))
    
    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))
    
    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))
    
    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))
    
    plt.tight_layout()
    # we just change from showing the plot to saving the
    # plot to a file
    plt.savefig(outputfile)

script = sys.argv[0]
inputfile = sys.argv[1]
outputfile = sys.argv[2]
analyze(inputfile, outputfile)
