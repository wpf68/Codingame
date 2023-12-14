# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    python.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/17 10:40:17 by pwolff            #+#    #+#              #
#    Updated: 2023/06/17 10:43:59 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def ft_Display(tab):
    for ligne in range(9):
        for colonne in range(9):
            print(tab[ligne][colonne], end='', file=sys.stderr, flush=True)
            if (colonne - 2) % 3 == 0:
                print(" ", end='', file=sys.stderr, flush=True)

        print("", file=sys.stderr, flush=True)
        if (ligne - 2) % 3 == 0:
            print("", file=sys.stderr, flush=True)

def ft_TestRow(tab, reference):
    controleLigne = [0 * 9]
    for ligne in range(9):
            controleLigne = list(tab[ligne])
            # print("ligne ", ligne, " : ", controleLigne, file=sys.stderr, flush=True)
            controleLigne.sort()
            # print("ligne ", ligne, " : ", controleLigne, file=sys.stderr, flush=True)
            if controleLigne != reference:
                return "false"
    return "true"

def ft_TestColumn(tab, reference):
    controleLigne = [0 for _ in range(9)]
    # print("**** : ", controleLigne, file=sys.stderr, flush=True)
    for colonne in range(9):
        for ligne in range(9):
            controleLigne[ligne] = tab[ligne][colonne]
        # print("Colonne ", colonne, " : ", controleLigne, file=sys.stderr, flush=True)
        controleLigne.sort()
        # print("Colonne ", colonne, " : ", controleLigne, file=sys.stderr, flush=True)
        if controleLigne != reference:
            return "false"
    return "true"

def ft_TestSquare(tab, reference):
    controleSquare = [0 for _ in range(9)]
    for z in range(3):
        for k in range(3):
            x = 0
            for ligne in range(3):
                for colonne in range(3):
                    controleSquare[x] = tab[ligne + z * 3][colonne + k * 3]
                    x += 1
            print("Z ", z, " K ", k, " = ", controleSquare, file=sys.stderr, flush=True)
            controleSquare.sort()
            if controleSquare != reference:
                return "false"


    return "true"



test = ""
reference = [1, 2, 3, 4, 5, 6, 7, 8, 9]

column, row = 9,9
# tab = [range(row) for _ in range(column)]
tab = [[0 for _ in range(row)] for _ in range(column)]

ft_Display(tab)

for i in range(9):
    k = 0
    for j in input().split():
        n = int(j)
        # print(i,' - ', j, ' : ', n, file=sys.stderr, flush=True)
        tab[i][k] = n
        k += 1

print("", file=sys.stderr, flush=True)
ft_Display(tab)
test = ft_TestRow(tab, reference)
# ft_Display(tab)
if test == "true":
    test = ft_TestColumn(tab, reference)
    # ft_Display(tab)
    if test == "true":
        test = ft_TestSquare(tab, reference)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(test)







# ****************************************************************************************
# ****************************************************************************************
# ****************************************************************************************
# ****************************************************************************************





# d = []
# g = [ [] for x in range(9) ]
# k = True
# for i in range(9):
#     d.append(input().split())
# for i in range(9):
#     for j in range(9):
#         x = 0 if i < 3 and j < 3 else 1 if i < 3 and j >= 3 and j < 6 else 2 if i < 3 else 3 if i >= 3 and i < 6 and j < 3 else 4 if i >= 3 and i < 6 and j >= 3 and j < 6 else 5 if i >= 3 and i < 6 else 6 if i >= 6 and j < 3 else 7 if i >= 6 and j >= 3 and j < 6 else 8
#         g[x].append(d[i][j])
# for i in range(9):
#     k = (len(list(set(d[i]))) == 9 and len(list(set([ x[i] for x in d ]))) == 9 and len(list(set(g[i]))) == 9) if k else k
# print("true" if k else "false")