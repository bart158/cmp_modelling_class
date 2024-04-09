import numpy as np
import numba
from numba import jit
from PIL import Image, ImageDraw

Nx = 580
Ny = 180

uin = 0.04
Re = 220
vLB = uin*(Ny/2)/Re
tau = 3*vLB + 1/2
eps = 0.0001

e = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
W = [4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36]
reverse = [0, 3, 4, 1, 2, 7, 8, 5, 6]

f = np.zeros((9, Nx, Ny))
feq = np.zeros((9, Nx, Ny))
u = np.zeros((Nx, Ny, 2))
u0 = np.zeros((Ny, 2))
rho = np.zeros((Nx, Ny))

for i in range(0, Ny):
    u[:, i, 1] = uin*(1 + eps*np.sin(2*np.pi*i/Ny - 1))
    u0[i, 1] = uin*(1 + eps*np.sin(2*np.pi*i/Ny - 1))

rho[:, ;] = 1
for i in range(0, 8):
    f[i, :, :] = W[i]*rho[:, :]*((1 + 3 * np.dot(u[:,:], e[i]) + 9/2 * (np.dot(u[:,:], e[i]) )**2 - 3/2 * u[:, :]**2))

for i in range(0, 1000):
    rho[0, :] = 2 * (f[0, :, 3] + f[0, :, 6] + f[0, :, 7]) + (f[0, :, 0] + f[0, :, 2] + f[0, :, 4])/(1 - np.abs(u0[:,1]))
    feq[0, :, :] = W[:]*rho[0, :] * (1 + 3 * e[:] * u0[:,:] + 9/2 * (e[:] * u0[:, :])**2 - 3/2 * u0[:, :]**2)