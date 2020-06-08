import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
from scipy.stats import expon
import csv
import random as rn

m_star_list = np.linspace(0.09, 0.2, 1000)
ratio_list1= np.linspace(0.03, 0.05, 500)
ratio_list2 = np.linspace(0.03, 0.08, 500)
ratio_list3 = np.linspace(0.03, 0.1, 500)
#a = 39

gd = np.linspace(10, 1000, 500)

m_disk_lupus = []
m_disk_ormel1 = []
m_disk_ormel2 = []
m_disk_ormel3 = []

while len(m_disk_ormel1) <= 1000:
	m = rn.choice(ratio_list1)*rn.choice(m_star_list)
	m_disk_ormel1.append(m)

while len(m_disk_ormel2) <= 1000:
	m = rn.choice(ratio_list2)*rn.choice(m_star_list)
	m_disk_ormel2.append(m)

while len(m_disk_ormel3) <= 1000:
	m = rn.choice(ratio_list3)*rn.choice(m_star_list)
	m_disk_ormel3.append(m)
	


while len(m_disk_lupus) < 1000:
	m1 = np.power(10., 1.8*np.log10(rn.choice(m_star_list))+(0.9+np.log10(rn.choice(gd))+np.log10(3e-6)))
	m_disk_lupus.append(m1)

m_disk_actual = []

with open('disks.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	if float(row[0]) >= 0.09 and float(row[0]) <= 0.2:
		m_disk_actual.append(float(row[1]))
	else:
		pass

print len(m_disk_actual)

bins = np.logspace(np.log10(1.e-6),np.log10(1.e-1), 25)

width = 3.487
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.14, bottom=.17, right=.95, top=.85)

plt.hist(m_disk_ormel1, bins = bins, label = '3-5% of star mass (Ormel)', histtype = 'step', edgecolor = 'maroon') # Ormel 2017
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)

plt.hist(m_disk_ormel2, bins = bins, label = '3-8% of star mass', histtype = 'step', edgecolor = 'grey') # Ormel 2017
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)

plt.hist(m_disk_ormel3, bins = bins, label = '3-10% of star mass', histtype = 'step', edgecolor = 'blue') # Ormel 2017
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)


plt.hist(m_disk_lupus, bins = bins, label = 'Lupus', histtype = 'step', edgecolor = 'green') # Lupus survey
plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
plt.ylabel('Frequency', size = 8)
plt.title('Number distribution of Disks', size = 10)
plt.xscale('log')
plt.legend(loc = 'upper left', prop={'size': 4})
plt.tick_params(labelsize = 6)
fig.set_size_inches(width, height)

#plt.show()

#plt.clf()

#plt.hist(m_disk_actual, bins = bins, label = 'Data from Disk Surveys', alpha = 0.3, color = 'red', edgecolor='black') # Actual masses
#plt.hist(m_disk_actual, bins = bins, label = 'Data from Disk Surveys', histtype = 'step', edgecolor='red') # Actual masses 
#plt.xlabel('Mass of Disks in M$_{\odot}$', size = 8)
#plt.ylabel('Frequency', size = 8)
#plt.title('Number distribution of Observed Disks', size = 10)
#plt.xscale('log')
#plt.legend(loc = 'upper left', prop={'size': 4})
#plt.tick_params(labelsize = 6)
#fig.set_size_inches(width, height)
fig.savefig('observeddisks.pdf')
