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

opC = opU(0, 0)
opD = opU(np.pi, 0)
opQ = np.array(((1j,0),(0,-1j)))
opM = np.array(((1j,-1),(1,-1j)))/np.sqrt(2)

payoff = np.array((((3,3), (0,5)), ((5,0), (1,1))))
gamma_test = 0

phif = playPD(gamma_test, opC, opC)
outcome = getPayoffs(phif, payoff)

print("Alice payoff: {}\nBob payoff: {}".format(outcome[0], outcome[1]))

gamma = np.linspace(0, np.pi/2, 100, endpoint = True)
ddpayoffs = []
dqpayoffs = []
qdpayoffs = []
qqpayoffs = []

for g in gamma:
    ddpayoffs.append(getPayoffs(playPD(g, opD, opD), payoff)[0])
    dqpayoffs.append(getPayoffs(playPD(g, opD, opQ), payoff)[0])
    qdpayoffs.append(getPayoffs(playPD(g, opQ, opD), payoff)[0])
    qqpayoffs.append(getPayoffs(playPD(g, opQ, opQ), payoff)[0])


plt.plot(gamma, ddpayoffs, label = "DxD")
plt.plot(gamma, dqpayoffs, label = "DxQ")
plt.plot(gamma, qdpayoffs, label = "QxD")
plt.plot(gamma, qqpayoffs, label = "QxQ")

plt.title("Alice payoffs")
plt.xlabel("$\gamma$")
plt.ylabel("payoff")
plt.legend()
plt.savefig("task2a.png")

plt.clf()

theta_bob = np.linspace(0, 2*np.pi, 100)
gamma_bob = np.pi/2
cpayoffs = []
dpayoffs = []
mpayoffs = []

for th in theta_bob:
    cpayoffs.append(getPayoffs(playPD(gamma_bob, opC, opU(th, 0)), payoff)[0])
    dpayoffs.append(getPayoffs(playPD(gamma_bob, opD, opU(th, 0)), payoff)[0])
    mpayoffs.append(getPayoffs(playPD(gamma_bob, opM, opU(th, 0)), payoff)[0])

plt.plot(theta_bob, cpayoffs, label = "C")
plt.plot(theta_bob, dpayoffs, label = "D")
plt.plot(theta_bob, mpayoffs, label = "M")

plt.title("Alice payoffs for $\gamma$ = {}".format(gamma_bob))
plt.xlabel("theta")
plt.ylabel("payoff")
plt.legend()
plt.savefig("task2b.png")
