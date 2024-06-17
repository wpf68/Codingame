# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240617_Ligue2.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/17 12:21:37 by pwolff            #+#    #+#              #
#    Updated: 2024/06/17 13:55:31 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

move = ["UP", "LEFT", "DOWN", "RIGHT"]

player_idx = int(input())
nb_games = int(input())



print("player_idx = ", player_idx, file=sys.stderr, flush=True)
print("nb_games = ", nb_games, file=sys.stderr, flush=True)


def testFirstPlayer(pos_player, pos_enemi_1, pos_enemi_2):
    result_i = 0
    test = -1000
    for i in range(nb_games):
        if pos_player[i] - pos_enemi_1[i] > pos_player[i] - pos_enemi_2[i]:
            result = pos_player[i] - pos_enemi_1[i]
        else :
            result = pos_player[i] - pos_enemi_2[i]
        if result > test:
            test = result
            result_i = i
    return result_i


def testOutPlayer(pos_player, pos_enemi_1, pos_enemi_2):
    ecart = -3
    if pos_player - pos_enemi_1 < ecart or pos_player - pos_enemi_2 < ecart:
        return False
    return True

def test_saut(gpu, pos_player, etourdissement_player):
    compteur = 0
    for i in range(nb_games):
        if etourdissement_player[i] == 0:
            if gpu[i][pos_player[i] + 2] == "#":
                compteur += 1
    if compteur > 2:
        return 1
    return 0



# game loop
while True:

    pos_player = []
    gpu = []

    pos_enemi_1 = []
    pos_enemi_2 = []

    etourdissement_player = []

    
    print("player_idx = ", player_idx, file=sys.stderr, flush=True)
    print("nb_games = ", nb_games, file=sys.stderr, flush=True)
    for i in range(3):
        score_info = input()
        print("Score", i, " = ", score_info, file=sys.stderr, flush=True)
    for i in range(nb_games):
        inputs = input().split()
        gpu.append(inputs[0]+"    ")
        len_gpu = len(gpu[i])
        print(gpu, " len = ", len_gpu, file=sys.stderr, flush=True)
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])
        pos_player.append(int(inputs[1 + player_idx]))

        etourdissement_player.append(int(inputs[4 + player_idx]))


        pos_enemi_1.append(int(inputs[2]))
        pos_enemi_2.append(int(inputs[3]))

        if len_gpu == 13:
            pos_player[i] = 0
        print("i = ", i, file=sys.stderr, flush=True )
        print("position de l'agent du joueur ", player_idx, " = ", pos_player[i], file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # for i in range(nb_games):
    #     print("**** p i = ", i, " = ", pos_player[i], "type = ", type(pos_player[i])  , file=sys.stderr, flush=True)


    

    # i = testFirstPlayer(pos_player, pos_enemi_1, pos_enemi_2)
    # if pos_player[i] < len(gpu[i]) - 3 and gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." and gpu[i][pos_player[i] + 3] == ".":
    #     movePlayer = 3
    # elif pos_player[i] < len(gpu[i]) - 2 and gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." :
    #     movePlayer = 2
    # elif pos_player[i] == len(gpu[i]) or gpu[i][pos_player[i] + 1] == ".":
    #     movePlayer = 1
    # else:
    #     movePlayer = 0

    # print(move[movePlayer])



    # movePlayerFinal = 4
    # for i in range(nb_games):

    #     if pos_player[i] < len(gpu[i]) - 3 and gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." and gpu[i][pos_player[i] + 3] == ".":
    #         movePlayer = 3
    #     elif pos_player[i] < len(gpu[i]) - 2 and gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." :
    #         movePlayer = 2
    #     elif pos_player[i] == len(gpu[i]) or gpu[i][pos_player[i] + 1] == ".":
    #         movePlayer = 1
    #     else:
    #         movePlayer = 0
    #     if movePlayer < movePlayerFinal:
    #         movePlayerFinal = movePlayer

    # print(move[movePlayerFinal])


    movePlayerFinal = 3
    for i in range(nb_games):
        print("etourdissement_player i = ", i, " = ", etourdissement_player[i], file=sys.stderr, flush=True)
        if etourdissement_player[i] == 0:
            if testOutPlayer(pos_player[i], pos_enemi_1[i], pos_enemi_2[i]):
                if gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." and gpu[i][pos_player[i] + 3] == ".":
                    movePlayer = 3
                elif gpu[i][pos_player[i] + 1] == "." and gpu[i][pos_player[i] + 2] == "." :
                    movePlayer = 2
                elif pos_player[i] == len(gpu[i]) or gpu[i][pos_player[i] + 1] == ".":
                    movePlayer = 1
                else:
                    movePlayer = 0
                if movePlayer == 0:
                    movePlayer = test_saut(gpu, pos_player, etourdissement_player)
                if movePlayer < movePlayerFinal:
                    movePlayerFinal = movePlayer

    print(move[movePlayerFinal])

    # print("RIGHT")
