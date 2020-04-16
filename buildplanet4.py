# Grow and migrate the planets, main code

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from nextorbit import findnextorbit

def buildplanet(f, o, m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff, next_orbit, disk_edge, iceline, m_star, m_disk, count, tend): #f is total time, o is disk lifetime, coeffs are calculated growth nd migration coeffs, y is profile factor, count is ordinal number of planet others are self explanatory, tend is the end of pebble flux
	
	if f >= tend or count == 21 or next_orbit >= iceline: #No migration outwards to iceline after iceline crossing and at most 20 planets in system
		return
	
	count = count
	a = [] #total time
	b = [] #semi-major axis
	c = [] #Internal time for each planet, starts at 0

	e = next_orbit

	file1 = open("rand_lupus_1000_m.txt","a")
	
	w = 0. #initiate internal time (time in planet's frame of reference)

	a.append(f)

	r = iceline + 0.02 #assume width of iceline is 0.02 au 
	
#	j = lambda t: (a_dot_coeff)*np.power(1.76e-4*(np.power(t,0.67))+np.power(1e-4,0.33),3.) #Just the integration to find mass (old)
	j = lambda w: a_dot_coeff*np.power(m_dot_2D_coeff*(np.power(w,0.67))+np.power(1e-4,0.33),3.)*np.exp(-a[-1]/o)
	while r > iceline and a[-1] < tend:  #2D accretion till iceline, migration equation is solved using solved mass equation
		h,k = integrate.quad(j, 0., w)
#		r = np.power(np.add(h,np.power(0.12,y)), 1./y) #old
		r = np.power(np.add(h,np.power(iceline+0.02,y)), 1./y)
		c.append(w)
		a.append(w+f)
		b.append(r)
		w = w+1e2

	M_p = np.power(m_dot_2D_coeff*(np.power(c,0.67))+np.power(1e-4,0.33),3.)
	Mp = M_p.tolist()
	tt1 = w
	tice = w+f #time of crossing the iceline
	m1 = Mp[-1]

	if a[-1] < tend and a[-1] < o:
		print 'Planetesimal crosses iceline with mass %0.3f M_earth after %d years.'%(m1,a[-1])
	
	
	h_a = 0.05*np.power(b[-1], 0.25)
	#m_planet_isolation = m_star*np.power(h_a, 3.)*333060.402
	m_planet_isolation = 20.0*np.power(h_a/0.05, 3.) #Bitsch 2015
	m_iso = m_planet_isolation
	z = iceline
	i = lambda w: a_dot_coeff*m1*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))*np.exp(-a[-1]/o)
	new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
	m2 = Mp[-1]
	rad = max(new_edge, e)
	

	while Mp[-1] <= m_planet_isolation and a[-1] <= tend and z > rad: #3D accretion till isolation mass, migration equation is solved using solved mass equation
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		h_a = 0.05*np.power(b[-1], 0.25)
		#m_planet_isolation = m_star*np.power(h_a, 3.)*333060.402
		m_planet_isolation = 20.0*np.power(h_a/0.05, 3.)
		g,s = integrate.quad(i, tt1, w)
		z = np.power(np.power(iceline,y)+g, 1./y)
		m = m1*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))
		a.append(w+f)
		c.append(w)
		b.append(z)
		Mp.append(m)
		m2 = m
		w = w+1e2

	while Mp[-1] <= m_planet_isolation and a[-1] <= tend and z <= rad:
		b.append(rad)
		m_planet_isolation = 20.0*np.power(h_a/0.05, 3.)
		#m_planet_isolation = m_star*np.power(h_a, 3.)*333060.402
		m = m1*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))
		a.append(w+f)
		c.append(w)
		Mp.append(m)
		m2 = m
		w = w+1e2


	if a[-1] <= o:
		print 'Planet reaches end/isolation mass after %d years with planet mass %0.3f M_earth. orbit at %0.4f AU.'%(a[-1],Mp[-1], b[-1])

	if a[-1] >= tend and m2 <= m_planet_isolation:
		print 'Planet remains at end mass after %d years with planet mass %0.3f M_earth.'%(a[-1],Mp[-1])		
		print 'No more pebble accretion as pebble flux stopped.'
				

	while Mp[-1] <= m_planet_isolation and a[-1] > tend and a[-1] < o and z > rad:	#Just migrate to orbit
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		g,s = integrate.quad(i, tt1, w)
		z = np.power(np.power(iceline,y)+g, 1./y)
		Mp.append(m2)
		b.append(z)
		a.append(w+f)
		c.append(w)
		w = w+1e2

	while Mp[-1] <= m_planet_isolation and a[-1] > tend and a[-1] < o and z <= rad: #Just stop there
		Mp.append(m2)
		b.append(rad)
		a.append(w+f)
		c.append(w)
		w = w+1e2

	while Mp[-1] > m_planet_isolation and a[-1] < o and z > rad: #Just migrate to orbit
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		g,s = integrate.quad(i, tt1, w)
		z = np.power(np.power(iceline,y)+g, 1./y)
		Mp.append(m2)
		b.append(z)
		a.append(w+f)
		c.append(w)
		w = w+1e2

	while Mp[-1] > m_planet_isolation and a[-1] < o and z <= rad: #Just stop there
		Mp.append(m2)
		b.append(rad)
		a.append(w+f)
		c.append(w)
		w = w+1e2
	

	print 'Planet remains at end mass after %d years with planet mass %0.3f M_earth at %.4f AU.'%(a[-1],Mp[-1], b[-1])
	
	file1.write(str(m1)+','+str(b[-1])+','+str(Mp[-1])+','+str(0.1*Mp[-1])+','+str(count)+','+str(m_star)+','+str(m_disk)+'\n')

	plt.scatter(b[-1],Mp[-1],color = 'blue')
	plt.xscale('log')
	plt.yscale('log')
	plt.title('Distribution of planets', size = 22)
	plt.xlabel('Semi-major axis in AU', size = 16)
	plt.ylabel('Mass of planet in $M_{\oplus}$', size = 16)
	plt.xlim(0.005, 1.)
	plt.tick_params(labelsize=14)
	
	count = count + 1
	
	orbit_new = findnextorbit(m_star, Mp[-1], b[-1], iceline) 
	buildplanet(tice, o, m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff, orbit_new, disk_edge, iceline, m_star, m_disk, count, tend) # Trigger planet formation when it crosses iceline

