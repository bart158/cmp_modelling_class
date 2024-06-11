import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def linf(x, a, b):
    return a*x + b

data1_raw = np.loadtxt('with_noise/p510-1/tau_plot.txt')
data2_raw = np.loadtxt('with_noise/p510-2/tau_plot.txt')
data3_raw = np.loadtxt('with_noise/p10-3/tau_plot.txt')

mask1 = np.where(data1_raw[1], True, False)
data1x = data1_raw[0, mask1]
data1y = data1_raw[1, mask1]
data1 = np.array([data1x, data1y])

mask2 = np.where(data2_raw[1], True, False)
data2x = data2_raw[0, mask2]
data2y = data2_raw[1, mask2]
data2 = np.array([data2x, data2y])

mask3 = np.where(data3_raw[1], True, False)
data3x = data3_raw[0, mask3]
data3y = data3_raw[1, mask3]
data3 = np.array([data3x, data3y])

popt1, pcov1 = curve_fit(linf, np.log(data1[0]), np.log(data1[1]))
popt2, pcov2 = curve_fit(linf, np.log(data2[0]), np.log(data2[1]))
popt3, pcov3 = curve_fit(linf, np.log(data3[0]), np.log(data3[1]))

#print(popt)
#print(np.sqrt(np.diag(pcov)))
x1 = np.log(np.linspace(np.min(data1[0]), np.max(data1[0]), 100))
y1 = linf(x1, popt1[0], popt1[1])
plt.scatter(np.log(data1[0]), np.log(data1[1]), label = 'p = 0.5', color = 'blue')
plt.plot(x1, y1, color = 'blue')

x2 = np.log(np.linspace(np.min(data2[0]), np.max(data2[0]), 100))
y2 = linf(x2, popt2[0], popt2[1])
plt.scatter(np.log(data2[0]), np.log(data2[1]), label = 'p = 0.05',color = 'orange')
plt.plot(x2, y2, color = 'orange')

x3 = np.log(np.linspace(np.min(data3[0]), np.max(data3[0]), 100))
y3 = linf(x3, popt3[0], popt3[1])
plt.scatter(np.log(data3[0]), np.log(data3[1]), label = 'p = 0.001',color = 'green')
plt.plot(x3, y3, color = 'green')

plt.ylabel('ln(P(tau))')
plt.xlabel('ln(tau)')
plt.legend()
plt.savefig('with_noise/tau_fit_wn.png')