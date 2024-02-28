# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Folding_Paper.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/28 08:16:28 by pwolff            #+#    #+#              #
#    Updated: 2024/02/28 08:28:01 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

order = input()
side = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("order : ", order, file=sys.stderr, flush=True)
print("side : ", side, file=sys.stderr, flush=True)


face = {'D': 1,
        'L': 1,
        'U': 1,
        'R': 1,
 }

for value in order:
    print(value, file=sys.stderr, flush=True)
    if value == 'D':
        face['U'] += face['D']
        face['D'] = 1
        face['R'] *= 2
        face['L'] *= 2
    elif value == 'U':
        face['D'] += face['U']
        face['U'] = 1
        face['R'] *= 2
        face['L'] *= 2
    elif value == 'L':
        face['R'] += face['L']
        face['L'] = 1
        face['D'] *= 2
        face['U'] *= 2
    elif value == 'R':
        face['L']  += face['R']
        face['R']  = 1
        face['D'] *= 2
        face['U'] *= 2

print(face[side])


# D = 1
# L = 1
# U = 1
# R = 1

# for value in order:
#     print(value, file=sys.stderr, flush=True)
#     if value == 'D':
#         U += D
#         D = 1
#         R *= 2
#         L *= 2
#     elif value == 'U':
#         D += U
#         U = 1
#         R *= 2
#         L *= 2
#     elif value == 'L':
#         R += L
#         L = 1
#         D *= 2
#         U *= 2
#     elif value == 'R':
#         L += R
#         R = 1
#         D *= 2
#         U *= 2
#     print(f"{value} : D = {D} U = {U} R = {R} L = {L}", file=sys.stderr, flush=True)

# if side == 'D':
#     print(D)
# elif side == 'U':
#     print(U)
# elif side == 'R':
#     print(R)
# elif side == 'L':
#     print(L)        
    








# ***********************************************************************

order = input()
look = input()

folds = [1, 1, 1, 1]
names = "DLUR"

for step in order:
    side = names.index(step)
    # use negative offsets for automatic wrap-around
    folds[side - 2] += folds[side]  # opposite side
    folds[side - 1] *= 2 # adjacent side
    folds[side - 3] *= 2 # adjacent side
    folds[side - 0] = 1 # this side

print(folds[names.index(look)])


# ***********************************************************************
opp = {'R': 'L', 'L': 'R', 'D': 'U', 'U': 'D'}
adj = {'R': 'UD', 'L': 'UD', 'D': 'RL', 'U': 'RL'}
layers = {x: 1 for x in 'RLUD'}
for fold in input():
    layers[opp[fold]] += layers[fold]
    layers[fold] = 1
    for a in adj[fold]:
        layers[a] *= 2
print(layers[input()])

# *****************************************************************

order = input()
side = input()

sides_name = 'RULD'
sides = [1, 1, 1, 1]

for f in order:
    i = sides_name.index(f)
            
    sides[i-2] += sides[i]
    sides[i] = 1
    
    sides[i-1] *= 2
    sides[i-3] *= 2
    
    
print(sides[sides_name.index(side)])

# ************************************************************

order, side = input(), input()
s = {'R' : [1, 'LUD'], 'L' : [1, 'RUD'], 'U' : [1, 'DRL'], 'D' : [1, 'URL']}
for o in order:
    si = s[o][1]
    s[si[0]][0] += s[o][0]
    s[o][0] = 1
    s[si[1]][0] *= 2
    s[si[2]][0] *= 2
print(s[side][0])