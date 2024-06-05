import numpy as np
from matplotlib.pyplot import colormaps as cm
import matplotlib.pyplot as plt
import networkx as nx

def diffusion(g, D, dt, beta):
    temp = np.zeros(34)
    temp[0] = 1
    temp[33] = 0
    for i in range(1, 33):
        for ed in g.edges(str(i)):
            #print(ed)
            temp[i] +=  D * (g.nodes[ed[1]]['state'] - g.nodes[ed[0]]['state']) * g.edges[ed]['weight'] * dt
    
    g = weight_change(g, beta, dt)
    for  i in range(1, 33):
        g.nodes[str(i)]['state'] += temp[i]
    return g

def weight_change(g, beta, dt):
    for ed in g.edges:
        #print(np.abs(g.nodes[ed[0]]['state'] - g.nodes[ed[1]]['state']))
        g.edges[ed]['weight'] += -beta * g.edges[ed]['weight'] * (1- g.edges[ed]['weight']) * (np.abs(g.nodes[ed[0]]['state'] - g.nodes[ed[1]]['state']) - 0.25)**3 * dt
    return g

def get_conn_str(g):
    conn_strength = 0
    for ed in g.edges:
        if (g.nodes[ed[0]]['state'] > 0.5 and g.nodes[ed[1]]['state'] <= 0.5) or (g.nodes[ed[1]]['state'] > 0.5 and g.nodes[ed[0]]['state'] <= 0.5):
            conn_strength += g.edges[ed]['weight']
    return conn_strength

D = 5
beta = 10
dt=0.01
g = nx.Graph()

for i in range(0, 34):
    g.add_node(str(i))
    g.nodes[str(i)]['state'] = 0.5
    if i == 0:
        g.nodes[str(i)]['state'] = 1
    elif i == 33:
        g.nodes[str(i)]['state'] = 0

connections = np.loadtxt('zachary1.txt', dtype=int, converters=float)

for i in range(0, len(connections)):
    g.add_edge(str(connections[i, 0]), str(connections[i, 1]))
    g.edges[str(connections[i, 0]), str(connections[i, 1])]['weight'] = 0.5

nx.draw_spring(g, cmap = cm['Blues'], vmin = 0, vmax = 1, with_labels = True, node_color =
list(nx.get_node_attributes(g, "state").values()), edge_cmap = cm['Oranges'], edge_vmin = 0,
edge_vmax = 1, edge_color = list(nx.get_edge_attributes(g, "weight").values()))
plt.show()
cstren = []
for i in range(0, 6000):
    cstren.append(get_conn_str(g))
    g = diffusion(g, D, dt, beta)
    if i % 1000 == 0:
        for node in g.nodes:
            print(g.nodes[node]['state'])
        nx.draw_spring(g, cmap = cm['Blues'], vmin = 0, vmax = 1, with_labels = True, node_color =
        list(nx.get_node_attributes(g, "state").values()), edge_cmap = cm['Oranges'], edge_vmin = 0,
        edge_vmax = 1, edge_color = list(nx.get_edge_attributes(g, "weight").values()))
        plt.show()
    
cstren.append(get_conn_str(g))
x = np.linspace(0, 6000, 6001)
plt.plot(x, cstren)
plt.show()


