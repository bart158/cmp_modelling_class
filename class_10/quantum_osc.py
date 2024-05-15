import numpy as np
import matplotlib.pyplot as plt
from numba import jit



@jit(nopython=True)
def naive_harmonic_path(x, beta, delta):
    def rho_free(x, y, Delta_tau):
        return np.exp(-(x-y)**2/(2*Delta_tau))
    N = len(x)
    Delta_tau = beta/N
    for i in range(0, N):
        k = np.random.randint(1,N)
        kprev = k - 1
        knext = (k + 1)%N

        xprimk = x[k] + np.random.rand(1)[0] * 2 * delta - delta
        pi_a = rho_free(x[kprev], x[k], Delta_tau) * rho_free(x[k], x[knext], Delta_tau) * np.exp(-Delta_tau * x[k]**2 / 2)
        pi_b = rho_free(x[kprev], xprimk, Delta_tau) * rho_free(xprimk, x[knext], Delta_tau) * np.exp(-Delta_tau * xprimk**2 / 2)
        ypsilon = pi_b/pi_a
        if np.random.rand(1)[0] < ypsilon:
            x[k] = xprimk
    return x, ypsilon

def analytical(x, beta):
    sig2 = 1/(2*np.tanh(beta/2))
    return np.exp(-x**2/(2*sig2))/np.sqrt(2*np.pi*sig2)
beta = 10
delta = 2.4
x = np.random.rand(40) * 2 * delta - delta

MCS_max = 100000
xavg = []
xvar = []
xzeros = []
xmid = []
ypsilon_arr = []
steps = []
for i in range(0, MCS_max):
    x, ypsilon = naive_harmonic_path(x, beta, delta)
    avg = np.sum(x)/len(x)
    var = np.sum((x - avg)**2)/len(x)
    xavg.append(avg)
    xvar.append(var)
    steps.append(i)
    ypsilon_arr.append(ypsilon)
    xzeros.append(x[0])
    xmid.append(x[len(x)//2])

print("r_acc = {}".format(np.sum(ypsilon_arr)/len(ypsilon_arr)))
mean_xavg = np.sum(xavg)/len(xavg)
mean_xvar = np.sum(xvar)/len(xvar)
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (15, 8))
ax[0].plot(steps, xavg)
ax[0].axline((0, mean_xavg), (steps[-1], mean_xavg), color = 'r')
ax[0].set_title("Average x")
ax[0].set_xlabel("MC steps")
ax[0].set_ylabel("x")
ax[1].plot(steps, xvar)
ax[1].axline((0, mean_xvar), (steps[-1], mean_xvar), color = 'r')
ax[1].set_title("Variance of x")
ax[1].set_xlabel("MC steps")
ax[1].set_ylabel("variance")

fig.savefig("task1.png")

fig2, ax2 = plt.subplots(nrows = 1, ncols = 1, figsize = (15, 8))

#ax2[0].hist(xzeros, bins = 20, density=True)
n, bins, patches = ax2.hist(xmid, bins = 20, density=True)
bincenters = bins + (bins[1]-bins[0])/2
bincenters = bincenters[:-1]
ax2.plot(bincenters, analytical(bincenters, beta))
fig2.savefig("task2.png")


