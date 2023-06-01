# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    python.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42mulhouse.fr>>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 16:20:42 by pwolff            #+#    #+#              #
#    Updated: 2023/05/31 16:20:42 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

result = ""
temp = ""
unary = ""
message = input()
print(message, file = sys.stderr)

for lettre in message:
    print(lettre, file = sys.stderr)
    temp = (bin(ord(lettre))[2:])
    while True:
        if (len(temp) < 7):
            temp = "0" + temp
        else :
            break
    result += temp

i = 0
while (i < len(result)):
    print(result[i], file = sys.stderr)
    if result[i] == '1':
        unary += "0 "
    else :
        unary += "00 "
    temp = ""
    j = i
    while (j < len(result) and result[j] == result[i]):
        temp += "0"
        j += 1
    unary += temp

    
    i = j
    if i < len(result):
        unary += " "



    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(temp, file = sys.stderr)
print(result, file = sys.stderr)

print(unary)

