import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['text.usetex'] = True

def MCstep(chain):
    for j in range(0, len(chain)):
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

def random_flip(chain, p):
    flip_prob = np.ranom.random(len(chain))
    if_to_flip = np.where(flip_prob <= p, -1, 0)
    chain = chain * if_to_flip

def getMag(chain):
    return np.sum(chain)

def check_if_changed(chain, chain_copy, time_arr, n_of_step):
    isChanged = np.abs((np.abs(chain + chain_copy) - 2)/2)
    for i, isC in enumerate(isChanged):
        if int(isC) == 1:
            time_arr[i].append(n_of_step)
    #print(isChanged)

def plot_state(chain, i):
    plt.clf()
    plt.figure(figsize=(10,5))
    ax = plt.gca()
    ax.set_ylim(0, 1)
    plt.stairs((chain + 1)/2, edges, fill=True, color = 'black', linewidth = 0, antialiased = False)
    file_name = 'for_gif/outcome{0:05d}.png'.format(i)
    plt.savefig(file_name)
    plt.clf()
    plt.close()


N = 1000

chain = np.random.randint(0,2,(N))*2 - 1
edges = np.linspace(0, N, N+1, endpoint=True)
x = []
m = []
time_arr_numpy = np.zeros((N, 1), dtype= int)
time_arr = time_arr_numpy.tolist()

for i in range(0, 100000):
    #plot_state(chain, i)
    x.append(i)
    chain_copy = np.copy(chain)
    chain = MCstep(chain)
    m.append(getMag(chain))
    check_if_changed(chain, chain_copy, time_arr, i)
    
#plot_state(chain, 1000)
plt.plot(x,m)
plt.title('Magnetization')
plt.ylabel('m')
plt.savefig("magnetization.png")
tau = []
for iTime in time_arr:
    for i in range(0, len(iTime) - 1):
        tau.append(iTime[i+1] - iTime[i])

plt.clf()
n, bins, patches = plt.hist(tau, 50)
plt.cla()
taux = bins + (bins[1]-bins[0])/2
taux = taux[0:-1]
np.savetxt('tau_plot.txt', np.array([taux, n]))
plt.scatter(taux, n)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('tau')
plt.ylabel('P(tau)')
plt.title('tau distribution')
plt.savefig('tauhist.png')

