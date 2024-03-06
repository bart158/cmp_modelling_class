import numpy as np
from PIL import Image, ImageDraw
sizeN = 201
board = np.zeros((sizeN,sizeN), dtype=np.int8)
board[int(sizeN/2),int(sizeN/2)] = 1
score = np.zeros((sizeN,sizeN))

b = 1.9
payoffmatrix = np.array((((1,1),(0,b)),
                        ((b,0),(0,0))))

for i in range(0,100):
    N = np.roll(board, 1, axis = 0)
    NE = np.roll(N, -1, axis = 1)
    E = np.roll(NE, -1, axis = 0)
    SE = np.roll(E, -1, axis = 0)
    S = np.roll(SE, 1, axis = 1)
    SW = np.roll(S, 1, axis = 1)
    W = np.roll(SW, 1, axis = 0)
    NW = np.roll(W, 1, axis = 0)
    board_arr = np.array((N, NE, E, SE, S, SW, W, NW))
    score = payoffmatrix[board, board, 0] + payoffmatrix[board, N, 0] + payoffmatrix[board, NE, 0] + payoffmatrix[board, E, 0] + payoffmatrix[board, SE, 0] + payoffmatrix[board, S, 0] + payoffmatrix[board, SW, 0] + payoffmatrix[board, W, 0] + payoffmatrix[board, NW, 0]
    scoreN = np.roll(score, 1, axis = 0)
    scoreNE = np.roll(scoreN, -1, axis = 1)
    scoreE = np.roll(scoreNE, -1, axis = 0)
    scoreSE = np.roll(scoreE, -1, axis = 0)
    scoreS = np.roll(scoreSE, 1, axis = 1)
    scoreSW = np.roll(scoreS, 1, axis = 1)
    scoreW = np.roll(scoreSW, 1, axis = 0)
    scoreNW = np.roll(scoreW, 1, axis = 0)
    new_board = board.copy()
    max_score = score.copy()
    score_arr = np.array((scoreN, scoreNE, scoreE, scoreSE, scoreS, scoreSW, scoreW, scoreNW))
    for j in range(0,8):
        new_board = np.where(max_score<score_arr[j], board_arr[j], new_board)
        max_score = np.where(max_score<score_arr[j], score_arr[j], max_score)
    board = new_board
    #print(new_board)
    #print(max_score)
    height = sizeN
    width = sizeN
    img = Image.new("RGB",(width, height),(255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if board[y][x]:
                draw.point((x,y),(0,0,0))
    img.save("spatialPD_frames/frame{0:05d}.PNG".format(i))
