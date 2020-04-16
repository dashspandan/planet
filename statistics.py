#Ref: https://stackoverflow.com/questions/6986986/bin-size-in-matplotlib-histogram

import numpy as np
import matplotlib.pyplot as plt

def freq(value, some_list):
	
	freq = 0
	for l in some_list:
		if l == value:
			freq = freq + 1
	return freq

x = np.loadtxt('rand_lupus_1000_m.txt', delimiter=',')

icemass = x[:,0]
final_sa = x[:,1]
final_mass = x[:,2]
gas_mass = x[:,3]
count = x[:,4]
star_mass = x[:,5]
disk_mass = x[:,6]

print 'Number of planets formed is %d.'%(len(count))
print 'Average planet mass is %.3f.'%(np.mean(final_mass))

bins = np.arange(min(count), max(count)+1, 1)
print bins

f = []
for i in bins:
	freq_i = freq(i, count)
	f.append(freq_i)
	
print f

g = []

j = 0
while j < len(f)-1:
	n = f[j]-f[j+1]
	g.append(n)
	j = j + 1

print g

per = []
for h in g:
	p = 100*(float(h)/float(1000))
	per.append(p)

print per
print sum(per)
#plt.hist(count, bins)
#plt.show()
