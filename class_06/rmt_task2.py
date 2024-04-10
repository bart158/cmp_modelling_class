import numpy as np
import matplotlib.pyplot as plt

dimN = 200
nSample = 100

def wigner_goe(s):
    return (np.pi/2) * s * np.exp(-np.pi/4 * s**2)

def wigner_gue(s):
    return (32 / np.pi**2) * s**2 * np.exp(-4/np.pi * s**2)

def gen_GOE_ham(dimN):
    h = np.random.randn(dimN, dimN)
    return (h + h.T)/2

def gen_GUE_ham(dimN):
    hx = np.random.randn(dimN, dimN)
    hy = np.random.randn(dimN, dimN)
    h = np.empty(hx.shape, dtype = np.complex128)
    h.real = hx/np.sqrt(2)
    h.imag = hy/np.sqrt(2)
    return (h + h.conj().T)/2

def get_eigen_diffs(nSamples, dimN, func):
    eigen_diffs = np.array([])
    for i in range(0,nSamples):
        eigenvalues, eigenvectors = np.linalg.eig(func(dimN))
        sorted_eigen = np.sort(eigenvalues.real)
        diffs = np.diff(sorted_eigen)
        #print(diffs)
        eigen_diffs = np.concatenate((eigen_diffs, diffs[int(dimN/2 - dimN/4):int(dimN/2 + dimN/4) ]))
        #eigen_diffs = np.concatenate((eigen_diffs, [diffs[int(dimN/2)]]))
        print(i)
    return eigen_diffs

goespacings = get_eigen_diffs(nSample, dimN, gen_GOE_ham)
guespacings = get_eigen_diffs(nSample, dimN, gen_GUE_ham)



norm_goespacing = goespacings/np.mean(goespacings)
norm_guespacing = guespacings/np.mean(guespacings)

fig, axes = plt.subplots(1, 2, figsize=(20, 10))

n1, bins1, patches1 = axes[0].hist(norm_goespacing, 50,  density = True)
axes[0].plot(bins1, wigner_goe(bins1), 'r-', linewidth = 2)

n2, bins2, patches2 = axes[1].hist(norm_guespacing, 50,  density = True)
axes[1].plot(bins2, wigner_gue(bins2), 'r-', linewidth = 2)

fig.savefig('task2_fig_n200_samp_100.png')
fig.show()