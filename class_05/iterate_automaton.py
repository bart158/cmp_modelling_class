import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

sizeN = 500
stepsN = 100

def get_neighbours(board):
    N = np.roll(board, 1, axis = 0)
    NE = np.roll(N, -1, axis = 1)
    E = np.roll(NE, -1, axis = 0)
    SE = np.roll(E, -1, axis = 0)
    S = np.roll(SE, 1, axis = 1)
    SW = np.roll(S, 1, axis = 1)
    W = np.roll(SW, 1, axis = 0)
    NW = np.roll(W, 1, axis = 0)
    return N, NE, E, SE, S, SW, W, NW

def gen_grid(board, automaton):
    #print(automaton)
    N, NE, E, SE, S, SW, W, NW = get_neighbours(board)

    rule_indx = NW + 2*N + 4*NE + 8*W + 16*board + 32*E + 64*SW + 128*S + 256*SE
    #print(rule_indx)
    board = automaton[rule_indx]
    #print(board)
    return board

def fit_test(board):
    adj_w = 4
    corn_w = 8
    corn_neg = -5
    N, NE, E, SE, S, SW, W, NW = get_neighbours(board)
    fit_score = np.zeros_like(board)
    check_adj = -adj_w * ((N == board) + (W == board))
    check_corner =  corn_w * ((NE == board) + (NW == board) ) + corn_neg * ((NE!=board) + (NW!=board))
    max_fitval = (adj_w*4 + corn_w*4) * len(board) * len(board[0])
    #print(check_adj + check_corner)
    return np.sum(check_adj + check_corner)/max_fitval

def print_frame(sizeN, board, filename = 'lastframe.png'):
    height = sizeN
    width = sizeN
    img = Image.new("RGB",(width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if not board[y, x]:
                draw.point((x,y), (0, 0, 0))
    img.save(filename)

automata = np.loadtxt('automata_working02.txt')
fulminante = np.loadtxt('fulminante.txt')
#np.savetxt('fulminante.txt', fulminante.astype(int), fmt='%s')
'''
for i in range(0, len(automata)):
    automaton = np.array(automata[i], dtype=int)
    board = np.random.randint(0,2,(sizeN, sizeN))
    for j in range(0, stepsN):
        board = gen_grid(board, automaton)
    print(fit_test(board))
    print_frame(sizeN, board, "larger_iter{}.png".format(i))
'''
automaton = np.array(fulminante, dtype=int)
board = np.random.randint(0,2,(sizeN, sizeN))
for j in range(0, stepsN):
    board = gen_grid(board, automaton)
print(fit_test(board))
print_frame(sizeN, board, "larger_iter{}.png".format('_fulminante'))