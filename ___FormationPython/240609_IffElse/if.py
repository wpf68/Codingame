# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    if.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/09 15:02:38 by pwolff            #+#    #+#              #
#    Updated: 2024/06/09 15:21:13 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

a = 6

print("True" if a == 5 else "False")




def PigLatin(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if string[0].lower() in vowels:
        return string + "yay"
    else:
        for i in range(len(string)):
            if string[i].lower() in vowels:
                return string[i:].lower() + string[:i].lower() + "ay"


sentence = str(input("Enter a string: ")).split(" ")
answer = ""

for word in sentence:
    answer+=PigLatin(word)+" "

print(answer.strip().lower())



# Define a word:
word = "HAELLOWZ helloaz"
print(word)

# Create a variable called shift, which can be negative or positive:
shift = 3

# Create a function to encode input and return the result:
def Caesar(word, shift):
    encoded = ""
    for char in word:
        # The integer '97' is the ordinal value in Unicode Point Code that represents the character "a".
        encoded += chr(((ord(char) - 97 + shift) % 26) + 97)
    # Check the case of the word, and match the case for the encoding.
    if word.isupper():
        return encoded.upper()
    else:
        return encoded

print(Caesar(word, shift))

