import numpy as np

def findnextorbit(m_star, m_planet, disk_edge, iceline): #Note disk_edge is orbit of planet before in ordinal number

	m_star = m_star #solar masses
	m_star_kg = np.multiply(m_star, 1.989e30)
	m_planet = m_planet # earth masses, preferable the isolation mass
	m_planet_kg = np.multiply(m_planet, 5.972e24)
	disk_edge = disk_edge # in au
	factor = np.power(np.divide(m_planet_kg, 3.*m_star_kg), 1./3.)

	d = disk_edge

	c = 5.*d*factor
	b = d+c


	return b
