""" great work """
import numpy as np
import matplotlib.pyplot as plt

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

