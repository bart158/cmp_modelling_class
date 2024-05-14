import numpy as np
import matplotlib.pyplot as plt



def neighbours(i, L):
    ix, iy = i
    return [(ix, (iy+1)%L), (ix, (iy-1)%L), ((ix + 1)%L, iy), ((ix - 1)%L, iy)]

def update(i, s, L, aval, aval_count):
    s[i] = 1
    for j in neighbours(i, L):
        h_loc[j] += 2
        aval[j] = aval_count
    return

def do_avalanche(h_loc, s, H, aval, aval_count):
    d = []
    inqueue = np.zeros((L, L), dtype = int)
    totrig = (h_loc+H) >= 0
    i_trig = totrig.nonzero()
    #print("i_trig ", (i_trig))
    for i in range(0, len(i_trig[0])):
        d.append((i_trig[0][i], i_trig[1][i]))

    while len(d) > 0:
        #print("d", d)
        itemp = d.pop(0)
        #print("s[itemp] ", (s[itemp]))
        if s[itemp] == -1:
            update(itemp, s, L, aval, aval_count)
            itoflip = np.transpose((np.logical_and(np.logical_and((h_loc + H) >= 0, s < 0), inqueue == 0)).nonzero())
            for i in itoflip:
                d.append((i[0], i[1]))
                inqueue[i[0], i[1]] = 1
            
            #print("len(d)", (len(d)))
    
    return np.sum(s)

L = 300
R = 2.1
H = -3
h_rnd = np.random.randn(L, L) * R
h_loc = np.ones((L, L)) * -4 + h_rnd
s = np.ones((L, L), dtype=int) * -1
aval = np.zeros((L, L), dtype=int)
aval_count = 0

hval = [H]
mval = [np.sum(s)/(L*L)]

while H <= 3:
    aval_count += 1
    do_avalanche(h_loc, s, H, aval, aval_count)
    hval.append(H)
    mval.append(np.sum(s)/(L*L))
    H += 0.1


plt.imshow(aval,interpolation='none',cmap="gist_rainbow")
plt.savefig("task2a.png")
plt.clf()
plt.plot(mval, hval)
plt.xlabel("M")
plt.ylabel("H")
plt.savefig("histeresis_r21.png")
