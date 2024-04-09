import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


sizeN = 20
atmtN = 20
stepsN = 100
genN = 20

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
    #print(board)
    N, NE, E, SE, S, SW, W, NW = get_neighbours(board)

    rule_indx = NW + 2*N + 4*NE + 8*W + 16*board + 32*E + 64*SW + 128*S + 256*SE
    #print(rule_indx)
    board = automaton[rule_indx]

def fit_test(board):
    adj_w = 5
    corn_w = 5
    N, NE, E, SE, S, SW, W, NW = get_neighbours(board)
    fit_score = np.zeros_like(board)
    check_adj = adj_w * ((N != board) + (W != board) + (E != board) + (S != board))
    check_corner =  corn_w * ((NE == board) + (NW == board) + (SE == board) + (SW == board))
    max_fitval = (adj_w*4 + corn_w*4) * len(board) * len(board[0])
    #print(check_adj + check_corner)
    return np.sum(check_adj + check_corner)/max_fitval

def clone(automata, fitness):
    weights = (fitness - 0.95 * fitness.min())
    #print(fitness)
    print(weights)
    return random.choices(automata, weights = weights, k = 100)

def reproduce(automaton1, automaton2):
    rand_cross = np.random.randint(0, 2, (512)).astype(bool)
    return np.where(rand_cross, automaton1, automaton2)

def mutate(automaton):
    for i in range(0, 2):
        randindx = np.random.randint(0, len(automaton))
        automaton[randindx] = (not automaton[randindx] ) and 1

def new_gen(automata, fitness):
    clones = clone(automata, fitness)
    for i in range(0, len(automata)):
        parents = random.choices(clones, k = 2)
        automata[i] = reproduce(parents[0], parents[1])
        mutate(automata[i])
    
def print_frame(sizeN, board):
    height = sizeN
    width = sizeN
    img = Image.new("RGB",(width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if not board[y, x]:
                draw.point((x,y), (0, 0, 0))
    img.save("lastframe.png")

automata = np.random.randint(0, 2, (atmtN, 512))
fitness = np.zeros((atmtN))
fitness_plot = []
#test_arr = np.array([[1,0,0], [0,1,0], [0,0,0]])
#gen_grid(test_arr, automata[0])
#print(fit_test(test_arr))
print(automata)
for n in range(0, genN):
    if not n%10:
        print("Gen #{}".format(n))
    initboard = np.random.randint(0, 2, (sizeN, sizeN))
    boards = np.array([initboard] * atmtN)

    for i in range(0, stepsN):
        for j in range(0, atmtN):
            gen_grid(boards[j], automata[j])
    
    for j in range(0, atmtN):
        fitness[j] = fit_test(boards[j])
    fitness_plot.append(fitness.max())
    new_gen(automata, fitness)

print_frame(len(boards[0]), boards[0])
plt.plot(np.arange(0, len(fitness_plot), 1), fitness_plot)
plt.savefig('fitnessplot.png')
plt.show()
