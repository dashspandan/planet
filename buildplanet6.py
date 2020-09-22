# Grow and migrate the planets, main code

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from nextorbit import findnextorbit

def buildplanet(f, o, m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff, next_orbit, disk_edge, iceline, m_star, m_disk, count, tend): #f is total time, o is disk lifetime, coeffs are calculated growth nd migration coeffs, y is profile factor, count is ordinal number of planet others are self explanatory, tend is the end of pebble flux
	
	if f >= tend or count == 21 or next_orbit >= iceline+0.02: #No migration outwards to iceline width after iceline crossing and at most 20 planets in system
		return
	
	count = count
	a = [] #total time
	b = [] #semi-major axis
	c = [] #Internal time for each planet, starts at 0
	Mp = [] #Mass of planet

	e = next_orbit

	file1 = open("test.txt","a")
	
	w = 0. #initiate internal time (time in planet's frame of reference)

	a.append(f)

	r = iceline + 0.02 #assume width of iceline is 0.02 au
	M_p = 1e-4 # Mass of seed
	Mp.append(M_p) #Initiate mass list
	b.append(r) #Initiate semi-major axis list
	c.append(w) #Initiate internal time list
	
	#Migration Within iceline but less than isolation mass
		
	h_a = 0.05*np.power(r, 0.25)
	m_planet_isolation = 72274.11*np.power(h_a, 3.)*(1.+0.146*np.power(h_a, -0.7))*m_star
	m_iso = m_planet_isolation

	j = lambda w: a_dot_coeff*np.power(m_dot_2D_coeff*(np.power(w,0.67))+np.power(1e-4,0.33),3.)*np.exp(-a[-1]/o)
	while r > iceline and a[-1] < tend and M_p < m_planet_isolation:  #2D accretion till iceline but only till isolation mass
		h,k = integrate.quad(j, 0., w)
		r = np.power(np.add(h,np.power(iceline+0.02,y)), 1./y)
		M_p = np.power(m_dot_2D_coeff*(np.power(w,0.67))+np.power(1e-4,0.33),3.)
		Mp.append(M_p)
		c.append(w)
		a.append(w+f)
		b.append(r)
		h_a = 0.05*np.power(b[-1], 0.25)
		m_planet_isolation = 72274.11*np.power(h_a, 3.)*(1.+0.146*np.power(h_a, -0.7))*m_star
		w = w+1e2


	m1 = Mp[-1]
	ticeprime = c[-1]
	oiceprime = b[-1]
	
	#Migration within iceline when isolation mass is reached
	
	j1 = lambda w: a_dot_coeff*m1*np.exp(-a[-1]/o)
	while r > iceline and a[-1] < tend and M_p >= m_planet_isolation:  #Just migrate to iceline with isolation mass
		h,k = integrate.quad(j1, ticeprime, w)
		r = np.power(np.add(h,np.power(oiceprime,y)), 1./y)
		M_p = m1
		Mp.append(M_p)
		c.append(w)
		a.append(w+f)
		b.append(r)
		w = w+1e2

	tt1 = c[-1]	
	tice = c[-1]+f #time of crossing the iceline
	m1 = Mp[-1]

	if a[-1] < tend and a[-1] < o:
		print 'Planetesimal crosses iceline with mass %0.3f M_earth after %d years.'%(m1,a[-1])
	if a[-1] > tend and a[-1] < o:
		print 'Planetesimal crosses iceline with end mass %0.3f M_earth after %d years.'%(m1,a[-1])
	
	#Migration outside iceline with mass less than isolation mass
	
	h_a = 0.05*np.power(b[-1], 0.25)
	m_planet_isolation = 72274.11*np.power(h_a, 3.)*(1.+0.146*np.power(h_a, -0.7))*m_star
	m_iso = m_planet_isolation
	m2 = Mp[-1] #Mass after crossing iceline
	z = b[-1]
	z1 = b[-1]
	i = lambda w: a_dot_coeff*m2*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))*np.exp(-a[-1]/o)
	new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
	rad = max(new_edge, e)
	
	#Planet still growing and migrating and accretion still on, grow and migrate to orbit
	
	while Mp[-1] <= m_planet_isolation and a[-1] <= tend and z > rad: #3D accretion till isolation mass, migration equation is solved using solved mass equation
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		h_a = 0.05*np.power(b[-1], 0.25)
		m_planet_isolation = 72274.11*np.power(h_a, 3.)*(1.+0.146*np.power(h_a, -0.7))*m_star
		g,s = integrate.quad(i, tt1, w)
		z = np.power(np.power(z1,y)+g, 1./y)
		m = m2*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))
		a.append(w+f)
		c.append(w)
		b.append(z)
		Mp.append(m)
		w = w+1e2

	
	while Mp[-1] <= m_planet_isolation and a[-1] <= tend and z <= rad:
		b.append(rad)
		m_planet_isolation = 72274.11*np.power(h_a, 3.)*(1.+0.146*np.power(h_a, -0.7))*m_star
		m = m2*np.exp(m_dot_3D_coeff*(np.power(w,0.67)-np.power(tt1,0.67)))
		a.append(w+f)
		c.append(w)
		Mp.append(m)
		w = w+1e2


	if a[-1] <= o:
		print 'Planet reaches end/isolation mass after %d years with planet mass %0.3f M_earth. orbit at %0.4f AU.'%(a[-1],Mp[-1], b[-1])

	if a[-1] >= tend and m2 <= m_planet_isolation:
		print 'Planet remains at end mass after %d years with planet mass %0.3f M_earth.'%(a[-1],Mp[-1])		
		print 'No more pebble accretion as pebble flux stopped.'
				

	#Pebble flow stopped with mass < misolation, just migrate and/or stop at orbit with the mass right now
	
	m2 = Mp[-1]
	oprime = b[-1]
	z = b[-1]
	tprime = c[-1]
	i1 = lambda w: a_dot_coeff*m2*np.exp(-a[-1]/o)
	while Mp[-1] <= m_planet_isolation and a[-1] > tend and a[-1] < o and z > rad:	#Just migrate to orbit
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		g,s = integrate.quad(i1, tprime, w)
		z = np.power(np.power(oprime,y)+g, 1./y)
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

	#Pebble flow stopped after isolation mass, just migrate and/or stop at orbit
	
	m2 = Mp[-1]
	oprime = b[-1]
	z = b[-1]
	tprime = c[-1]
	i2 = lambda w: a_dot_coeff*m2*np.exp(-a[-1]/o)

	while Mp[-1] > m_planet_isolation and a[-1] < o and z > rad: #Just migrate to orbit
		new_edge = disk_edge*np.exp((2*a[-1])/(7*o))
		rad = max(new_edge, e)
		g,s = integrate.quad(i2, tprime, w)
		z = np.power(np.power(oprime,y)+g, 1./y)
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
	#plt.plot(b,Mp, linewidth = 0.5, label = str(count), zorder = 1)
	#plt.plot(np.divide(a,1e6),Mp, linewidth = 0.5, label = str(count))
	#plt.plot(np.divide(a,1e6),b, linewidth = 0.5, label = str(count))
	#plt.scatter(b[-1],Mp[-1], s = 5., zorder = 2)
	#plt.scatter(a[-1]/1e6,Mp[-1], s = 3.)
	#plt.scatter(a[-1]/1e6,b[-1], s = 3.)
	plt.xscale('log')
	plt.yscale('log')
	plt.ylim(1e-4, 3.)
	plt.xlim(0.005, 1.)
	#plt.xlim(0.01, 0.2)
	#plt.ylim(0.01, 0.2)
	#plt.xlim(9e-2, 1.2)
	plt.title('Distribution of planets', size = 22)
	#plt.title('Evolution of planets ($c_{mig}=1$)', size = 8)
	#plt.title('Semi major axis Evolution of planets ($c_{mig}=1$)', size = 8)
	plt.xlabel('Semi-major axis in AU', size = 16)
	plt.ylabel('Mass of planet in $M_{\oplus}$', size = 16)
	#plt.ylabel('Semi-major axis in AU', size = 8)
	#plt.ylabel('Mass of planet in $M_{\oplus}$', size = 8)
	#plt.xlabel('Semi-major axis in AU', size = 8)
	#plt.xlabel('Time in million years', size = 8)
	
	plt.tick_params(labelsize=14)
	#plt.tick_params(axis = 'both', labelsize = 6)
	#plt.legend(prop={'size': 4}, loc = 3)
	
	count = count + 1
	
	orbit_new = findnextorbit(m_star, Mp[-1], b[-1], iceline) 
	buildplanet(tice, o, m_dot_2D_coeff, m_dot_3D_coeff, y, a_dot_coeff, orbit_new, disk_edge, iceline, m_star, m_disk, count, tend) # Trigger planet formation when it crosses iceline

