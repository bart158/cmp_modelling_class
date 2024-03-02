import numpy as np
import random
import matplotlib.pyplot as plt

board = np.random.randint(0,2,(256,512))

for n in range(0, 1000):
    sum_board = np.zeros((256,512))
    rolled_board = np.roll(board, 1, axis = 0)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, 1, axis = 1)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, -1, axis = 0)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, -1, axis = 0)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, -1, axis = 1)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, -1, axis = 1)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, 1, axis = 0)
    sum_board += rolled_board
    rolled_board = np.roll(rolled_board, 1, axis = 0)
    sum_board += rolled_board
    #still need to change the loops
    life_check = np.empty((256,512), dtype=bool)
    life_check = ((board == 0) & (sum_board == 3)) | ((board == 1) & ((sum_board == 2) | (sum_board == 3)))
    board = life_check.astype(int)
    '''
    if n < 100:
        plt.imshow(board, cmap='gray_r', vmin = 0, vmax = 1)
        plt.savefig("gol_frames/frame{0:05d}.png".format(n))
    '''

plt.imshow(board, cmap='gray_r', vmin = 0, vmax = 1)
plt.show()