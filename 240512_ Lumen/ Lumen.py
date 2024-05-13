# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     Lumen.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/13 07:01:20 by pwolff            #+#    #+#              #
#    Updated: 2024/05/13 07:16:11 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def display(data):
    for ligne in data:
        print(ligne, file=sys.stderr, flush=True)
    print("\n", file=sys.stderr, flush=True)


# def testAutour(data, x, y):
#     resultLumiere = 0
#     lumiere = 0
#     test = 0

#     # Ligne du haut
#     xTest = x - 1
#     xFin = x + 2
#     yTest = y + 1
#     while xTest < xFin and not test: 
#         if xTest > 0 and xTest < len(data[0]) and yTest > 0 and yTest < len(data):
#             if data[yTest][xTest] != "X":
#                 # print(data[yTest][xTest])
#                 lumiere += int(data[yTest][xTest]) - 1
#                 if resultLumiere < lumiere:
#                     resultLumiere = lumiere
#                 test = 1
#         xTest += 1
    
#     # Ligne du bas
#     xTest = x - 1
#     xFin = x + 2
#     yTest = y - 1
#     while xTest < xFin and not test: 
#         if xTest > 0 and xTest < len(data[0]) and yTest > 0 and yTest < len(data):
#             if data[yTest][xTest] != "X":
#                 # print(data[yTest][xTest])
#                 lumiere += int(data[yTest][xTest]) - 1
#                 if resultLumiere < lumiere:
#                     resultLumiere = lumiere
#                 test = 1
#         xTest += 1

#     # Cote droit
#     xTest = x - 1
#     yTest = y
#     if xTest > 0 and not test:
#         if data[yTest][xTest] != "X":
#             # print("x - y =", x, y, data[yTest][xTest])
#             lumiere += int(data[yTest][xTest]) - 1
#             if resultLumiere < lumiere:
#                 resultLumiere = lumiere
#             test = 1

#     # Cote gauche
#     xTest = x + 1
#     yTest = y
#     if xTest < len(data[0]) and not test:
#         if data[yTest][xTest] != "X":
#             # print("x - y =", x, y, data[yTest][xTest])
#             lumiere += int(data[yTest][xTest]) - 1
#             if resultLumiere < lumiere:
#                 resultLumiere = lumiere
#             test = 1

#     if resultLumiere < 0:
#         resultLumiere = 0

#     if test:
#         return resultLumiere
#     return -1



def remplace(data, x, str):
    i = 0
    string = ""
    while i < len(data):
        if i == x:
            string += str
        else:
            string += data[i]
        i += 1
    return string


# def chercheLumiere(data):
#     X = len(data[0])
#     Y = len(data)
#     print(X, Y, file=sys.stderr, flush=True)
#     dataTemp = data
#     y = 0
#     while (y < Y):
#         x = 0
#         while (x < X):
#             if data[y][x] == 'X':
#                 # print("test pos X*Y :", x, y)
#                 lumiere = testAutour(data, x, y)
#                 if lumiere != -1:
#                     if dataTemp[y][x] == 'X' or int(dataTemp[y][x]) < lumiere:
#                         dataTemp[y] = remplace(dataTemp[y], x, str(lumiere))                    
#             x += 1
#         y += 1
#     return dataTemp


def countZero(data):
    X = len(data[0])
    Y = len(data)
    nbZero = 0
    y = 0
    while (y < Y):
        x = 0
        while (x < X):
            if data[y][x] == '0' or data[y][x] == 'X':
                nbZero += 1                   
            x += 1
        y += 1
    return nbZero

def searchX(data):
    X = len(data[0])
    Y = len(data)
    nbX = 0
    y = 0
    while (y < Y):
        x = 0
        while (x < X):
            if data[y][x] == 'X':
                nbX += 1                   
            x += 1
        y += 1
    return nbX


def valueTest(data, x, y):
    if data[y][x] == 'X':
        return 0
    return 1

def changeValue(data, x, y):
    value = int(data[y][x]) - 1
    
    if value < 0:
        value = 0

    posY = y - 1
    if posY >= 0:
        posX = x - 1 
        if posX >= 0:         
            if valueTest(data, posX, posY) and value > int(data[posY][posX]):
                data[posY] = remplace(data[posY], posX, str(value))
            elif valueTest(data, posX, posY) == 0:
                data[posY] = remplace(data[posY], posX, str(value))

        posX = x
        if valueTest(data, posX, posY) and value > int(data[posY][posX]):
            data[posY] = remplace(data[posY], posX, str(value))
        elif valueTest(data, posX, posY) == 0:
            data[posY] = remplace(data[posY], posX, str(value))

        posX = x + 1 
        if posX < len(data[0]):         
            if valueTest(data, posX, posY) and value > int(data[posY][posX]):
                data[posY] = remplace(data[posY], posX, str(value))
            elif valueTest(data, posX, posY) == 0:
                data[posY] = remplace(data[posY], posX, str(value))
                
    posY = y + 1
    if posY < len(data):
        posX = x - 1 
        if posX >= 0:         
            if valueTest(data, posX, posY) and value > int(data[posY][posX]):
                data[posY] = remplace(data[posY], posX, str(value))
            elif valueTest(data, posX, posY) == 0:
                data[posY] = remplace(data[posY], posX, str(value))

        posX = x
        if valueTest(data, posX, posY) and value > int(data[posY][posX]):
            data[posY] = remplace(data[posY], posX, str(value))
        elif valueTest(data, posX, posY) == 0:
            data[posY] = remplace(data[posY], posX, str(value))

        posX = x + 1 
        if posX < len(data[0]):         
            if valueTest(data, posX, posY) and value > int(data[posY][posX]):
                data[posY] = remplace(data[posY], posX, str(value))
            elif valueTest(data, posX, posY) == 0:
                data[posY] = remplace(data[posY], posX, str(value))

    posY = y
    posX = x - 1 
    if posX >= 0:         
        if valueTest(data, posX, posY) and value > int(data[posY][posX]):
            data[posY] = remplace(data[posY], posX, str(value))
        elif valueTest(data, posX, posY) == 0:
            data[posY] = remplace(data[posY], posX, str(value))

    posX = x + 1 
    if posX < len(data[0]):         
        if valueTest(data, posX, posY) and value > int(data[posY][posX]):
            data[posY] = remplace(data[posY], posX, str(value))
        elif valueTest(data, posX, posY) == 0:
            data[posY] = remplace(data[posY], posX, str(value))


    return data





n = int(input())
l = int(input())
data = []
print(f"n = {n} - l = {l}", file=sys.stderr, flush=True)
for i in range(n):
    temp = ""
    for cell in input().split():
        # print(cell)
        temp += cell
    data.append(temp)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(data, "\n", file=sys.stderr, flush=True)
display(data)

# Allumer les bougies
dataTemp = []
for ligne in data:
    ligne = ligne.replace("C", str(l))
    dataTemp.append(ligne)

data = dataTemp
display(data)

# test chaque chiffre dans la Data

while l > 0:
    X = len(data[0])
    Y = len(data)
    y = 0
    while (y < Y):
        x = 0
        while (x < X):
            # print("x - y ", x, y, (data[y][x]))
            if data[y][x] != 'X' and int(data[y][x]) == l:
                
                data = changeValue(data, x, y)               
            x += 1
        y += 1   
    l -= 1


display(data)




# testX = 1
# while testX:
#     data = chercheLumiere(data)
#     display(data)
#     testX = searchX(data)
#     # print("nbX = ",testX)

nbZero = countZero(data)

print(nbZero)




# ****************************************************************
# ****************************************************************
# ****************************************************************




#Read inputs.
N = int(input())
L = int(input())

grid = []

#Read and create initial grid.
for x in range(N):
    grid += [[L if c == 'C' else 0 for c in input().split()]]

#Add dimmed spots, so everything 0<x<L.
for i in range(L - 1, 0, -1):
    for x in range(N):
        for y in range(N):
            
            #Find biggest surrounding cell.
            max_surrounding_cell = 0
            
            for x_step in range(-1, 2):
                for y_step in range(-1, 2):
                    if 0 <= x + x_step < N and 0 <= y + y_step < N:
                        max_surrounding_cell = max(max_surrounding_cell, grid[x + x_step][y + y_step])

            #Dimmed spot on (x, y) is the maximum in the surrounding cells minus one.
            grid[x][y] = max(grid[x][y], max_surrounding_cell - 1)

#Count dark spots and print the result.
print(sum(x.count(0) for x in grid))



# ****************************************************************
# ****************************************************************
# ****************************************************************


n = int(input())
l = int(input())
grid = []
for x in range(n):
    grid += [[l if c == 'C' else 0 for c in input().split()]]
for i in range(l - 1, 0, -1):
    for x in range(n):
        for y in range(n):
            max_surrounding_cell = 0
            for x_step in range(-1, 2):
                for y_step in range(-1, 2):
                    if 0 <= x + x_step < n and 0 <= y + y_step < n:
                        max_surrounding_cell = max(max_surrounding_cell, grid[x + x_step][y + y_step])
            grid[x][y] = max(grid[x][y], max_surrounding_cell - 1)
print(sum(x.count(0) for x in grid)) 



# ****************************************************************
# ****************************************************************
# ****************************************************************



n = int(input())
l = int(input())

candles = []
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == "C":
            candles += [[i, j]]
    
zeros = 0
for i in range(n):
    for j in range(n): zeros += int(not sum(max(0, l-max(abs(c[0]-i), abs(c[1]-j))) for c in candles))
print(zeros)



# ****************************************************************
# ****************************************************************
# ****************************************************************



def main():
    n,bright = int(input()), int(input())
    candles = tuple( (x, y) for y in range(n) for x,c in enumerate(input().split()) if c == 'C' )

    print(sum(
        hidden(bright, candles, (xc, yc))
        for yc in range(n) for xc in range(n)
    ))


def hidden(bright, candles, cell):
    return all(bright<=dist(cn, cell) for cn in candles)


def dist(candle, cell):
    return max(abs(a-b) for a,b in zip(candle, cell))


if __name__ == '__main__':
    main()
