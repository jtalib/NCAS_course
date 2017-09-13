import numpy as np

def quad_wrong(a,b,c):
	return (-b+np.sqrt(b**2.0 - 4.*a*c)/(2*a), -b-np.sqrt(b**2.0 - 4.*a*c)/(2*a))

def quad_correct(a,b,c):
	return ((-b+np.sqrt(b**2.0 - 4.*a*c))/(2*a), (-b-np.sqrt(b**2.0 - 4.*a*c))/(2*a))

def moist_static_energy_calculation(temp,geopotential,specific_humidity):
	cp = 1004.0
	g = 9.81
	Lv = 2.501e6	
	return (cp*temp)+(g*geopotential)+(Lv*specific_humidity)
