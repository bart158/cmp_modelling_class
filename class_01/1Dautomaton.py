import numpy as np
from PIL import Image, ImageDraw


rule = input("Give rule number:")
rule_bin_str = np.binary_repr(int(rule), width=8)
rule_bin = np.array([int(ch) for ch in rule_bin_str], dtype=np.int8)

board = np.zeros((1000,101))

board[0, 50] = 1

for i in range(1, len(board)):
    leftcell = np.roll(board[i-1], 1)
    rightcell = np.roll(board[i-1], -1)
    sumboard = leftcell*4 + board[i-1]*2 + rightcell
    board[i] = rule_bin[7-sumboard.astype(np.int8)]


img = Image.new("RGB",(101, 1000),(255,255,255))
draw = ImageDraw.Draw(img)
for y in range(1000):
    for x in range(101):
        if board[y][x]:
            draw.point((x,y),(0,0,0))
img.save(f"ca{rule}.PNG")