import numpy as np
import matplotlib.pyplot as plt


board = np.ones((100,100))
ant_pos = np.zeros(2, int)
ant_pos[0] = 50
ant_pos[1] = 50
ant_dir = 0

# 0 up, 1 right, 2 down, 3 left

for i in range(0, 10000):
    if board[ant_pos[0], ant_pos[1]] == 0:
        board[ant_pos[0], ant_pos[1]] = 1
        ant_dir += 1
        if ant_dir == 4:
            ant_dir = 0
    else:
        board[ant_pos[0], ant_pos[1]] = 0
        ant_dir -= 1
        if ant_dir == -1:
            ant_dir = 3
    if ant_dir == 0:
        ant_pos[1] -= 1
        if ant_pos[1] == -1:
            ant_pos[1] = 99
    elif ant_dir == 1:
        ant_pos[0] += 1
        if ant_pos[0] == 100:
            ant_pos[0] = 0
    elif ant_dir == 2:
        ant_pos[1] += 1
        if ant_pos[1] == 100:
            ant_pos[1] = 0
    else:
        ant_pos[0] -= 1
        if ant_pos[0] == -1:
            ant_pos[0] = 99

plt.imshow(board*255, cmap='gray', vmin=0, vmax=255)
plt.show()