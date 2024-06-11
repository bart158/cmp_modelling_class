import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def linf(x, a, b):
    return a*x + b

data_raw = np.loadtxt('no_noise/tau_plot.txt')

mask = np.where(data_raw[1], True, False)
datax = data_raw[0, mask]
datay = data_raw[1, mask]
data = np.array([datax, datay])

popt, pcov = curve_fit(linf, np.log(data[0]), np.log(data[1]))

x = np.log(np.linspace(np.min(data[0]), np.max(data[0]), 100))
y = linf(x, popt[0], popt[1])
plt.scatter(np.log(data[0]), np.log(data[1]))
plt.plot(x, y)
plt.show()