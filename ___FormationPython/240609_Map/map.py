# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    map.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/09 14:15:21 by pwolff            #+#    #+#              #
#    Updated: 2024/06/09 14:38:29 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

string = "1 2 3 4"

a, b, c, d = map(int, string.split(" "))


print(a, b, c, d, type(a))

a, b, c, d = string.split(" ")


print(a, b, c, d, type(a))

liste = range(1, 10)
print(liste)
print(liste[3])


def display(x):
    print(x, "x 2 = ", x*2)
    return x * 2


result = map(display, liste)

print("result = ", result)
print(list(result))

def adition(x, y):
    return x + y



result2 = map(adition, liste, range(10, 19))
print(list(result2))

result2 = map(adition, liste, range(10, 15))
print(list(result2))

print("\n********** Puissance ************\n")
print(list(liste))
print(list(map(lambda x: x**2, liste)))