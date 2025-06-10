from scipy.optimize import curve_fit
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

porosities = np.array([0.6565443796216106, 0.7240904185857312, 0.7919796030230958, 0.8571953565469218])
# o2_diffusion_capacities = np.array([35.5816280022055, 27.827452621993828, 19.999096976055746, 13.23108631774468])
# co2_diffusion_capacities = np.array([577.424749740426, 442.4691837108629, 369.0658853963265, 277.15377912582505])
o2_diffusion_capacities = np.array([4.049251983882865, 6.041275595427421, 3.773143284077835, 1.5530015320743695])
co2_diffusion_capacities = np.array([645.177074644361, 467.9802434081638, 383.1026062291853, 293.9070334426192])

o2_lin_popt, o2_lin_pcov = curve_fit(linear_func, porosities, o2_diffusion_capacities)
co2_lin_popt, co2_lin_pcov = curve_fit(linear_func, porosities, co2_diffusion_capacities)
o2_diff_lin_predicted = linear_func(porosities, *o2_lin_popt)
o2_lin_rmse = np.sqrt(mean_squared_error(o2_diffusion_capacities, o2_diff_lin_predicted))
co2_diff_lin_predicted = linear_func(porosities, *co2_lin_popt)
co2_lin_rmse = np.sqrt(mean_squared_error(co2_diffusion_capacities, co2_diff_lin_predicted))
print(o2_lin_rmse)
print(co2_lin_rmse)

o2_quad_popt, o2_quad_pcov = curve_fit(quadratic_func, porosities, o2_diffusion_capacities)
co2_quad_popt, co2_quad_pcov = curve_fit(quadratic_func, porosities, co2_diffusion_capacities)
o2_diff_quad_predicted = quadratic_func(porosities, *o2_quad_popt)
o2_quad_rmse = np.sqrt(mean_squared_error(o2_diffusion_capacities, o2_diff_quad_predicted))
co2_diff_quad_predicted = quadratic_func(porosities, *co2_quad_popt)
co2_quad_rmse = np.sqrt(mean_squared_error(co2_diffusion_capacities, co2_diff_quad_predicted))
print(o2_quad_rmse)
print(co2_quad_rmse)

o2_exp_popt, o2_exp_pcov = curve_fit(exponential_func, porosities, o2_diffusion_capacities, maxfev=10000)
co2_exp_popt, co2_exp_pcov = curve_fit(exponential_func, porosities, co2_diffusion_capacities, maxfev=10000)
o2_diff_exp_predicted = exponential_func(porosities, *o2_exp_popt)
o2_exp_rmse = np.sqrt(mean_squared_error(o2_diffusion_capacities, o2_diff_exp_predicted))
co2_diff_exp_predicted = exponential_func(porosities, *co2_exp_popt)
co2_exp_rmse = np.sqrt(mean_squared_error(co2_diffusion_capacities, co2_diff_exp_predicted))
print(o2_exp_rmse)
print(co2_exp_rmse)

# quadratic has best fit, so use it going forward

porosities_to_map = np.array([0.657, 0.697, 0.706, 0.723, 0.787, 0.807, 0.828, 0.822, 0.856, 0.896])

a_fit, b_fit, c_fit = o2_quad_popt
print(a_fit, b_fit, c_fit)
print(str(a_fit)+'*x^2 + '+str(b_fit)+'*x + '+str(c_fit))

a_fit, b_fit, c_fit = co2_quad_popt
print(a_fit, b_fit, c_fit)
print(str(a_fit)+'*x^2 + '+str(b_fit)+'*x + '+str(c_fit))

o2_y_fit = quadratic_func(porosities_to_map, *o2_quad_popt)
co2_y_fit = quadratic_func(porosities_to_map, *co2_quad_popt)
print(o2_y_fit)
print(co2_y_fit)
