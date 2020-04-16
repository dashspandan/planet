#Plotting reference from https://www.robotswillkillusall.org/posts/mpl-scatterplot-colorbar.html
#https://www.bastibl.net/publication-quality-plots/

import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt

x = np.loadtxt('rand_lupus_1000_m.txt', delimiter=',')

icemass = x[:,0]
final_sa = x[:,1]
final_mass = x[:,2]


width = 3.487
height = width / 1.618

#fig, ax = plt.subplots(figsize=(width,height))
fig, ax = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.17, right=.95, top=.85)
ax.scatter(final_sa,final_mass,color = 'grey', s = 0.05)
plt.xscale('log')
plt.yscale('log')
plt.title('Distribution of planets', size = 12)
plt.xlabel('Semi-major axis in AU', size = 8)
plt.ylabel('Mass of planet in $M_{\oplus}$', size = 8)
plt.xlim(0.005, 1.)
#plt.grid()
plt.tick_params(labelsize=6)

#TRAPPIST-1
trm_t = [1.02, 1.16, 0.3, 0.77, 0.93, 1.15, 0.33]
trsa_t = [0.012, 0.016, 0.022, 0.029, 0.038, 0.047, 0.062]
trmuerr_t = [0.154, 0.142, 0.039, 0.079, 0.080, 0.098, 0.056]
trmlerr_t = [0.143, 0.131, 0.035, 0.075, 0.078, 0.095, 0.049]
trmerr_t = [trmlerr_t, trmuerr_t]

#YZ Cent
trm_yz = [0.75, 0.98, 1.14]
trsa_yz = [0.01557, 0.02090, 0.02764]
trmuerr_yz = [0.13, 0.14, 0.17]
trmlerr_yz = [0.13, 0.14, 0.17]
trmerr_yz = [trmlerr_yz, trmuerr_yz]

#GJ3323

trm_gj = [2.02, 2.31]
trsa_gj = [0.03282, 0.1264]
trmuerr_gj = [0.25, 0.50]
trmlerr_gj = [0.25, 0.50]
trmerr_gj = [trmlerr_gj, trmuerr_gj]

#LHS 1140

trm_lh = [1.81, 6.98]
trsa_lh = [0.02675, 0.0936]
trmuerr_lh = [0.39, 0.89]
trmlerr_lh = [0.39, 0.89]
trmerr_lh = [trmlerr_lh, trmuerr_lh]

# Proxima cen b

trm_pb = [1.27]
trsa_pb = [0.0485]
trmuerr_pb = [0.19]
trmlerr_pb = [0.17]
trmerr_pb = [trmlerr_pb, trmuerr_pb]

# GJ1214b

trm_gb = [6.55]
trsa_gb = [0.0143]
trmuerr_gb = [0.98]
trmlerr_gb = [0.98]
trmerr_gb = [trmlerr_gb, trmuerr_gb]

# GJ1132b

trm_32 = [1.66, 2.64]
trsa_32 = [0.0153, 0.0476]
trmuerr_32 = [0.23, 0.44]
trmlerr_32 = [0.23, 0.44]
trmerr_32 = [trmlerr_32, trmuerr_32]

# ross 128b

trm_ro = [1.35]
trsa_ro = [0.0493]
trmuerr_ro = [0.2]
trmlerr_ro = [0.2]
trmerr_ro = [trmlerr_ro, trmuerr_ro]

# teegarden's star system

trm_tee = [1.25, 1.33]
trsa_tee = [0.0252, 0.0443]
trmuerr_tee = [0.68, 0.71]
trmlerr_tee = [0.22, 0.25]
trmerr_tee = [trmlerr_tee, trmuerr_tee]

ax.errorbar(trsa_t, trm_t, yerr = trmerr_t, color = 'red', fmt='o', label = 'TRAPPIST-1 system', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_yz, trm_yz, yerr = trmerr_yz, color = 'darkgreen', fmt='o', label = 'YZ Cet system', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_gj, trm_gj, yerr = trmerr_gj, color = 'magenta', fmt='o', label = 'GJ3323 system', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_lh, trm_lh, yerr = trmerr_lh, color = 'y', fmt='o', label = 'LHS 1140 system', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_pb, trm_pb, yerr = trmerr_pb, color = 'black', fmt='o', label = 'Proxima Cen b', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_gb, trm_gb, yerr = trmerr_gb, color = 'cyan', fmt='o', label = 'GJ 1214b', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_32, trm_32, yerr = trmerr_32, color = 'darkorange', fmt='o', label = 'GJ 1132 system', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_ro, trm_ro, yerr = trmerr_ro, color = 'purple', fmt='o', label = 'Ross 128b', ms = 2, elinewidth = 0.5)
ax.errorbar(trsa_tee, trm_tee, yerr = trmerr_tee, color = 'gold', fmt='o', label = 'Teegarden star system', ms = 2, elinewidth = 0.5)
ax.legend(prop={'size': 4}, loc = 3)

ax.set_yticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])
ax.set_ylim(1e-5,1e1)
fig.set_size_inches(width, height)
fig.savefig('rand_lupus_1000_m.pdf')
#plt.show()

