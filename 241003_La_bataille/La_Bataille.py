# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    La_Bataille.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/03 09:07:58 by pwolff            #+#    #+#              #
#    Updated: 2024/10/03 09:12:16 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

manches = 0

player1 = []
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    player1.append(cardp_1)

#test
# player1.append("3C")
# player1.append("10C")

player2 = []
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    player2.append(cardp_2)

def display():
    print("\nplayer1 : ", len(player1), "\n", player1[:], file=sys.stderr, flush=True)
    print("\nplayer2 : ", len(player2), "\n", player2[:], file=sys.stderr, flush=True)

display()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def valueCart(cart):
    if len(cart) == 3:
        return 10
    tab = ["0","1","2","3","4","5","6","7","8","9","Z","J","Q","K","A"]
    return tab.index(cart[0])


# test Value
# for carte in player1:
#     print(carte, " = ", valueCart(carte), file=sys.stderr, flush=True)


def bataille(player1, player2, x):
    if len(player1) < 4 * x or len(player2) < 4 * x:
        print("PAT")
        exit()
    if valueCart(player1[(4 * x) - 1]) > valueCart(player2[(4 * x) - 1]):
        return 1
    if valueCart(player1[(4 * x) - 1]) < valueCart(player2[(4 * x) - 1]):
        return 2
    return 0

def gagne(player1, toPlayer2, x):
    x *= 4
    while x:
        player1.append(toPlayer2[0])
        del toPlayer2[0]
        x -= 1
    pass



while True:
    round = 1
    if not(len(player1)) or not(len(player2)):
        break

    cartePlayer1 = player1[0]
    del player1[0]
    cartePlayer2 = player2[0]
    del player2[0]
    if valueCart(cartePlayer1) > valueCart(cartePlayer2):
        player1.append(cartePlayer1)
        player1.append(cartePlayer2)
    elif valueCart(cartePlayer1) < valueCart(cartePlayer2):
        player2.append(cartePlayer1)
        player2.append(cartePlayer2)

    else :
        print("\n*** Bataille ***\n", file=sys.stderr, flush=True)
        if len(player1) < 4 or len(player2) < 4:
            print("PAT")
            exit()
        
        while True:
            result = bataille(player1, player2, round)
            if result == 0:
                round += 1
            elif result == 1:
                player1.append(cartePlayer1)
                gagne(player1, player1, round)
                player1.append(cartePlayer2)
                gagne(player1, player2, round)
                break
            elif result == 2:
                player2.append(cartePlayer1)
                gagne(player2, player1, round)
                player2.append(cartePlayer2)
                gagne(player2, player2, round)

                break

        

    display()

    manches += 1

    
    # print("Debug messages...", file=sys.stderr, flush=True)
    # player1[:] = []


if len(player1):
    print("1", manches)
else :
    print("2", manches)




# print("PAT")




# ***************************************************************************


import sys
import math
sys.setrecursionlimit(10000)
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

joueur1 = []
joueur2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    joueur1.append(input())  # the n cards of player 1

m = int(input())  # the number of cards for player 2
for i in range(m):
    joueur2.append(input())

def tournois(j1, j2, cote1, cote2, nb_tour):
    #print(j2,file=sys.stderr)
    if not j1:
        return print(f"{2} {nb_tour}")
    elif not j2:
        return print(f"{1} {nb_tour}")
    
    carte1 = j1.pop(0)
    carte2 = j2.pop(0)

    if values[carte1[:-1]] > values[carte2[:-1]]:
        tournois(j1 + cote1 + [carte1] + cote2 + [carte2], j2, [], [], nb_tour + 1)
    elif values[carte1[:-1]] < values[carte2[:-1]]:
        tournois(j1, j2 + cote1 + [carte1] + cote2 + [carte2], [], [], nb_tour + 1)
    else:
        if len(j1) < 4 or len(j2) < 4:
            return print("PAT")
        else:
            tournois(j1[3:], j2[3:], cote1 + [carte1] + [j1[0]] + [j1[1]] + [j1[2]], cote2 + [carte2] + [j2[0]] + [j2[1]] + [j2[2]], nb_tour)

tournois(joueur1, joueur2, [], [], 0)