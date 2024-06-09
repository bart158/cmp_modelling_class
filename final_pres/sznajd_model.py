import numpy as np
import matplotlib.pyplot as plt

def MCstep(chain):
    i = np.random.randint(0, len(chain)-1)
    if chain[i] == chain[i+1]:
        if i-1 >= 0:
            chain[i-1] = chain[i]
        if i+2 < len(chain):
            chain[i+2] = chain[i]
    else:
        if i-1 >= 0:
            chain[i-1] = chain[i+1]
        if i+2 < len(chain):
            chain[i+2] = chain[i]
    return chain

def getMag(chain):
    return np.sum(chain)

def check_if_changed(chain, chain_copy, time_arr, n_of_step):
    isChanged = np.abs((np.abs(chain + chain_copy) - 2)/2)
    for i, isC in enumerate(isChanged):
        if int(isC) == 1:
            time_arr[i].append(n_of_step)
    #print(isChanged)

N = 100

chain = np.random.randint(0,2,(N))*2 - 1
edges = np.linspace(0, N, N+1, endpoint=True)
x = []
m = []
time_arr_numpy = np.zeros((N, 1), dtype= int)
time_arr = time_arr_numpy.tolist()

for i in range(0, 10000):
    x.append(i)
    chain_copy = np.copy(chain)
    chain = MCstep(chain)
    m.append(getMag(chain))
    check_if_changed(chain, chain_copy, time_arr, i)
    #if i%500==0:
        #plt.stairs(chain, edges)
        #plt.show()

plt.plot(x,m)
plt.savefig("magnetization.png")
tau = []
for iTime in time_arr:
    for i in range(0, len(iTime) - 1):
        tau.append(iTime[i+1] - iTime[i])

plt.clf()
plt.hist(tau)
plt.xscale('log')
plt.yscale('log')
plt.savefig('tauhist.png')

