import numpy as np
import matplotlib.pyplot as plt
import random

def ant_step(ant_pos, ant_dir, color, board):
    if board[ant_pos[0], ant_pos[1]] != color:
        board[ant_pos[0], ant_pos[1]] = color
        ant_dir += 1
        if ant_dir == 4:
            ant_dir = 0
    else:
        board[ant_pos[0], ant_pos[1]] = 255
        ant_dir -= 1
        if ant_dir == -1:
            ant_dir = 3
    if ant_dir == 0:
        ant_pos[1] -= 1
        if ant_pos[1] == -1:
            ant_pos[1] = len(board)-1
    elif ant_dir == 1:
        ant_pos[0] += 1
        if ant_pos[0] == len(board):
            ant_pos[0] = 0
    elif ant_dir == 2:
        ant_pos[1] += 1
        if ant_pos[1] == len(board):
            ant_pos[1] = 0
    else:
        ant_pos[0] -= 1
        if ant_pos[0] == -1:
            ant_pos[0] = len(board)-1
    return(ant_dir)

board = np.full((1000,1000), 255)
ant_pos = np.zeros((4,2), int)
ant_color = np.array((50, 100, 150, 200))
ant_dir = np.zeros(4, int)
for i in range(0, len(ant_pos)):
    ant_dir[i] = int(random.random()*4)
    for j in range(0, len(ant_pos[0])):
        ant_pos[i, j] = int(random.random()*99)


# 0 up, 1 right, 2 down, 3 left

for i in range(0, 100000):
    for j in range(0, len(ant_color)):
        ant_dir[j] = ant_step(ant_pos[j], ant_dir[j], ant_color[j], board)

plt.imshow(board, cmap = 'terrain', vmin=0, vmax=255)
plt.show()