import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import random

C = np.array((1,0))
D = np.array((0,1))

def opU(theta, phi):
    return np.array(((np.exp(1j*phi)*np.cos(theta/2), np.sin(theta/2)), (-np.sin(theta/2), np.exp(-1j*phi)*np.cos(theta/2))))

def opJ(gamma):
    opD = opU(np.pi, 0)
    return scp.linalg.expm(-1j*gamma*np.kron(opD, opD)/2)

def playPD(gamma, opUA, opUB):
    opJ0 = opJ(gamma)
    opJ0_H = np.array(np.matrix(opJ0).getH())
    initstate = np.kron(C, C)

    phi0 = np.dot(opJ0, initstate)

    phi1 = np.dot(np.kron(opUA, opUB), phi0)
    phif = np.dot(opJ0_H, phi1)

    return phif

def getPayoffs(phif, payoff):
    PCC = np.abs(phif[0])**2
    PCD = np.abs(phif[1])**2
    PDC = np.abs(phif[2])**2
    PDD = np.abs(phif[3])**2
    return (payoff[0, 0, 0] * PCC + payoff[0, 1, 0] * PCD + payoff[1, 0, 0] * PDC + payoff[1, 1, 0] * PDD, payoff[0, 0, 1] * PCC + payoff[0, 1, 1] * PCD + payoff[1, 0, 1] * PDC + payoff[1, 1, 1] * PDD)


def payoff_A(angles, *args):
    gamma, payoff = args
    theta, phi = angles
    phif1 = playPD(gamma, opU(theta, phi), opU(0, 0))
    phif2 = playPD(gamma, opU(theta, phi), opU(np.pi, 0))
    m1 = getPayoffs(phif1, payoff)[0]
    m2 = getPayoffs(phif2, payoff)[0]
    if  m1 < m2:
        return -m1
    else:
        return -m2

def payoff_A_tparam(tA, tB, *args):
    gamma, payoff = args
    
    if tA < 0:
        UA = opU(0, -tA*np.pi/2)
    else:
        UA = opU(tA * np.pi, 0)
    if tB < 0:
        UB = opU(0, -tB*np.pi/2)
    else:
        UB = opU(tB * np.pi, 0)
    
    return getPayoffs(playPD(gamma, UA, UB), payoff)[0]

opC = opU(0, 0)
opD = opU(np.pi, 0)
opQ = np.array(((1j,0),(0,-1j)))
opM = np.array(((1j,-1),(1,-1j)))/np.sqrt(2)

payoff = np.array((((3,3), (0,5)), ((5,0), (1,1))))

x = y = np.arange(-1, 1, 0.1)
X, Y = np.meshgrid(x, y)
xraveled = np.ravel(X)
yraveled = np.ravel(Y)
zlist1 = []
zlist2 = []
for i in range(0, len(xraveled)):
    zlist1.append(payoff_A_tparam(xraveled[i], yraveled[i], 0, payoff))
    zlist2.append(payoff_A_tparam(xraveled[i], yraveled[i], np.pi/2, payoff))
zs1 = np.array(zlist1)
zs2 = np.array(zlist2)
Z1 = zs1.reshape(X.shape)
Z2 = zs2.reshape(X.shape)

fig, axes = plt.subplots(1, 2, subplot_kw = {"projection": '3d'}, figsize=(10, 5))
axes[0].plot_surface(X, Y, Z1)
axes[1].plot_surface(X, Y, Z2)

for ax in axes:
    ax.set_xlabel('$U_A$')
    ax.set_ylabel('$U_B$')
    ax.set_zlabel('$\$_A$')

axes[0].set_title("$\gamma = 0$")
axes[1].set_title("$\gamma = \pi/2$")
plt.show()