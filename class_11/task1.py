import numpy as np
import matplotlib.pyplot as plt

def Stensor(S, i):
    if i == 1:
        return np.kron(np.kron(S, np.eye(2)), np.eye(2))
    elif i == 2:
        return np.kron(np.kron(np.eye(2), S), np.eye(2))
    else:
        return np.kron(np.kron(np.eye(2), np.eye(2)), S)

Sx = np.array([[0, 1], [1, 0]])
Sz = np.array([[1, 0], [0, -1]])

J12 = -0.4
J13 = -1.6
J23 = -1.0
h1 = -0.5
h2 = 0.5
h3 = -0.1

H0 = - (Stensor(Sx, 1) + Stensor(Sx, 2) + Stensor(Sx, 3))
H1 = - (J12 * Stensor(Sz, 1) * Stensor(Sz, 2) + J13 * Stensor(Sz, 1) * Stensor(Sz, 3) + J23 * Stensor(Sz, 2) * Stensor(Sz, 3) + h1 * Stensor(Sz, 1) + h2 * Stensor(Sz, 2) + h3 * Stensor(Sz, 3))

lam = np.linspace(0, 1, 100)

H = []
for l in lam:
    H.append( (1 - l) * H0 + l * H1)

gr_eigenval = []
gr_eigenvec = []
for h in H:
    egn = np.linalg.eigh(h)
    gr_eigenval.append(egn[0][0])
    gr_eigenvec.append(egn[1][:,0])
#print(gr_eigenvec[0])
#plt.plot(lam, gr_eigenval)

expS1 = []
expS2 = []
expS3 = []
for vec in gr_eigenvec:
    expS1.append(np.dot(vec, np.dot(Stensor(Sz, 1), vec)))
    expS2.append(np.dot(vec, np.dot(Stensor(Sz, 2), vec)))
    expS3.append(np.dot(vec, np.dot(Stensor(Sz, 3), vec)))

fig, ax = plt.subplots(1, 2, figsize = (10, 5))
ax[0].plot(lam, expS1, label = "Sz1")
ax[0].plot(lam, expS2, label = "Sz2")
ax[0].plot(lam, expS3, label = "Sz3")
ax[0].set_title("Expectation values")
ax[0].legend()

ax[1].plot(lam, gr_eigenval)
ax[1].set_title("Ground energy")
fig.savefig("task1.png")


