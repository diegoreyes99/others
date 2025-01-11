# Implementa tu función sudoku_validator a continuación:
def sudoku_validator(grid):
    # Validar que cada fila contiene todos los números del 1 al 9 sin duplicados
    for row in grid:
        if sorted(row) != list(range(1, 10)):  # Compara la fila con la lista [1, 2, ..., 9]
            return False

    # Validar que cada columna contiene todos los números del 1 al 9 sin duplicados
    for col in range(9):
        column = [grid[row][col] for row in range(9)]  # Construir la lista de la columna
        if sorted(column) != list(range(1, 10)):  # Compara la columna con la lista [1, 2, ..., 9]
            return False

    # Validar que cada subcuadrante 3x3 contiene todos los números del 1 al 9 sin duplicados
    for i in range(0, 9, 3):  # Para cada bloque de 3x3
        for j in range(0, 9, 3):
            block = []
            for x in range(3):
                for y in range(3):
                    block.append(grid[i + x][j + y])
            if sorted(block) != list(range(1, 10)):  # Compara el bloque con la lista [1, 2, ..., 9]
                return False

    return True  # Si todo es válido, retorna True

# No modifiques el código a continuación:

print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testeando sudoku con estructura correcta:")

grid = [
        [7,8,4,  1,5,9,  3,2,6],
        [5,3,9,  6,7,2,  8,4,1],
        [6,1,2,  4,3,8,  7,5,9],

        [9,2,8,  7,1,5,  4,6,3],
        [3,5,7,  8,4,6,  1,9,2],
        [4,6,1,  9,2,3,  5,8,7],

        [8,7,6,  3,9,4,  2,1,5],
        [2,4,3,  5,6,1,  9,7,8],
        [1,9,5,  2,8,7,  6,3,4]
    ]
if sudoku_validator(grid):
    os.system("echo '\e[32mCorrecto\e[0m'")
else:
    os.system("echo '\e[31mIncorrecto\e[0m'")


print("Testeando sudoku con estructura incorrecta")

grid = [
    [8,8,4,  1,5,9,  2,2,6],
    [5,2,9,  6,8,2,  8,4,1],
    [6,1,2,  4,2,8,  8,5,9],

    [9,2,8,  8,1,5,  4,6,2],
    [2,5,8,  8,4,6,  1,9,2],
    [4,6,1,  9,2,2,  5,8,8],

    [8,8,6,  2,9,4,  2,1,5],
    [2,4,2,  5,6,1,  9,8,8],
    [1,9,5,  2,8,8,  6,2,4]
]

if sudoku_validator(grid):
    os.system("echo '\e[31mIncorrecto\e[0m'")
else:
    os.system("echo '\e[32mCorrecto\e[0m'")


print("Testeando sudoku con otra estructura incorrecta")

grid = [
    [1,2,3, 4,5,6, 7,8,9],
    [2,3,1, 5,6,4, 8,9,7],
    [3,1,2, 6,4,5, 9,7,8],

    [4,5,6, 7,8,9, 1,2,3],
    [5,6,4, 8,9,7, 2,3,1],
    [6,4,5, 9,7,8, 3,1,2],

    [7,8,9, 1,2,3, 4,5,6],
    [8,9,7, 2,3,1, 5,6,4],
    [9,7,8, 3,1,2, 6,4,5]
]

if sudoku_validator(grid):
    os.system("echo '\e[31mIncorrecto\e[0m'")
else:
    os.system("echo '\e[32mCorrecto\e[0m'")


print("Testeando sudoku con otra estructura incorrecta")

grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,2,7,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]

if sudoku_validator(grid):
    os.system("echo '\e[31mIncorrecto\e[0m'")
else:
    os.system("echo '\e[32mCorrecto\e[0m'")


def verificar_columnas(grid):
    num_columnas = len(grid[0])  # Número de columnas, asumiendo que todas las filas tienen el mismo tamaño
    for j in range(num_columnas):  #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) Iteramos sobre los índices de las columnas
        columna_sum = 0  # Inicializamos la suma de la columna en 0
        for i in range(len(grid)):  # Iteramos sobre las filas
            columna_sum += grid[i][j]  # Sumamos el valor de cada fila en la columna j
        if columna_sum != 45:  # Si la suma de la columna no es 45
            return False  # Retorna False si alguna columna no cumple la condición
    return True
