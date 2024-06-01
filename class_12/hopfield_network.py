import numpy as np
import matplotlib.pyplot as plt

def update(x, W):
    #print(np.dot(W, x))
    #print(np.sign(np.dot(W, x)))
    return np.sign(np.dot(W, x))

# Define the patterns for letters D, J, C, and M
D = np.array([
    [1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
])

J = np.array([
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 0]
])

C = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1]
])

M = np.array([
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])

patterns = [D, J, C, M]
flattened = []
for patt in patterns:
    flattened.append(patt.flatten() * 2 - 1)

dimW = len(flattened[0])
W = np.zeros((dimW, dimW))

nofPatt = len(flattened)
for f in flattened:
    W += np.outer(f, f)/nofPatt

np.fill_diagonal(W, 0)

fields = np.copy(flattened)
fields_noise=np.copy(fields)

for f in fields_noise:
    for i in range(0, 5):
        indx = np.random.randint(0, len(f))
        f[indx] *= -1
noise_org = np.copy(fields_noise)

for i in range(0, 5):
    for j in range(0, len(patterns)):
        fields[j] = update(fields[j], W)
        fields_noise[j] = update(fields_noise[j], W)

fields_resh = np.empty((4, 7, 5))
fld_noise_resh = np.empty((4, 7, 5))
noise_org_resh = np.empty((4, 7, 5))
for i in range(0, len(fields)):
    fields_resh[i] = np.reshape(fields[i], (7, 5))
    fld_noise_resh[i] = np.reshape(fields_noise[i], (7, 5))
    noise_org_resh[i] = np.reshape(noise_org[i], (7, 5))
    #print(fields[i])

print(np.shape(fields))
fig, axes = plt.subplots(4, 4, figsize = (15, 15))

for i in range(0,len(patterns)):
    axes[0, i].imshow(patterns[i])
    axes[1, i].imshow(fields_resh[i])
    axes[2, i].imshow(noise_org_resh[i])
    axes[3, i].imshow(fld_noise_resh[i])

fig.savefig('hopfield.png')