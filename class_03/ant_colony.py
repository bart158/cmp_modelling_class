import numpy as np
import random as rnd
import numba
from numba import jit
from PIL import Image, ImageDraw

class Ant:
    def __init__(this, pos, drc, board, has_food = False, turns_lost = 0):
        this.pos = pos
        this.drc = drc
        this.has_food = has_food
        this.turns_lost = turns_lost
        this.board = board
        this.lost_lim = 30
    
    #701
    #6x2
    #543
    def get_facing(this):
        size = len(this.board)
        facing_cells_pos = np.zeros((3,2), dtype=int)
        #print(this.pos)
        if this.drc == 0:
            facing_cells_pos[0] = ((this.pos[0]-1)%size, (this.pos[1]+1)%size)
            facing_cells_pos[1] = ((this.pos[0])%size, (this.pos[1]+1)%size)
            facing_cells_pos[2] = ((this.pos[0]+1)%size, (this.pos[1]+1)%size)
        elif this.drc == 1:
            facing_cells_pos[0] = ((this.pos[0])%size, (this.pos[1]+1)%size)
            facing_cells_pos[1] = ((this.pos[0]+1)%size, (this.pos[1]+1)%size)
            facing_cells_pos[2] = ((this.pos[0]+1)%size, (this.pos[1])%size)
        elif this.drc == 2:
            facing_cells_pos[0] = ((this.pos[0]+1)%size, (this.pos[1]+1)%size)
            facing_cells_pos[1] = ((this.pos[0]+1)%size, (this.pos[1])%size)
            facing_cells_pos[2] = ((this.pos[0]+1)%size, (this.pos[1]-1)%size)
        elif this.drc == 3:
            facing_cells_pos[0] = ((this.pos[0]+1)%size, (this.pos[1])%size)
            facing_cells_pos[1] = ((this.pos[0]+1)%size, (this.pos[1]-1)%size)
            facing_cells_pos[2] = ((this.pos[0])%size, (this.pos[1]-1)%size)
        elif this.drc == 4:
            facing_cells_pos[0] = ((this.pos[0]+1)%size, (this.pos[1]-1)%size)
            facing_cells_pos[1] = ((this.pos[0])%size, (this.pos[1]-1)%size)
            facing_cells_pos[2] = ((this.pos[0]-1)%size, (this.pos[1]-1)%size)
        elif this.drc == 5:
            facing_cells_pos[0] = ((this.pos[0])%size, (this.pos[1]-1)%size)
            facing_cells_pos[1] = ((this.pos[0]-1)%size, (this.pos[1]-1)%size)
            facing_cells_pos[2] = ((this.pos[0]-1)%size, (this.pos[1])%size)
        elif this.drc == 6:
            facing_cells_pos[0] = ((this.pos[0]-1)%size, (this.pos[1]-1)%size)
            facing_cells_pos[1] = ((this.pos[0]-1)%size, (this.pos[1])%size)
            facing_cells_pos[2] = ((this.pos[0]-1)%size, (this.pos[1]+1)%size)
        else:
            facing_cells_pos[0] = ((this.pos[0]-1)%size, (this.pos[1])%size)
            facing_cells_pos[1] = ((this.pos[0]-1)%size, (this.pos[1]+1)%size)
            facing_cells_pos[2] = ((this.pos[0])%size, (this.pos[1]+1)%size)
        return facing_cells_pos
    
    def move(this):
        this.turns_lost += 1
        facing_cells_pher = np.zeros((3))
        size = len(this.board)
        facing_cells_pos = this.get_facing()

        if this.has_food:
            if this.turns_lost < this.lost_lim:
                this.board[this.pos[0], this.pos[1], 1] += 1-(this.turns_lost/this.lost_lim)
            for i in range(0, 3):
                if this.board[facing_cells_pos[i, 0], facing_cells_pos[i, 1], 0] == 1:
                    this.pos = facing_cells_pos[i]
                    this.has_food = False
                    this.drc = (this.drc+4)%8
                    this.turns_lost = 0
                    return 1
                facing_cells_pher[i] = this.board[facing_cells_pos[i, 0], facing_cells_pos[i, 1], 2]
            #facing_cells_pher[0] /= 2
            #facing_cells_pher[2] /= 2
            if(np.sum(facing_cells_pher)):
                this.pos = (rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = facing_cells_pher.tolist()))[0]
                if (this.pos[0] == facing_cells_pos[0,0] and this.pos[1] == facing_cells_pos[0,1]):
                    this.drc = (this.drc-1)%8
                elif (this.pos[0] == facing_cells_pos[2,0] and this.pos[1] == facing_cells_pos[2,1]):
                    this.drc = (this.drc+1)%8
            else:
                this.pos = (rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = (1,1,1)))[0]
                if (this.pos[0] == facing_cells_pos[0,0] and this.pos[1] == facing_cells_pos[0,1]):
                    this.drc = (this.drc-1)%8
                elif (this.pos[0] == facing_cells_pos[2,0] and this.pos[1] == facing_cells_pos[2,1]):
                    this.drc = (this.drc+1)%8
        else:
            if this.turns_lost < this.lost_lim:
                this.board[this.pos[0], this.pos[1], 2] += 1-(this.turns_lost/this.lost_lim)
            for i in range(0, 3):
                #print(facing_cells_pos[i, 0])
                if this.board[facing_cells_pos[i, 0], facing_cells_pos[i, 1], 0] == 2:
                    this.pos = facing_cells_pos[i]
                    this.board[this.pos[0], this.pos[1], 0] = 0
                    this.has_food = True
                    this.drc = (this.drc+4)%8
                    turns_lost = 0
                    return 0
                facing_cells_pher[i] = this.board[facing_cells_pos[i, 0], facing_cells_pos[i, 1], 1]
                
            if(np.sum(facing_cells_pher)):
                this.pos = (rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = facing_cells_pher.tolist()))[0]
                if (this.pos[0] == facing_cells_pos[0,0] and this.pos[1] == facing_cells_pos[0,1]):
                    this.drc = (this.drc-1)%8
                elif (this.pos[0] == facing_cells_pos[2,0] and this.pos[1] == facing_cells_pos[2,1]):
                    this.drc = (this.drc+1)%8
            else:
                this.pos = (rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = (1,1,1)))[0]
                if (this.pos[0] == facing_cells_pos[0,0] and this.pos[1] == facing_cells_pos[0,1]):
                    this.drc = (this.drc-1)%8
                elif (this.pos[0] == facing_cells_pos[2,0] and this.pos[1] == facing_cells_pos[2,1]):
                    this.drc = (this.drc+1)%8
                '''print(type(this.pos))
                print(type(this.pos[0]))
                print(facing_cells_pos[0])'''
        #print(this.has_food)
        return 0

def print_frame(i, sizeN, board, ants):
    height = sizeN
    width = sizeN
    img = Image.new("RGB",(width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if board[y, x, 1]:
                if int(40*board[y, x, 1]) < 256:
                    draw.point((x, y), (int(40*board[y, x, 1]), 255-int(40*board[y, x, 1]), 255-int(40*board[y, x, 1])))
                else:
                    draw.point((x, y), (255, 0, 0))
            if board[y,x,0] == 1:
                draw.point((x,y),(0,0,255))
            if board[y, x, 0] == 2:
                draw.point((x,y),(0,255,0))
            if board[y, x, 0] == 3:
                draw.point((x, y), (255,0,0))
    for a in ants:
        draw.point((a.pos[1], a.pos[0]), (0,0,0))
        #print("drawing an ant at pos: ", sep = " ")
        #print(a.pos)
    img.save("ant_colony_frames/frame{0:05d}.png".format(i))

#----------------------
# board initialization
sizeN = 80
board = np.zeros((sizeN,sizeN,3))
# 0 - cell type; 1 - home pheromone level; 2 - foraging pheromone level
# 0 - open field; 1 - nest; 2 - food; 3 - obstacle
nest_lim = (38, 42)
for i in range(nest_lim[0],nest_lim[1]):
    for j in range(nest_lim[0], nest_lim[1]):
        board[i, j, 0] = 1

for i in range(5,75):
    for j in range(5, 30):
        board[i, j, 0] = 2

#----------------------
# ant initialization
nAnts = 80
ants = np.empty((nAnts), dtype = Ant)
for i in range(0, nAnts):
    ants[i] = Ant(np.array((np.random.randint(nest_lim[0],nest_lim[1]), np.random.randint(nest_lim[0],nest_lim[1]))), np.random.randint(0, 8), board)

food_count = 0
print("Simulating the ant colony...")
for i in range(0, 5000):
    for a in ants:
        food_count += a.move()
    board[:, :, 1] *= 0.99
    board[:, :, 2] *= 0.99
    #print(i)
    print_frame(i, sizeN, board, ants)
print("Simulation finished!")
print("Collected food: ")
print(food_count)

'''
class Cell:
    def __init__(this, home_ph, forage_ph, nest):
        this.home_ph = home_ph
        this.forage_ph = forage_ph
        this.nest = bool(nest)

test_cell = Cell(1, 2, True)

print(test_cell.home_ph)

test_cell.home_ph = 3

print(test_cell.home_ph)'''