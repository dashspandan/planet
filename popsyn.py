#simulate planet distribution given stellar and disk parameters iteration using random selections

import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import random as rn
from coeffsstandard import getcoeffdisk
from buildplanet6 import buildplanet
import matplotlib as mpl
#mpl.use('pdf')


rn.seed(rn.random()) #Initate the randomness counter

mass_list = np.linspace(0.09, 0.2, 1000).tolist()
age_list = np.linspace(1e6, 3e6, 5000).tolist()
ratio_list = np.linspace(0.03, 0.05, 500).tolist()
gd = np.linspace(10, 1000, 500) #gas to dust ratio
cmig = 0.1 #Migration parameter
sim = 1

#fig, ax = plt.subplots()
#fig.subplots_adjust(left=.15, bottom=.17, right=.95, top=.85)



while sim <= 1:
	
	rn.seed(rn.random())
	p = 1. #surface density profile factor, must be less than 2
	z_o = 0.02 # metallicity of disk
	z = 0.5   # silicate to pebble ratio (From Ormel and Yamila, personal communication)
	m_star = rn.choice(mass_list) # star mass in solar masses chosen at random
	#m_star = 0.1
		
	m_disk = rn.choice(ratio_list)*rn.choice(mass_list) #disk mass in stellar masses, Ormel 2017
	#m_disk = np.power(10., 1.8*np.log10(rn.choice(mass_list))+(0.9+np.log10(rn.choice(gd))+np.log10(3e-6))) #disk mass in stellar masses (Lupus 2016)
	#m_disk = 0.05*m_star #disk mass in stellar masses, Ormel 2017
	#m_disk = np.power(10., 1.8*np.log10(m_star)+(0.9+np.log10(1000.)+np.log10(3e-6))) #disk mass in stellar masses (Lupus 2016)
	M_dot_accre = 1e-10 # in solar masses per year
	r_out = 200. #outer radius of disk (To make sufficient pebbles)

	disk_edge = 0.0102*np.power(0.08/rn.choice(mass_list), 1./7.) #Randomize
	#disk_edge = 0.0102*np.power(0.08/m_star, 1./7.)

	iceline = 0.077*np.power((m_star/0.08), 2.) #The coeff of disk edge, the time dependance is included in buildplanet1
	tend = 0.796e6*np.power((0.08/m_star), 0.5)

	next_orbit = disk_edge
	m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff = getcoeffdisk(p, z_o, z, m_star, m_disk, M_dot_accre, r_out, cmig)
	
	count = 1 #Start from 1st planet formation
	o = rn.choice(age_list) #lifetime of disk chosen at random
	#o = 1e6
	buildplanet(0., o, m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff, next_orbit, disk_edge, iceline, m_star, m_disk, count, tend)

	print 'sim %d completed' %sim
	sim = sim+1

#TRAPPIST-1 system parameters

trm = [1.02, 1.16, 0.3, 0.77, 0.93, 1.15, 0.33]
trsa = [0.012, 0.016, 0.022, 0.029, 0.038, 0.047, 0.062]
trmuerr = [0.154, 0.142, 0.039, 0.079, 0.080, 0.098, 0.056]
trmlerr = [0.143, 0.131, 0.035, 0.075, 0.078, 0.095, 0.049]
trmerr = [trmlerr, trmuerr]

#width = 3.487
#height = width / 1.618

plt.errorbar(trsa, trm, yerr = trmerr, color = 'red', fmt='o', label = 'TRAPPIST-1 system')
plt.legend()
plt.show()

#fig.set_size_inches(width, height)
#fig.savefig('saevoltimeplotcmig10.pdf')
