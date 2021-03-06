import os
import pandas as pd
import matplotlib
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

matplotlib.style.use('fivethirtyeight')

os.chdir('/Users/Carsten/Dropbox/Code/CentralPlaceWiki/Python Plots/Incoming references - plots')

cities = pd.read_csv('All Incoming references - all cities DE.csv', sep=',')
upper  = pd.read_csv('All Incoming references - upper centers.csv', sep=',')
middle = pd.read_csv('All Incoming references - middle centers.csv', sep=',')

# make 0.1 step bins from 0 to 15:
ints = range(0,150,1)
bins = [ (float(x)/10.0) for x in ints ]

pyplot.hist(np.log(cities['incoming']).dropna(), normed=True, bins=bins, alpha=0.5, label='All cities')
pyplot.hist(np.log(middle['incoming']).dropna(), normed=True, bins=bins, alpha=0.5, label='Middle centers')
pyplot.hist(np.log(upper['incoming']), normed=True, bins=bins, alpha=0.5, label='Upper centers')

ticks = bins[0::20]
pyplot.xticks(ticks, [int(np.exp(i)) for i in ticks])

pyplot.xlabel('incoming references from cities (log scale)')
pyplot.ylabel('probability')
pyplot.legend(loc='upper right')

pyplot.savefig('hist - all incoming references.pdf', bbox_inches='tight')
pyplot.close()

# pyplot.show()
