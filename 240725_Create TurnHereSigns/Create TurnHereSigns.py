# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Create TurnHereSigns.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/25 14:03:34 by pwolff            #+#    #+#              #
#    Updated: 2024/08/01 07:57:29 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_input = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print(_input)
liste = _input.split()
print(liste, file=sys.stderr, flush=True)


if liste[0] == 'right':
    char = '>'

    model = ""
    i = int(liste[3])
    while i:
        model += char
        i -= 1


    space = ""
    i = int(liste[4])
    while i:
        space += " "
        i -= 1

    ligne = ""
    i = int(liste[1]) - 1
    while i:
        ligne += model + space
        i -= 1
    ligne += model


    additionalIndentOfEachLine = ""
    i = int(liste[5])
    while i:
        additionalIndentOfEachLine += " "
        i -= 1


    result = []
    result.append(ligne)
    i = int(liste[2]) - 1
    while i:
        ligne = additionalIndentOfEachLine + ligne
        result.append(ligne)
        i -= 1

    lenResult = len(result)
    i = lenResult
    while i > lenResult / 2:
        result[i - 1] = result[lenResult - i]
        i -= 1


    print("char     : ", char, file=sys.stderr, flush=True)
    print("model    : ", model, len(model), file=sys.stderr, flush=True)
    print("space    : ", space, len(space), file=sys.stderr, flush=True)
    print("ligne    : ", ligne, len(ligne), file=sys.stderr, flush=True)
    print("ad space : ", additionalIndentOfEachLine, len(additionalIndentOfEachLine), file=sys.stderr, flush=True)

    print(result, len(result), file=sys.stderr, flush=True)

    i = 0
    while i < lenResult:
        print(result[i])
        i += 1




else:
    char = '<'

    model = ""
    i = int(liste[3])
    while i:
        model += char
        i -= 1

    space = ""
    i = int(liste[4])
    while i:
        space += " "
        i -= 1

    ligne = ""
    i = int(liste[1]) - 1
    while i:
        ligne += model + space
        i -= 1
    ligne += model

    additionalIndentOfEachLine = ""
    i = int(liste[5])
    while i:
        additionalIndentOfEachLine += " "
        i -= 1

    spaceMax = ""
    i = 1
    while i < int(liste[2]) / 2:
        spaceMax += additionalIndentOfEachLine
        i += 1

    ligneMax = spaceMax + ligne
    

    espace = ligneMax.find("<")

    result = []
    # result.append(ligne)
    i = 0
    while i < int(liste[2]) / 2:
        ligne = ligneMax[(i * len(additionalIndentOfEachLine)) :]
        # ligne = ligneMax[(i * 2) :]
        result.append(ligne)
        i += 1

    i = len(result) - 1
    while i:
        ligne = ligneMax[((i - 1) * len(additionalIndentOfEachLine)) :]
        result.append(ligne)
        i -= 1


    print("char     : ", char, file=sys.stderr, flush=True)
    print("model    : ", model, len(model), file=sys.stderr, flush=True)
    print("space    : ", space, len(space), file=sys.stderr, flush=True)
    print("ligne    : ", ligne, len(ligne), file=sys.stderr, flush=True)

    print("ligne Max: ", ligneMax, len(ligneMax), file=sys.stderr, flush=True)
    # print("ligne Max: ", ligneMax[5:], len(ligneMax[5:]), file=sys.stderr, flush=True)

    print("ad space : ", additionalIndentOfEachLine, len(additionalIndentOfEachLine), file=sys.stderr, flush=True)
    print("espace   : ", espace, "\n", file=sys.stderr, flush=True)


    i = 0
    while i < len(result):
        print(result[i])
        i += 1
# print("The Turn Here Sign")





# ***********************************************************************************************

d,*rest = input().split()
TurnRight = d=='right'
n,height,width,space,offset = map(int, rest)
line = (' '*space).join(['<>'[TurnRight]*width]*n)
yc = height//2
for indent in [abs(y-yc) for y in range(height)]:
    if TurnRight: indent = yc-indent
    print(' '*offset*indent + line)


# ***********************************************************************************************

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

direction, *ints = input().split()
amt, height, width, space, indent = map(int, ints)
sym = "<>"[direction == "right"]

for i in range(height):
    if i > int(height / 2):
        i = height - i - 1
    
    if direction == "left":
        i = int(height / 2) - i

    print(end=" " * (i * indent))
    print(*([sym * width] * amt), sep=" " * space)

# ***********************************************************************************************

