""" great work """
import numpy as np
import matplotlib.pyplot as plt
execfile("initial.py")
execfile("numerical_methods.py")
execfile("plotting.py")

if __name__ == "__main__":
	# function that creates constants needed to initialise model.
	# put in number of x points, change in time and total number of timesteps.	
	nx,dt,dx,total_nt,x = initial_constants(200,0.001,100)
	initial_phi_curve = initial_curve(x)
	initial_phi_square = initial_square(x)
	
	# FTCS for all time-steps.
	phi_FTCS, phi = FTCS(initial_phi_square,total_nt)

	# CTCS
	phi_new, phi = FTCS(initial_phi_square,1)
	phi_CTCS = CTCS(phi_new,phi,total_nt-1)

	fig = plt.figure(figsize=[12,12])
	f, ax = plt.subplots(2, 2, sharex=True,figsize=[12,12])

	plotting_2_by_2_subplot(0,0,x,[initial_phi_square,phi_FTCS,phi_CTCS],\
				['--','--','--'],['Initial','FTCS','CTCS'],\
				['r','b','g'],'Initial Square',ylim_limits=[-0.1,1.1],legend='yes')
	plotting_2_by_2_subplot(0,1,x,[phi_FTCS-phi_CTCS],\
				['-'],['FTCS - CTCS'],\
				['k'],'Difference')
	    
	# FTCS for all time-steps.
	phi_FTCS, phi = FTCS(initial_phi_curve,total_nt)

	# CTCS
	phi_new, phi = FTCS(initial_phi_curve,1)
	phi_CTCS = CTCS(phi_new,phi,total_nt-1)

	plotting_2_by_2_subplot(1,0,x,[initial_phi_curve,phi_FTCS,phi_CTCS],\
				['--','--','--'],['Initial','FTCS','CTCS'],\
				['r','b','g'],'Initial Curve',ylim_limits=[-0.1,1.1],legend='yes')

	plotting_2_by_2_subplot(1,1,x,[phi_FTCS-phi_CTCS],\
				['-'],['FTCS - CTCS'],\
				['k'],'Difference')

	plt.suptitle('Burger Number Investigation - JT',fontsize=12.0)
	plt.tight_layout()
	plt.show()
	plt.close()


