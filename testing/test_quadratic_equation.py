# script to test the quadratic equation.
import numpy as np
from quadratic import quad_wrong, quad_correct, moist_static_energy_calculation

def test_quadratic_equation():
	'''quadratic test when a=1, b=5 and c=4'''
	assert quad_correct(1.,5.,4.) == (-1.0, -4.0)

def test_quadratic_eqaution_2():
	assert quad_wrong(1.,5.,4.) == (-1.0,-4.0)

def test_MSE_calculation():
	''' calculating MSE energy with test values of T = 300K, z = 1m and Q = 0.018'''
	assert moist_static_energy_calculation(300,1,0.018) == 346227.81




