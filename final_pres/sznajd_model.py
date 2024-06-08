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

N = 100

chain = np.random.randint(0,2,(N))*2 - 1
edges = np.linspace(0, N, N+1, endpoint=True)
for i in range(0, 10000):
    chain = MCstep(chain)
    if i%500==0:
        plt.stairs(chain, edges)
        plt.show()



print(chain)
