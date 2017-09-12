""" great work """
import numpy as np
import matplotlib.pyplot as plt

# function defining a sqaure
def initial_square(x):
	return np.where((x%1. > 0.25) & (x%1. < 0.75),1,0)
	
def initial_curve(x):
    return np.where((x%1. > 0.25) & (x%1. < 0.75),np.power(np.sin(2*x*np.pi+(np.pi/2.)),2),0)

nx = 200
dt = 0.001
dx = 1./nx
total_nt = 100
# set-up initial square
x = np.linspace(0,1,nx+1)

initial_phi_curve = initial_curve(x)
initial_phi_square = initial_square(x)

def FTCS(phi,nt):
    phi_New = phi.copy()
    for t in xrange(0,nt):
        max_c = 0.0
        for j in xrange(1,nx):
            #print (j)
            c = (phi[j]*dt)/dx
            max_c = np.max([c,max_c]) 
            phi_New[j] = phi[j] - c/2.*(phi[j+1]-phi[j-1])
        print ('maximum c number at ts ', t, ' is ', max_c)
        # boundary conditions
        phi_New[0] = phi[0] - c/2.*(phi[1]-phi[nx-1])
        phi[nx] = phi[0]
        phi = phi_New.copy()
    return phi_New,phi
    
	
def CTCS(phi,phi_old,nt):
    phi_New = phi.copy()
    for t in xrange(0,nt):
        for j in xrange(1,nx):
            c = (phi[j]*dt)/dx
            phi_New[j] = phi_old[j] - c*(phi[j+1]-phi[j-1])
        phi_New[0] = phi_old[0] - c*(phi[1]-phi[nx-1])
        phi_New[nx] = phi_New[0]
        phi_old = phi.copy()
        phi = phi_New.copy()
    return phi_New

# FTCS for all time-steps.
phi_FTCS, phi = FTCS(initial_phi_square,total_nt)

# CTCS
phi_new, phi = FTCS(initial_phi_square,1)
phi_CTCS = CTCS(phi_new,phi,total_nt-1)

#fig = plt.figure(figsize=[12,12])
f, ax = plt.subplots(2, 2, sharex=True,figsize=[12,12])

ax[0,0].plot(x,initial_phi_square,'r',linestyle='--',label='initial')
ax[0,0].plot(x,phi_FTCS,'b',linestyle='--',label='FTCS')
ax[0,0].plot(x,phi_CTCS,'g',linestyle='--',label='CTCS')

ax[0,0].legend(loc='best',fontsize=12.0)
ax[0,0].set_ylim([-0.1,1.1])
ax[0,0].set_title('Initial Square')

ax[0,1].plot(x,phi_FTCS-phi_CTCS,'k',label='FTCS - CTCS')
ax[0,1].set_title('Difference, FTCS - CTCS')
    
# FTCS for all time-steps.
phi_FTCS, phi = FTCS(initial_phi_curve,total_nt)

# CTCS
phi_new, phi = FTCS(initial_phi_curve,1)
phi_CTCS = CTCS(phi_new,phi,total_nt-1)

ax[1,0].plot(x,initial_phi_curve,'r',linestyle='--',label='initial')
ax[1,0].plot(x,phi_FTCS,'b',linestyle='--',label='FTCS')
ax[1,0].plot(x,phi_CTCS,'g',linestyle='--',label='CTCS')

ax[1,1].plot(x,phi_FTCS-phi_CTCS,'k',label='FTCS - CTCS')
ax[1,1].set_title('Difference, FTCS - CTCS')

ax[1,0].set_ylim([-0.1,1.1])
ax[1,0].set_title('Initial Curve')
plt.suptitle('Burger Number Investigation - JT',fontsize=12.0)
ax[1,0].legend(loc='best',fontsize=12.0)
plt.tight_layout()
plt.show()


