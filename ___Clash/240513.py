# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240513.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/13 14:26:49 by pwolff            #+#    #+#              #
#    Updated: 2024/05/13 14:32:43 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input("value : "))
# print(n)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

temp = "#" * (n * 2 + 3)
result = [""] * (n * 2 + 3)

result[0] = temp
result[((n * 2 + 3) - 1)] = temp

for i in range(n):
    result[(i + 1)] = "#" + " " * i + "X" + " " * ((2 * (n - i - 1) + 1)) + "X" + " " * i + "#"

result[(n + 1)] = "#" + " " * n + "X" + " " * n + "#"

for ligne in range (n):
    result[(n + 2 + ligne)] = result[(n - ligne)] 

for value in result:
    print(value)
