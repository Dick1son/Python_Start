import os

def CreateArray():
    array = []
    for i in range(3):
        array1 = []
        for j in range(3):
            array1.append('-')
        array.append(array1)
    return array

def PrintArray(array):
    for i in range(3):
        print("  ".join(array[i]))



def Bot(table):
    step = 1
    if step == 1:
        for i in range(0,3,2):
            for j in range(0,3,2):
                if table[i][j] != 'X':
                    table[i][j] = 'O'
    else:
        for i in range(3):
            for j in range(3):
                if table[i][j] == 'O':
                    if table [i - 1][j] == '-':
                        table [i - 1][j] == 'O'
                        break
                    if table [i][j - 1] == '-':
                        table [i][j - 1] == 'O'
                        break
                    if table [i - 1][j - 1] == '-':
                        table [i - 1][j - 1] == 'O'
                        break
                    if table [i + 1][j] == '-':
                        table [i + 1][j] == 'O'
                        break
                    if table [i][j + 1] == '-':
                        table [i][j + 1] == 'O'
                        break
                    if table [i + 1][j + 1] == '-':
                        table [i + 1][j + 1] == 'O'
                        break

def CheckWin(table):
    win_coord_i = ((0,0,0,0,1,2),(1,1,1),(2,2,2),(0,1,2),(0,1,2),(0,1,2),(0,1,2),(0,1,2))
    win_coord_j = ((),(0,1,2),(0,1,2),(0,0,0),(1,1,1),(2,2,2),(0,1,2),(2,1,0))
    for each1 in win_coord_i:
        for each2 in win_coord_j:
            if table[each1[0]][each2[3]] == table[each1[1]][each2[4]] == table[each1[2]][each2[5]]:
                return table[each[0]]
    return False

table = CreateArray()

while True:
    os.system('cls||clear')
    PrintArray(table)
    row = int(input("Введите строку: "))
    column = int(input("Введите столбец: "))
    table[row - 1][column - 1] = 'X'
    CheckWin(table)
    if char == 'X':
        char = 'O'
    else:
        char = 'X'