# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    WordSearchforProgrammers.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/29 10:59:52 by pwolff            #+#    #+#              #
#    Updated: 2024/09/29 11:03:53 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())
tab = []
newtab = []
# finaltab = []
for i in range(size):
    row = input()
    print(i, " ** ", row, file=sys.stderr, flush=True)
    tab.append(row)
clues = input().upper()
words = list(clues.split())





# words.append("HNL")  # ******** Test
# words= ["EUOE"]  # ******** Test
# words= ["E"]  # ******** Test

# words = ["GARFIELD"]

# **********************************************



print(clues, file=sys.stderr, flush=True)
print(len(words), " ** ", words, file=sys.stderr, flush=True)
for mot in words:
    print(" ** ", mot, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


for i in range(size):
    newstring = list(" " * len(tab[0]))
    newtab.append(newstring)

print("\nnewtab = ", newtab, "\n", file=sys.stderr, flush=True)


# ********  Droite  ********
for i in range(len(words)):
    for y in range(size):
        if words[i] in tab[y]:
            print(words[i], " in ", tab[y], file=sys.stderr, flush=True)
            pos = tab[y].find(words[i])
            for k in range(len(words[i])):
                if newtab[y][k + pos] == " ":
                    newtab[y][k + pos] = words[i][k] 
                # print(words[i][k], file=sys.stderr, flush=True) 
                print(newtab[y], file=sys.stderr, flush=True) 

        # else:
        #     print("error",words[i], " not in ", tab[y], file=sys.stderr, flush=True)

# newtab[1][3] = "k" 

# ********  Gauche  ********
for i in range(len(words)):
    chaine_inverse = words[i][::-1]
    # print(words[i], " = ", chaine_inverse, file=sys.stderr, flush=True) 
    for y in range(size):
        if chaine_inverse in tab[y]:
            print(chaine_inverse, " in ", tab[y], file=sys.stderr, flush=True)
            pos = tab[y].find(chaine_inverse)
            for k in range(len(chaine_inverse)):
                if newtab[y][k + pos] == " ":
                    newtab[y][k + pos] = chaine_inverse[k] 
                # print(words[i][k], file=sys.stderr, flush=True) 
                print(newtab[y], file=sys.stderr, flush=True) 


# ********  Bas  ********
for i in range(len(tab[0])):
    newChaine= ""
    for j in range(len(tab)):
        newChaine += tab[j][i]
    print(i, " -- ", newChaine, file=sys.stderr, flush=True)
    for k in range(len(words)):
        if words[k] in newChaine:
            print("match ", words[k], newChaine,  file=sys.stderr, flush=True)
            pos = newChaine.find(words[k])
            for l in range(len(words[k])):
                if newtab[pos + l][i] == " ":
                    newtab[pos + l][i] = words[k][l]

    # *********** Haut **********
    for k in range(len(words)):
        chaine_inverse = words[k][::-1]
        if chaine_inverse in newChaine:
            pos = newChaine.find(chaine_inverse)
            print("match ", chaine_inverse, newChaine,  file=sys.stderr, flush=True)
            for l in range(len(chaine_inverse)):
                if newtab[pos + l][i] == " ":
                    newtab[pos + l][i] = chaine_inverse[l]




# ******** Diagonale Haut - BasDroite **********   

# https://openclassrooms.com/forum/sujet/diagonale-matrice-2d

def diag(M, i):
    ligne, col = (abs(i), 0) if i < 0 else (0, i)
    result = ""
    while ligne < len(M) and col < len(M[0]):
        result += (M[ligne][col])
        ligne += 1
        col += 1
    return result


for i in range(len(tab[0])):
    Diago = diag(tab, i)
    print(Diago, file=sys.stderr, flush=True)
    for word in range(len(words)):
        if words[word] in Diago:
            pos = Diago.find(words[word])
            print("match ", words[word], Diago,  file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                if newtab[pos + j][i + pos + j] == " ":
                    newtab[pos + j][i + pos + j] = words[word][j]
            # break
        chaine_inverse = words[word][::-1]
        if chaine_inverse in Diago:
            pos = Diago.find(chaine_inverse)
            print("match ", words[word], Diago,  file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                if newtab[pos + j][i + pos + j] == " ":
                    newtab[pos + j][i + pos + j] = chaine_inverse[j]



for i in range(1, len(tab[0])):
    ii = -i
    Diago = diag(tab, ii)
    print(Diago, file=sys.stderr, flush=True) 
    for word in range(len(words)):
        if words[word] in Diago:
            pos = Diago.find(words[word])
            print("match ", words[word], Diago,  file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                if newtab[i + pos + j][pos + j] == " ":
                    newtab[i + pos + j][pos + j] = words[word][j]
            # break
        chaine_inverse = words[word][::-1]
        if chaine_inverse in Diago:
            pos = Diago.find(chaine_inverse)
            print("match ", words[word], Diago,  file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                if newtab[i + pos + j][pos + j] == " ":
                    newtab[i + pos + j][pos + j] = chaine_inverse[j]
    




# ******** Diagonale Haut Droit - Bas Gauche **********   

def diagInverse(M, i):
    # ligne, col = (abs(i), 0) if i < 0 else (0, i)
    # result = []
    # while ligne < len(M) and col < len(M[0]):
    #     result.append(M[ligne][col])
    #     ligne += 1
    #     col += 1
    # return result
    # print(" **** ", file=sys.stderr, flush=True)
    # ligne, col = (len(M) - abs(i) - 1, len(M[0]) - 1) if i < 0 else (0, len(M[0] - i - 1))
    ligne, col = (abs(i), len(M[0]) - 1) if i < 0 else (0, i)
    result = ""
    # print(" **** ", ligne, col, file=sys.stderr, flush=True)
    while ligne < len(M) and col >= 0:
        # print(ligne, col, file=sys.stderr, flush=True)
        result += (M[ligne][col])
        ligne += 1
        col -= 1
    return result

print("\n********  Diago droite - gauche ********\n", file=sys.stderr, flush=True)

for i in range(len(tab[0])):
    Diago = diagInverse(tab, i)
    print(Diago, file=sys.stderr, flush=True)
    for word in range(len(words)):
        if words[word] in Diago:
            print("match ", words[word], Diago,  file=sys.stderr, flush=True)
            pos = Diago.find(words[word])
            for j in range(len(words[word])):
                if newtab[pos + j][i - pos - j] == " ":
                    newtab[pos + j][i - pos - j] = words[word][j]
            # break
        chaine_inverse = words[word][::-1]
        if chaine_inverse in Diago:
            print("match ", chaine_inverse, Diago,  file=sys.stderr, flush=True)
            pos = Diago.find(chaine_inverse)
            for j in range(len(words[word])):
                if newtab[pos + j][i - pos - j] == " ":
                    newtab[pos + j][i - pos - j] = chaine_inverse[j]

print("\n******** Part II ********\n", file=sys.stderr, flush=True)

for i in range(1, len(tab[0])):
    Diago = diagInverse(tab, -i)
    print(Diago, file=sys.stderr, flush=True)
    for word in range(len(words)):
        if words[word] in Diago:
            pos = Diago.find(words[word])
            print("match ", words[word], Diago, " i = ", i, "pos = ",pos, file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                # newtab[len(newtab) - (pos + j + i)][i + pos + j] = words[word][j]
                # newtab[(pos + j + i)][len(newtab[0]) - (i + pos + j)] = words[word][j]
                if newtab[(pos + j + i)][len(newtab[0]) - (pos + j + 1)] == " ":
                    newtab[(pos + j + i)][len(newtab[0]) - (pos + j + 1)] = words[word][j]

                # newtab[(pos + j + i)][(pos - j + i)] = words[word][j]


            # break
        chaine_inverse = words[word][::-1]
        if chaine_inverse in Diago:
            pos = Diago.find(chaine_inverse)
            print("match ", words[word], Diago, "reverse :  i = ", i, "pos = ",pos, file=sys.stderr, flush=True)
            for j in range(len(words[word])):
                if newtab[(pos + j + i)][len(newtab[0]) - 1 - (pos + j)] == " ":
                    newtab[(pos + j + i)][len(newtab[0]) - 1 - (pos + j)] = chaine_inverse[j]
    







    
    # # print(words[i], " = ", chaine_inverse, file=sys.stderr, flush=True) 
    # for y in range(size):
    #     if newChaine in tab[y]:
    #         print(newChaine, " in ", tab[y], file=sys.stderr, flush=True)
    #         pos = tab[y].find(newChaine)
    #         for k in range(len(newChaine)):
    #             newtab[y][k + pos] = newChaine[k] 
    #             # print(words[i][k], file=sys.stderr, flush=True) 
    #             print(newtab[y], file=sys.stderr, flush=True) 

print("\nnewtab = ", newtab, "\n", file=sys.stderr, flush=True)


for i in range(size):
    print("".join(newtab[i]))




# *********************************************************************************************************************
# *********************************************************************************************************************
# *********************************************************************************************************************



import sys
import re


NEXT_STEP = [  # carré des possibilités
    "c-1, l-1",     "c, l-1",   "c+1, l-1",
    "c-1, l",                   "c+1, l",
    "c-1, l+1",     "c, l+1",   "c+1, l+1"
]

def log(*args):
    print(*args, file=sys.stderr, flush=True)

def find_direction(l, c, mot):
    for step in range(len(NEXT_STEP)):
        if (result := find_word(l, c, mot, step, 1)) != None:
            result.append((l, c))
            return result[:0:-1]

def find_word(l, c, mot, step, index):
    if index == len(mot):
        return ['']
    x, y = eval(NEXT_STEP[step])
    if 0 <= x < X and 0 <= y < Y and mot[index] == GRILLE[y][x]:
        if (soluce := find_word(y, x, mot, step, index + 1)):
            soluce.append((y, x))
            return soluce



rows = int(input())
GRILLE = [input() for _ in range(rows)]
mots = map(lambda mot: mot.upper(), input().split())

lines = [[" " for _ in range(len(GRILLE[0]))] for _ in range(rows)]
log(lines)
X = len(GRILLE[0])
Y = len(GRILLE)



for mot in mots:
    flag = False
    for l, line in enumerate(GRILLE):
        for c in re.finditer(mot[0], line):
            if (soluce := find_direction(l, c.start(), mot)):
                for index, lettre in enumerate(soluce):
                    lines[lettre[0]][lettre[1]] = mot[index]
                flag = True
                break
        if flag:
            break


for line in lines:
    print(''.join(line))
