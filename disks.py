import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
from scipy.stats import expon
import csv
import random as rn

m_star_list = np.linspace(0.08, 0.2, 1000)
ratio_list = np.linspace(0.03, 0.05, 100)
#a = 39

m_disk_lupus = []
m_disk_ormel = []

while len(m_disk_ormel) <= 39:
	m = rn.choice(ratio_list)*rn.choice(m_star_list)
	m_disk_ormel.append(m)
	


while len(m_disk_lupus) < 39:
	m1 = np.exp(1.8*np.log(rn.choice(m_star_list))-2.6)
	m_disk_lupus.append(m1)

m_disk_actual = []

with open('disks.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	if float(row[0]) >= 0.08 and float(row[0]) <= 0.2:
		m_disk_actual.append(float(row[1]))
	else:
		pass

bins = np.logspace(np.log10(1.e-6),np.log10(1.e-2), 10)

width = 3.487
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.14, bottom=.17, right=.95, top=.85)

plt.hist(m_disk_ormel, bins = bins, label = 'Ormel', histtype = 'step', edgecolor = 'blue') # Ormel 2017
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Ormel Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)
fig.savefig('ormeldisks.pdf')


plt.hist(m_disk_lupus, bins = bins, label = 'Lupus', histtype = 'step', edgecolor = 'green') # Lupus survey
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Lupus Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)
fig.savefig('lupusdisks.pdf')
#plt.show()

#plt.clf()

#plt.hist(m_disk_actual, bins = bins, label = 'Data from Disk Surveys', alpha = 0.3, color = 'red', edgecolor='black') # Actual masses
plt.hist(m_disk_actual, bins = bins, label = 'Data from Disk Surveys', histtype = 'step', edgecolor='red') # Actual masses 
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Observed Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)
fig.savefig('observeddisks.pdf')
