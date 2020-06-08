# Based on https://matplotlib.org/examples/axes_grid/scatter_hist.html

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

x = np.loadtxt('lupus_real_1000.txt', delimiter=',')

icemass = x[:,0]
final_sa = x[:,1]
final_mass = x[:,2]


fig, axScatter = plt.subplots(figsize=(6., 6.))

# the scatter plot:
axScatter.scatter(final_sa, final_mass, s = 0.01, color = 'grey')
#axScatter.set_aspect(1.)
axScatter.set(xscale="log", yscale="log")
axScatter.set_yticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])
axScatter.set_xlim(5e-3, 1.)
axScatter.set_ylim(1e-5,1e1)
#axScatter.scatter(final_sa,final_mass,color = 'grey', s = 0.05)
#axScatter.tick_params(labelsize = 6)
axScatter.set_xlabel('Semi-major axis in AU')
axScatter.set_ylabel('Mass of planet in $M_{\oplus}$')

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

axScatter.errorbar(trsa_t, trm_t, yerr = trmerr_t, color = 'red', fmt='o', label = 'TRAPPIST-1 system', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_yz, trm_yz, yerr = trmerr_yz, color = 'darkgreen', fmt='o', label = 'YZ Cet system', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_gj, trm_gj, yerr = trmerr_gj, color = 'magenta', fmt='o', label = 'GJ3323 system', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_lh, trm_lh, yerr = trmerr_lh, color = 'y', fmt='o', label = 'LHS 1140 system', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_pb, trm_pb, yerr = trmerr_pb, color = 'black', fmt='o', label = 'Proxima Cen b', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_gb, trm_gb, yerr = trmerr_gb, color = 'cyan', fmt='o', label = 'GJ 1214b', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_32, trm_32, yerr = trmerr_32, color = 'darkorange', fmt='o', label = 'GJ 1132 system', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_ro, trm_ro, yerr = trmerr_ro, color = 'purple', fmt='o', label = 'Ross 128b', ms = 2, elinewidth = 0.5)
axScatter.errorbar(trsa_tee, trm_tee, yerr = trmerr_tee, color = 'gold', fmt='o', label = 'Teegarden star system', ms = 2, elinewidth = 0.5)
#axScatter.legend(prop={'size': 6}, loc = 3)

# create new axes on the right and on the top of the current axes
# The first argument of the new_vertical(new_horizontal) method is
# the height (width) of the axes to be created in inches.
divider = make_axes_locatable(axScatter)
#axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=axScatter)
axHistx = divider.append_axes("top", 1.2, pad = 0.1, sharex=axScatter)
#axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=axScatter)
axHisty = divider.append_axes("right", 1.2, pad = 0.1, sharey=axScatter)

# make some labels invisible
plt.setp(axHistx.get_xticklabels() + axHisty.get_yticklabels(), visible=False)

# now determine nice limits by hand:
#binwidth = 0.25
#xymax = np.max([np.max(np.fabs(final_sa)), np.max(np.fabs(final_mass))])
#lim = (int(xymax/binwidth) + 1)*binwidth

#bins = np.arange(-lim, lim + binwidth, binwidth)
binsx = np.logspace(np.log10(5.e-3),np.log10(1.), 40)
binsy = np.logspace(np.log10(1.e-5),np.log10(1e1), 40)
axHistx.hist(final_sa, bins=binsx)
axHisty.hist(final_mass, bins=binsy, orientation='horizontal')

# the xaxis of axHistx and yaxis of axHisty are shared with axScatter,
# thus there is no need to manually adjust the xlim and ylim of these
# axis.

#axHistx.axis["bottom"].major_ticklabels.set_visible(False)
for tl in axHistx.get_xticklabels():
    tl.set_visible(False)
axHistx.set_yticks([0, 200])
axHistx.set_title('Run 4')

#axHisty.axis["left"].major_ticklabels.set_visible(False)
for tl in axHisty.get_yticklabels():
    tl.set_visible(False)
axHisty.set_xticks([0, 200])

#plt.title('Distribution of planets', size = 12)
#plt.xlabel('Semi-major axis in AU', size = 8)
#plt.ylabel('Mass of planet in $M_{\oplus}$', size = 8)

#fig.set_size_inches(width, height)
plt.draw()
fig.savefig('run4.pdf')
