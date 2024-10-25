# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_parenthesesPourEquation.py                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/25 08:34:57 by pwolff            #+#    #+#              #
#    Updated: 2024/10/25 08:51:27 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import math

equation = "3+25-6/2=6"

listSolution = []

travail = equation.split("=")[0] + "$"
print("equation : ", equation)
print("travail : ", travail)

# i = 0
for i in range(len(travail)):

    if i == 0 or travail[i].isnumeric() and not travail[i - 1].isnumeric():
        temp = travail[:i] + "(" + travail[i:]
        print("temp : ", temp)
        
        # for j in range(len(temp)):

    
    i += 1

print("--- END ---")




