import scipy.linalg
import numpy as np
import matplotlib.pyplot as plt

import pylab
import time

plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['lines.linewidth'] = 2.
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# rc('font',**{'family':'sans-serif','sans-serif':['Proxima Nova']})
# rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15., 5.),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


# import matplotlib as mpl
# label_size = 60
# mpl.rcParams['xtick.labelsize'] = label_size 
# mpl.rcParams['ytick.labelsize'] = label_size 
# mpl.rcParams['axes.labelsize'] = label_size
# mpl.rcParams['legend.fontsize'] = 50
# pylab.rcParams['xtick.major.pad']=8
# pylab.rcParams['ytick.major.pad']=8
# plt.title('title', fontsize=18)





def pretty_histogram(x, num_bins = 30, col='blue', yll=0., yul=1.):
    '''
    to make histograms visually more appealing
    '''
    if num_bins > len(x):
        num_bins = len(x)/2
    n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor=col, alpha=0.75)

    # add a 'best fit' line
#     y = [1.]*bins.size
#     l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('x')
    plt.ylabel('Probability')
#     plt.axis([0, 1, yll, yul])
    plt.grid(True)