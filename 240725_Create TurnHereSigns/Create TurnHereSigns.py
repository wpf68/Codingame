# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Create TurnHereSigns.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/25 14:03:34 by pwolff            #+#    #+#              #
#    Updated: 2024/07/25 14:03:51 by pwolff           ###   ########.fr        #
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

# print("The Turn Here Sign")