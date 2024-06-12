# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240612_Ligue1.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:57:47 by pwolff            #+#    #+#              #
#    Updated: 2024/06/12 10:59:01 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())
print("player_idx = ", player_idx, file=sys.stderr, flush=True)
print("nb_games = ", nb_games, file=sys.stderr, flush=True)


# game loop
while True:
    print("player_idx = ", player_idx, file=sys.stderr, flush=True)
    print("nb_games = ", nb_games, file=sys.stderr, flush=True)
    for i in range(3):
        score_info = input()
        print("Score", i, " = ", score_info, file=sys.stderr, flush=True)
    for i in range(nb_games):
        inputs = input().split()
        gpu = inputs[0]
        len_gpu = len(gpu)
        print(gpu, " len = ", len_gpu, file=sys.stderr, flush=True)
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])
        pos_player = int(inputs[1 + player_idx])
        if len_gpu == 9:
            pos_player = 0
        print("position de l'agent du joueur ", player_idx, " = ", pos_player, file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)



    if pos_player < len(gpu) - 3 and gpu[pos_player + 1] == "." and gpu[pos_player + 2] == "." and gpu[pos_player + 3] == ".":
        print("RIGHT")
    elif pos_player < len(gpu) - 2 and gpu[pos_player + 1] == "." and gpu[pos_player + 2] == "." :
        print("DOWN")
    elif pos_player == len(gpu) or gpu[pos_player + 1] == ".":
        print("LEFT")
    else:
        print("UP")

    # print("RIGHT")


