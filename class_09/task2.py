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
R = 1.4
H = -3
h_rnd = np.random.randn(L, L) * R
h_loc = np.ones((L, L)) * -4 + h_rnd
s = np.ones((L, L), dtype=int) * -1
aval = np.zeros((L, L), dtype=int)
aval_count = 0

hval1 = [H]
mval1 = [np.sum(s)/(L*L)]

while H <= 3:
    aval_count += 1
    do_avalanche(h_loc, s, H, aval, aval_count)
    hval1.append(H)
    mval1.append(np.sum(s)/(L*L))
    H += 0.1

L = 300
R = 0.9
H = -3
h_rnd = np.random.randn(L, L) * R
h_loc = np.ones((L, L)) * -4 + h_rnd
s = np.ones((L, L), dtype=int) * -1
aval = np.zeros((L, L), dtype=int)
aval_count = 0

hval2 = [H]
mval2 = [np.sum(s)/(L*L)]

while H <= 3:
    aval_count += 1
    do_avalanche(h_loc, s, H, aval, aval_count)
    hval2.append(H)
    mval2.append(np.sum(s)/(L*L))
    H += 0.1


L = 300
R = 2.1
H = -3
h_rnd = np.random.randn(L, L) * R
h_loc = np.ones((L, L)) * -4 + h_rnd
s = np.ones((L, L), dtype=int) * -1
aval = np.zeros((L, L), dtype=int)
aval_count = 0

hval3 = [H]
mval3 = [np.sum(s)/(L*L)]

while H <= 3:
    aval_count += 1
    do_avalanche(h_loc, s, H, aval, aval_count)
    hval3.append(H)
    mval3.append(np.sum(s)/(L*L))
    H += 0.1

plt.plot(hval1, mval1)
plt.plot(hval2, mval2)
plt.plot(hval3, mval3)
plt.xlabel("H")
plt.ylabel("M")
plt.savefig("histeresis_all.png")
