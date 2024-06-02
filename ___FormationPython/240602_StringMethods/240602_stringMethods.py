# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    240602_stringMethods.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/02 10:55:14 by pwolff            #+#    #+#              #
#    Updated: 2024/06/02 11:10:39 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import platform
import os

print(platform.system())

def Clean():
    
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
 
print("Le texte a effacer")
# Clean()



string = "Hello World"
border20 = "*" * 20
border100 = "*" * 100

print(string)
print(border20)
print(string.center(20))
print(border100)


print(string.center(100))
print(string.rjust(100))



# ****************************************************

Clean()

for i in range(100 - len(string)):
    print(border100)
    print(string.rjust(100 - i))
    Clean()
    



