# Implementa tu función sudoku_solver a continuación:

def sudoku_solver(grid):
    for i in range(0, 9, 3):  # Para cada bloque de 3x3 0, 3, 6
        for j in range(0, 9, 3): # 0, 3, 6
            for x in range(3): # 0, 1, 2
                for y in range(3): # 0, 1, 2
                    if grid[i + x][j + y] == 0: # grid[0+0][0+0], grid[0+0][0+1], grid[0+0][0+2]
                        grid[i + x][j + y] = 1
                    return grid[i + x][j + y]
# No modifiques el código a continuación:

print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testeando sudoku con estructura correcta:")

correct_input_grid = [
    [7,0,0,  0,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,8,  0,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,0],
    [0,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,0,5,  0,0,7,  0,0,4]
]


import copy
input_grid = copy.deepcopy(correct_input_grid)
output_grid = [
    [7, 1, 3, 2, 4, 5, 8, 9, 6],
    [5, 8, 9, 6, 1, 3, 2, 4, 7],
    [4, 6, 2, 7, 9, 8, 1, 3, 5],
    [1, 2, 8, 3, 5, 4, 6, 7, 9],
    [9, 5, 4, 8, 7, 6, 3, 2, 1],
    [3, 7, 6, 9, 2, 1, 4, 5, 8],
    [6, 9, 7, 4, 8, 2, 5, 1, 3],
    [8, 4, 1, 5, 3, 9, 7, 6, 2],
    [2, 3, 5, 1, 6, 7, 9, 8, 4]
]
if output_grid == sudoku_solver(input_grid):
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
    os.system("echo '\e[31mIncorrecto\e[0m'")
