import numpy as np
import random as rnd
from PIL import Image, ImageDraw

class Ant:
    def __init__(this, pos, drc, board, has_food = False, is_lost = 0):
        this.pos = pos
        this.drc = drc
        this.has_food = has_food
        this.is_lost = is_lost
        this.board = board

    #701
    #6x2
    #543
    def get_facing(this):
        size = len(this.board)
        facing_cells_pos = np.zeros((3,2), dtype=int)
        print(this.pos)
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
        facing_cells_pher = np.zeros((3))
        size = len(this.board)
        facing_cells_pos = this.get_facing()
        if this.has_food:
            this.pos = this.pos
        else:
            for i in range(0, 3):
                #print(facing_cells_pos[i, 0])
                facing_cells_pher[i] = this.board[facing_cells_pos[i, 0], facing_cells_pos[i, 1], 1]
            if(np.sum(facing_cells_pher)):
                this.pos = rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = facing_cells_pher.tolist())
                
            else:
                this.pos = rnd.choices(population = (facing_cells_pos[0],facing_cells_pos[1],facing_cells_pos[2]), weights = (1,1,1))
                print(facing_cells_pos[0])



#----------------------
# board initialization
sizeN = 80
board = np.zeros((sizeN,sizeN,3))
# 0 - cell type; 1 - home pheromone level; 2 - foraging pheromone level
# 0 - open field; 1 - nest; 2 - food; 3 - obstacle
for i in range(35,45):
    for j in range(35, 45):
        board[i, j, 0] = 1

for i in range(5,20):
    for j in range(5, 20):
        board[i, j, 0] = 2

#----------------------
# ant initialization
ants = np.empty((50), dtype = Ant)
for i in range(0, 50):
    ants[i] = Ant(np.array((np.random.randint(35,45), np.random.randint(35,45))), np.random.randint(0, 8), board)

for i in range(0, 100):
    for a in ants:
        #print(i)
        a.move()

height = sizeN
width = sizeN
img = Image.new("RGB",(width, height),(255,255,255))
draw = ImageDraw.Draw(img)
for y in range(height):
    for x in range(width):
        if board[y,x,0] == 1:
            draw.point((x,y),(0,0,255))
        if board[y, x, 0] == 2:
            draw.point((x,y),(0,255,0))
        if board[y, x, 0] == 3:
            draw.point((x, y), (255,0,0))
for a in ants:
    draw.point(a.pos, (0,0,0))
img.save("ant_colony.PNG")


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