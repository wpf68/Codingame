# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    theIndex.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/06 10:07:15 by pwolff            #+#    #+#              #
#    Updated: 2024/06/06 10:12:12 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

string = "Hello World!"

print(string.index("World!")) # The first letter of this substring in at index 6.

string = "Hello World!"

print(string.index("l")) # There are three letter l's in "Hello World!", but the first occurence is at index 2.


list = ['H', 'e', 'l', 'l', 'o']

print(list.index("e")) # The only occurence of "e" is at index 1.

tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(tuple.index(8)) # The first occurence of "8" is at index 3.
