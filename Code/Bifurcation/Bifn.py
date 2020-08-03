# Bifn.py: plot a bifurcation diagram for piecewise maps.

from scipy import arange
from pylab import *

# Example: Tent map, a in [1,2]
def TentMap(a,x):
	if x < 0.5:
		return a*x
	else:
		return a*(1-x)

plow  = 1.0
phigh = 2.0


figure(1,(8,6))
# Stuff parameter range into a string via the string formating commands.
TitleString = 'Tent map bifurcation diagram for r in [%g,%g]' % (plow,phigh)
title(TitleString)
xlabel('Control parameter r')
ylabel('x')

# Set the initial condition used across the different parameters
ic = 0.2
# Establish the arrays to hold the set of iterates at each parameter value
psweep = [ ] # The parameter value
x = [ ] # The iterates
# The iterates we'll throw away
nTransients = 250
# This sets how much the attractor is filled in
nIterates = 500
# This sets how dense the bifurcation diagram will be
nSteps = 200.0
# Sweep the control parameter over the desired range
for p in arange(plow,phigh,(phigh-plow)/nSteps):
	# Set the initial condition to the reference value
	state = ic
	# Throw away the transient iterations
	for i in range(nTransients):
		state = TentMap(p,state)
	# Now store the next batch of iterates
	for i in range(nIterates):
		state = TentMap(p,state)
		psweep.append(p)
		x.append( state )

plot(psweep, x, 'k,')

# Use this to save figure as a bitmap png file
#savefig('TentBifn', dpi=600)

show()

