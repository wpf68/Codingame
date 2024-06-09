# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numberPrime.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/06 11:46:38 by pwolff            #+#    #+#              #
#    Updated: 2024/06/06 12:11:34 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def numberPrime(number):
    if number < 2:
        return False
    for test in range(2, number):
        if number % test == 0:
            return False
    return True

for test in range (0, 100):
    if numberPrime(test):
        print(str(test).rjust(3), "  --  True")