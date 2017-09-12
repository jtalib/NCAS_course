""" great work """
import numpy as np
import matplotlib.pyplot as plt
execfile("initial.py")
execfile("numerical_methods.py")

def plotting_2_by_2_subplot(x_loc,y_loc,x,data,linestyle_choice,label_choice,colour,set_title_choice,ylim_limits=None,legend=None):
	for i, array in enumerate(data):
		print i
		ax[x_loc,y_loc].plot(x,array,colour[i],linestyle=linestyle_choice[i],label=label_choice[i])

	if legend:
		ax[x_loc,y_loc].legend(loc='best',fontsize=12.0)
	if ylim_limits:	
		ax[x_loc,y_loc].set_ylim(ylim_limits)
	ax[x_loc,y_loc].set_title(set_title_choice)



