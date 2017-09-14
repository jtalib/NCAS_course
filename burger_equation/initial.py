""" great work """
import numpy as np
import matplotlib.pyplot as plt

# function defining a sqaure
def initial_square(x):
	return np.where((x%1. > 0.25) & (x%1. < 0.75),1.,0.)
	
def initial_curve(x):
    return np.where((x%1. > 0.25) & (x%1. < 0.75),np.power(np.sin(2.*x*np.pi+(np.pi/2.)),2.),0.)

def initial_constants(nx,dt,total_nt):
    dx = 1./nx
    x = np.linspace(0,1,nx+1)
    return nx,dt,dx,total_nt,x



