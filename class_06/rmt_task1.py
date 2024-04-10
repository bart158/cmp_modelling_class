import numpy as np
import matplotlib.pyplot as plt

nSample1 = 20000
dimN1 = 6

nSample2 = 10000
dimN2 = 20

nSample3 = 500
dimN3 = 200


def gen_GOE_ham(dimN):
    h = np.random.randn(dimN, dimN)
    return (h + h.T)/2

def wigner(E, N):
    return 2 * np.sqrt(2*N - E*E)/(np.pi * 2 * N)

def get_eigens(nSamples, dimN):
    eigen = np.array([])
    for i in range(0,nSamples):
        eigenvalues, eigenvectors = np.linalg.eig(gen_GOE_ham(dimN))
        eigen = np.concatenate((eigen, eigenvalues))
    return eigen



fig, axes = plt.subplots(1, 3, figsize=(30, 10))
eigen1 = get_eigens(nSample1, dimN1)
eigen2 = get_eigens(nSample2, dimN2)
eigen3 = get_eigens(nSample3, dimN3)

n1, bins1, patches1 = axes[0].hist(eigen1, 50,  density = True, label = "dim = {}, nSamples = {}".format(dimN1,nSample1))
axes[0].plot(bins1, wigner(bins1, dimN1), 'r-', linewidth = 2)

n2, bins2, patches2 = axes[1].hist(eigen2, 50,  density = True, label = "dim = {}, nSamples = {}".format(dimN2,nSample2))
axes[1].plot(bins2, wigner(bins2, dimN2), 'r-', linewidth = 2)

n3, bins3, patches3 = axes[2].hist(eigen3, 50,  density = True, label = "dim = {}, nSamples = {}".format(dimN3,nSample3))
axes[2].plot(bins3, wigner(bins3, dimN3), 'r-', linewidth = 2)

fig.savefig('task1_fig.png')
fig.show()
