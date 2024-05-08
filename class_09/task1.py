import numpy as np
import matplotlib.pyplot as plt



def neighbours(i, L):
    ix, iy = i
    return [(ix, (iy+1)%L), (ix, (iy-1)%L), ((ix + 1)%L, iy), ((ix - 1)%L, iy)]

def update(i, s, L):
    s[i] = 1
    for j in neighbours(i, L):
        h_loc[j] += 2
    return

def do_avalanche(h_loc, s, H):
    d = []
    inqueue = np.zeros((L, L), dtype = int)
    i_trig = np.unravel_index(np.argmax(h_loc + (s+1)*(-100)), h_loc.shape)
    #print("i_trig ", (i_trig))
    H -= h_loc[i_trig]
    d.append(i_trig)

    while len(d) > 0:
        #print("d", d)
        itemp = d.pop(0)
        #print("s[itemp] ", (s[itemp]))
        if s[itemp] == -1:
            update(itemp, s, L)
            itoflip = np.transpose((np.logical_and(np.logical_and((h_loc + H) >= 0, s < 0), inqueue == 0)).nonzero())
            for i in itoflip:
                d.append((i[0], i[1]))
                inqueue[i[0], i[1]] = 1
            
            #print("len(d)", (len(d)))
    
    return np.sum(s)

L = 100
R = 0.7
H = 0
h_rnd = np.random.randn(L, L) * R
h_loc = np.ones((L, L)) * -4 + h_rnd
s = np.ones((L, L), dtype=int) * -1

avg1 = 0
for i in range(0, 1000):
    R = 0.7
    H = 0
    h_rnd = np.random.randn(L, L) * R
    h_loc = np.ones((L, L)) * -4 + h_rnd
    s = np.ones((L, L), dtype=int) * -1
    avg1 += do_avalanche(h_loc, s, H)/1000
    #print("s {}", (s))
    if i%10 == 0:
        print(i)

avg2 = 0
for i in range(0, 1000):
    R = 0.9
    H = 0
    h_rnd = np.random.randn(L, L) * R
    h_loc = np.ones((L, L)) * -4 + h_rnd
    s = np.ones((L, L), dtype=int) * -1
    avg2 += do_avalanche(h_loc, s, H)/1000
    if i%100 == 0:
        print(i)

avg3 = 0
for i in range(0, 1000):
    R = 1.4
    H = 0
    h_rnd = np.random.randn(L, L) * R
    h_loc = np.ones((L, L)) * -4 + h_rnd
    s = np.ones((L, L), dtype=int) * -1
    avg3 += do_avalanche(h_loc, s, H)/1000
    if i%100 == 0:
        print(i)

print( "R = {} \t mean_size = {}".format(0.7, (avg1 + L*L)/2))
print( "R = {} \t mean_size = {}".format(0.9, (avg2 + L*L)/2))
print( "R = {} \t mean_size = {}".format(1.4, (avg3 + L*L)/2))