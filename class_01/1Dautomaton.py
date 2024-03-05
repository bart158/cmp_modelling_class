import numpy as np
from PIL import Image, ImageDraw

rule = 150
rule_bin = np.binary_repr(rule)
ruledict = {
    7: rule_bin[0]
    6: rule_bin[1]
    5: rule_bin[2]
    4: rule_bin[3]
    3: rule_bin[4]
    2: rule_bin[5]
    1: rule_bin[6]
    0: rule_bin[7]
}
board = np.zeros((1000,101))

board[0, 50] = 1
for i in range(1, len(board)):
    

print(board[0])