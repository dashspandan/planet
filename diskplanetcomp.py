import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import random as rn


rn.seed(rn.random())

#Ansdell 2016 data of dust disks
x = [0.12, 0.14, 0.19, 0.18, 0.12, 0.19, 0.14, 0.1, 0.11, 0.13, 0.1, 0.18, 0.1, 0.18, 0.19, 0.16, 0.1, 0.1, 0.2, 0.19, 0.2, 0.1, 0.14, 0.1, 0.15, 0.16] #star mass in solar masses

y = [0.0305, 10.9915, 4.0516, 7.7648, 0.0376, 28.2109, 0.3267, 2.1182, 0.8732, 1.3286, 3.6014, 23.1586, 0.1713, 1.3955, 11.3266, 0.4596, 1.4038, 0.8314, 1.6962, 9.4506, 1.738, 3.1836, 0.2423, 0.3092, 0.1128, 1.0194] #upper limit of mass of dust disks in earth masses


a = [] #List of star masses
b = [] #List of gas disk masses
c = [] #List of dust disk masses
d = [] #Star mass list for dust disk

mass_list = np.linspace(0.09, 0.2, 1000).tolist()
gd = np.linspace(10, 1000, 500) #gas to dust ratio

while len(a) <= 1000:
	mass = rn.choice(mass_list)
	a.append(mass)
	m_disk = np.power(10., 1.8*np.log10(rn.choice(mass_list))+(0.9+np.log10(rn.choice(gd)))) #In earth masses
	b.append(m_disk)

while len(d) <= 1000:
	mass = rn.choice(mass_list)
	d.append(mass)
	m_disk = np.power(10., 1.8*np.log10(rn.choice(mass_list))+(0.9)) #In earth masses
	c.append(m_disk)

liny = [317.8 for i in mass_list]

fig, ax = plt.subplots()
#fig.subplots_adjust(left=.15, bottom=.18, right=.95, top=.85)
ax.scatter(a,b,color = 'grey', s = 2, label = 'Simulated Gas disk masses')
ax.scatter(a,c,color = 'peru', s = 2, label = 'Simulated Dust disk masses')
ax.scatter(x,y,color = 'darkblue', marker = 'D', s = 5, label = 'Maximum observed dust disk masses')
ax.plot(mass_list, liny, linestyle = 'dashed', label = 'Upper limit for most observed Gas disk masses')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(7e-2, 3e-1)
ax.set_ylim(1e-2, 1e3)
#ax.set_xticks([7e-2, 8e-2, 9e-2, 1e-1, 2e-1, 3e-1])
ax.set_yticks([1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3])
ax.set_title('Planet mass-Disk mass comparison', size = 20)
ax.set_xlabel('Mass of star in $M_{\odot}$', size = 14)
ax.set_ylabel('Mass of planets or disks in $M_{\oplus}$', size = 14)
#ax.tick_params(axis = 'both', labelsize = 6)

ax.legend(prop={'size': 6}, loc = 4)

fig.savefig('diskplanetcomp1.pdf')
fig.clf()

fig, ax = plt.subplots()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(7e-2, 3e-1)
ax.set_ylim(1e-2, 1e3)
#ax.set_xticks([7e-2, 8e-2, 9e-2, 1e-1, 2e-1, 3e-1])
ax.set_yticks([1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3])
#ax.set_title('Planet mass-Disk mass comparison', size = 20)
ax.set_xlabel('Mass of star in $M_{\odot}$', size = 14)
ax.set_ylabel('Mass of planets or disks in $M_{\oplus}$', size = 14)

#TRAPPIST-1
trm_t = [1.02, 1.16, 0.3, 0.77, 0.93, 1.15, 0.33]
trms_t = [0.089, 0.089, 0.089, 0.089, 0.089, 0.089, 0.089]
trmuerr_t = [0.154, 0.142, 0.039, 0.079, 0.080, 0.098, 0.056]
trmlerr_t = [0.143, 0.131, 0.035, 0.075, 0.078, 0.095, 0.049]
trmerr_t = [trmlerr_t, trmuerr_t]
trm_tu = [5.66]
trms_tu = [0.089]

#YZ Cent
trm_yz = [0.75, 0.98, 1.14]
trms_yz = [0.130, 0.130, 0.130]
trmuerr_yz = [0.13, 0.14, 0.17]
trmlerr_yz = [0.13, 0.14, 0.17]
trmerr_yz = [trmlerr_yz, trmuerr_yz]
trm_yzu = [2.87]
trms_yzu = [0.130]

#GJ3323

trm_gj = [2.02, 2.31]
trms_gj = [0.164, 0.164]
trmuerr_gj = [0.25, 0.50]
trmlerr_gj = [0.25, 0.50]
trmerr_gj = [trmlerr_gj, trmuerr_gj]
trm_gju = [4.33]
trms_gju = [0.164]

#LHS 1140

trm_lh = [1.81, 6.98]
trms_lh = [0.146, 0.146]
trmuerr_lh = [0.39, 0.89]
trmlerr_lh = [0.39, 0.89]
trmerr_lh = [trmlerr_lh, trmuerr_lh]
trm_lhu = [8.79]
trms_lhu = [0.146]

# Proxima cen b

trm_pb = [1.27]
trms_pb = [0.122]
trmuerr_pb = [0.19]
trmlerr_pb = [0.17]
trmerr_pb = [trmlerr_pb, trmuerr_pb]
trm_pbu = [1.27]
trms_pbu = [0.122]

# GJ1214b

trm_gb = [6.55]
trms_gb = [0.157]
trmuerr_gb = [0.98]
trmlerr_gb = [0.98]
trmerr_gb = [trmlerr_gb, trmuerr_gb]
trm_gbu = [6.55]
trms_gbu = [0.157]

# GJ1132b

trm_32 = [1.66, 2.64]
trms_32 = [0.181, 0.181]
trmuerr_32 = [0.23, 0.44]
trmlerr_32 = [0.23, 0.44]
trmerr_32 = [trmlerr_32, trmuerr_32]
trm_32u = [4.3]
trms_32u = [0.181]

# ross 128b

trm_ro = [1.35]
trms_ro = [0.168]
trmuerr_ro = [0.2]
trmlerr_ro = [0.2]
trmerr_ro = [trmlerr_ro, trmuerr_ro]
trm_rou = [1.35]
trms_rou = [0.168]

# teegarden's star system

trm_tee = [1.25, 1.33]
trms_tee = [0.08, 0.08]
trmuerr_tee = [0.68, 0.71]
trmlerr_tee = [0.22, 0.25]
trmerr_tee = [trmlerr_tee, trmuerr_tee]
trm_teeu = [2.58]
trms_teeu = [0.08]

mplu = [5.66, 2.87, 4.33, 8.79, 1.27, 6.55, 4.3, 1.35, 2.58]
mplsu = [0.089, 0.130, 0.164, 0.146, 0.122, 0.157, 0.181, 0.168, 0.08]


ax.scatter(mplsu, mplu ,color = 'deeppink', marker = 's', s = 5, label = 'Sum of planet mass')
ax.errorbar(trms_t, trm_t, yerr = trmerr_t, color = 'red', fmt='o', label = 'TRAPPIST-1 system', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_yz, trm_yz, yerr = trmerr_yz, color = 'darkgreen', fmt='o', label = 'YZ Cet system', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_gj, trm_gj, yerr = trmerr_gj, color = 'darkmagenta', fmt='o', label = 'GJ3323 system', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_lh, trm_lh, yerr = trmerr_lh, color = 'y', fmt='o', label = 'LHS 1140 system', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_pb, trm_pb, yerr = trmerr_pb, color = 'black', fmt='o', label = 'Proxima Cen b', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_gb, trm_gb, yerr = trmerr_gb, color = 'cyan', fmt='o', label = 'GJ 1214b', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_32, trm_32, yerr = trmerr_32, color = 'darkorange', fmt='o', label = 'GJ 1132 system', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_ro, trm_ro, yerr = trmerr_ro, color = 'orchid', fmt='o', label = 'Ross 128b', ms = 3, elinewidth = 0.5)
ax.errorbar(trms_tee, trm_tee, yerr = trmerr_tee, color = 'gold', fmt='o', label = 'Teegarden star system', ms = 3, elinewidth = 0.5)

ax.legend(prop={'size': 8}, loc = 1)

fig.savefig('diskplanetcomp2.pdf')
