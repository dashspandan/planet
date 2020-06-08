The popsyn.py file is the main file.

To run simulations: 

1. Edit the name of the text file in buildplanet4.py. This is the file that will have all planetary system information after simulations (includes mass of planet while crossing iceline, final semi-major axis, final mass, mass of gas accreted, mass of star, mass of disk and ordinal number of planet).
2. Run the popsyn.py file after changing any input parameters you need to.

buildplanet4.py, nextorbit.py and coeffstandard.py are function files used to simulate the planetary systems.

Some python files are provided for plotting the data e.g. newplots1.py. The main popsyn.py file itself can be modified for planet profile simulations. You can also use any files from your side for plotting.

The statistics.py file provides the percent wise distribution of planetary systems by number of planets assuming the total number of simulations is 1000. If this number is changed, tweak the file accordingly. disks.py plots the different disk mass distributions provided in the paper.

diskplanetcomp.py is the file that outputs a figure that compares simulated disks, observed disks and observed exoplanets.
