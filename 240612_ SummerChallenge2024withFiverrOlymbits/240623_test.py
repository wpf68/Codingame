# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240323_test.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/23 09:57:54 by pwolff            #+#    #+#              #
#    Updated: 2024/06/23 09:57:57 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())
move = ["UP", "LEFT", "DOWN", "RIGHT"]



print("player_idx = ", player_idx, file=sys.stderr, flush=True)
print("nb_games = ", nb_games, file=sys.stderr, flush=True)

# game loop
while True:
    pos_player = []
    gpu = []
    len_gpu = 0
    comboJeux4 = []

    comboJ2 = []
    comboJ3 = []

    for i in range(3):
        score_info = input()
    for i in range(nb_games):
        inputs = input().split()
        gpu.append(inputs[0] + "...")
        len_gpu = len(gpu[0])
        print("** len *** ", len_gpu, file=sys.stderr, flush=True)
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])

        pos_player.append(int(inputs[1 + player_idx]))
        comboJeux4.append(int(inputs[1 + player_idx]))
        print("** Joueur *** ", 1 + player_idx, file=sys.stderr, flush=True)
        player = (1 + player_idx) % 3 + 1
        print("** Player *** ", player, file=sys.stderr, flush=True)
        comboJ2.append(int(inputs[player]))
        player = (2 + player_idx) % 3 + 1
        print("** Player *** ", player, file=sys.stderr, flush=True)
        comboJ3.append(int(inputs[player]))


        if inputs[0] == "GAME_OVER...":
            pos_player[player_idx] = 0





    # posjeux4 = 0

    if comboJeux4[3] <= comboJ2[3] and comboJeux4[3] <= comboJ3[3]:
        if gpu[3][0] == 'R':
            print("RIGHT")
        elif gpu[3][0] == 'D':
            print("DOWN")
        elif gpu[3][0] == 'L':
            print("LEFT")
        else :
            print("UP") 


    elif "#" in gpu[0][pos_player[0]:]:
        print(pos_player[player_idx], gpu[0], file=sys.stderr, flush=True)

        str = gpu[0][pos_player[0]:pos_player[0] + 3]
        gpu[3][pos_player[3]:pos_player[3] + 1]

        

        movePlayer = 0

        str = gpu[0][pos_player[0] + 1:pos_player[0] + 2]   
        if str == ".":
            movePlayer = 1

        str = gpu[0][pos_player[0] + 1:pos_player[0] + 3]
        if str == "..":
            movePlayer = 2

        str = gpu[0][pos_player[0] + 1:pos_player[0] + 4]
        if str == "...":
            movePlayer = 3

        print(move[movePlayer])



    else :
        if gpu[3][0] == 'R':
            print("RIGHT")
        elif gpu[3][0] == 'D':
            print("DOWN")
        elif gpu[3][0] == 'L':
            print("LEFT")
        else :
            print("UP")

    # else:
    #     str = gpu[0][pos_player[0]:pos_player[0] + 3]
    #     gpu[3][pos_player[3]:pos_player[3] + 1]

        

    #     movePlayer = 0

    #     str = gpu[0][pos_player[0] + 1:pos_player[0] + 2]   
    #     if str == ".":
    #         movePlayer = 1

    #     str = gpu[0][pos_player[0] + 1:pos_player[0] + 3]
    #     if str == "..":
    #         movePlayer = 2

    #     str = gpu[0][pos_player[0] + 1:pos_player[0] + 4]
    #     if str == "...":
    #         movePlayer = 3

    #     print(move[movePlayer])    



    




    print("combo jeux 4 : ", comboJeux4[3],file=sys.stderr, flush=True)