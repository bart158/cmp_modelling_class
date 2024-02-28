import numpy as np
import random
import matplotlib.pyplot as plt

board = np.random.randint(0,2,(256,512))
new_board = np.zeros((256,512))
for n in range(0, 10):
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
    for i in range(1,255):
        for j in range(1, 511):
                if board[i, j] == 0:
                    if sum_board[i, j] == 3:
                        new_board[i, j] = 1
                else:
                    if not (sum_board[i, j] == 2 or sum_board[i, j] == 3):
                        new_board[i, j] = 0

    board = new_board

plt.imshow(board, cmap='grey', vmin = 0, vmax = 1)
plt.show()