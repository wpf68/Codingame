# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ShootEnemyAircraft.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/04 08:27:18 by pwolff            #+#    #+#              #
#    Updated: 2024/03/04 08:42:36 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



def moveAvions(dictionnaire, posMissile):
    # Part Left
    y = 0
    awake = 0
    while y < n-1:
        x = posMissile - 1
        while x >= 0:
            if dictionnaire[y][x] == '>':
                dictionnaire[y][x] = '.'
                dictionnaire[y][x + 1] = '>'
                awake = 1
            x -= 1
        y += 1
    # Part Right
    y = 0
    while y < n-1:
        x = posMissile + 1
        while x < len(dictionnaire[y]):
            if dictionnaire[y][x] == '<':
                dictionnaire[y][x] = '.'
                dictionnaire[y][x - 1] = '<'
                awake = 1
            x += 1
        y += 1         

    return awake

dictionnaire = {}
n = int(input())
print(n, file=sys.stderr, flush=True)

for i in range(n):
    line = input()
    temp = list(line)
    dictionnaire[i] = temp

    print(line, file=sys.stderr, flush=True)

for temp in dictionnaire:
    print(temp, " - ", dictionnaire[temp], file=sys.stderr, flush=True)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

missile = dictionnaire[n-1].index('^')
print("\n",missile, file=sys.stderr, flush=True)

awake = 1
# test = 4

while awake:
    fire = 0
    y = 0
    while y < n-1:
        x = 0
        for pos in dictionnaire[y]:
            if pos == '>':
                avionX = missile - x - 1
                avionY = n-2 - y
                print(f"{pos} : X = {avionX}  Y = {avionY}", file=sys.stderr, flush=True)
                if avionX == avionY + 1:
                    fire = 1
                    dictionnaire[y][x] = '.'
            elif pos == '<':
                avionX = x - missile - 1
                avionY = n-2 - y
                print(f"{pos} : X = {avionX}  Y = {avionY}", file=sys.stderr, flush=True)
                if avionX == avionY + 1:
                    fire = 1
                    dictionnaire[y][x] = '.'
            x += 1
        y += 1
    if fire:
        print("SHOOT")
    else:
        print("WAIT")
    awake = moveAvions(dictionnaire, missile)
    for temp in dictionnaire:
        print(temp, " - ", dictionnaire[temp], file=sys.stderr, flush=True)
    


#**********************************************************************************
      

moving = set()

n = int(input())
for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] in "<>":
            moving.add((i,j))
        if line[j] == "^":
            base = (i,j)

turnsToShoot = set()
(a,b) = base
for (i,j) in moving:
    turnsToShoot.add(abs(j-b)-abs(i-a))

for i in range(1,max(turnsToShoot)+1):
    print("SHOOT" if i in turnsToShoot else "WAIT")
  