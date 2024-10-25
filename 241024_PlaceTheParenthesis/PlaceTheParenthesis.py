# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PlaceTheParenthesis.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/25 08:19:29 by pwolff            #+#    #+#              #
#    Updated: 2024/10/25 08:32:51 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

equ = []
calcul = ""
dataResult = []


def splitSous(calcul):
    split = []
    i = 1
    # if calcul[0] == "-":
    #     split.append('-')
    while calcul[i]:
        if calcul[i] == '=':
            split.append(calcul)
            return split
        if calcul[i] == '-':
            split.append(calcul[:i])
            split.append(calcul[i+1:])
            return split
        i += 1
    
    print("//// ERROR splitSous", file=sys.stderr, flush=True)
    split.append(calcul)
    return split


def clean(firstPart):
    while True:
        # print("-- Clean = ", firstPart[-1:], file=sys.stderr, flush=True)
        if firstPart[-1:].isnumeric():
            firstPart = firstPart[:len(firstPart) - 1]
        else:
            break
    return firstPart


def testInt(string, sens):
    value = 0
    if sens == 1:
        for i in string:
            if i.isnumeric():
                value += 1
            else:
                break
    else:
        for i in reversed(string):
            if i.isnumeric():
                value -= 1
            else:
                break
    # print("-- Value = ", value, file=sys.stderr, flush=True)
    return value

def multiplication(multi, calcul):
    # a = int(multi[0].split("+|-|*|/|=")[len(multi[0].split("+|-|*|/|=")) - 1])
    # b = int(multi[1].split("=")[0])
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    b = int(multi[1][:testInt(multi[1], 1)])
    print("A = ", a, file=sys.stderr, flush=True)
    print("B = ", b, file=sys.stderr, flush=True)
    c = a * b
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    # print("firstPart = ", firstPart, file=sys.stderr, flush=True)
    # print("firstPart = ", firstPart[:len(firstPart) - len(str(a))], file=sys.stderr, flush=True)

    firstPart = clean(firstPart)
    # print("Clean firstPart = ", firstPart, file=sys.stderr, flush=True)

    # if len(firstPart) <= 1 and multi[0][:len(str(a)) + 1].isnumeric():
    #     newString = str(c) + multi[1][len(str(b)):]   
    # else:  
        # newString = multi[0][:len(str(a)) + 1] + str(c) + multi[1][len(str(b)):]
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)

def division(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    b = int(multi[1][:testInt(multi[1], 1)])
    print("A = ", a, file=sys.stderr, flush=True)
    print("B = ", b, file=sys.stderr, flush=True)
    c = round(a / b)
    # creation d'une erreur en cas de division non entiere *******************************
    if c * 100 - round(a / b * 100) != 0:
        c = 100 
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    firstPart = clean(firstPart)
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)

def addition(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    if len(multi[0]) - len(str(a)) == 1:
        a = -a
    b = int(multi[1][:testInt(multi[1], 1)])
    print("A = ", a, file=sys.stderr, flush=True)
    print("B = ", b, file=sys.stderr, flush=True)
    c = (a + b)
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    firstPart = clean(firstPart)
    # newString = firstPart + str(c) + multi[1][len(str(b)):]
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)

def soustraction(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    if len(multi[0]) - len(str(a)) == 1:
        a = -a
    b = int(multi[1][:testInt(multi[1], 1)])
    print("A = ", a, file=sys.stderr, flush=True)
    print("B = ", b, file=sys.stderr, flush=True)
    c = (a - b)
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    firstPart = clean(firstPart)
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)


def blok(calcul):
    value = 0
    # travail = calcul
    while True:
        multi = calcul.split('*')
        print("Multiplications : ", multi, file=sys.stderr, flush=True)
        while True:
            if len(multi) > 2:
                temp = multi[1] + "*" + multi[2]
                multi[1] = temp
                del multi[2]
            else:
                break
        if len(multi) == 1:
            break
        calcul = multiplication(multi, calcul)
        # print("BREAK", file=sys.stderr, flush=True)
        # break
    while True:
        div = calcul.split('/')
        print("Divisions : ", div, file=sys.stderr, flush=True)
        while True:
            if len(div) > 2:
                temp = div[1] + "/" + div[2]
                div[1] = temp
                del div[2]
            else:
                break
        if len(div) == 1:
            break
        calcul = division(div, calcul)
        # break


    while True:
        # soustract = calcul.split('-')
        # soustract = []
        soustract = splitSous(calcul)
        print("Soustraction : ", soustract, file=sys.stderr, flush=True)
        while True:
            if len(soustract) > 2:
                temp = soustract[1] + "-" + soustract[2]
                soustract[1] = temp
                del soustract[2]
            else:
                break
        if len(soustract) == 1:
            break
        print("Soustraction : ", soustract, file=sys.stderr, flush=True)
        calcul = soustraction(soustract, calcul)




    while True:
        add = calcul.split('+')
        print("Additions : ", add, file=sys.stderr, flush=True)
        while True:
            if len(add) > 2:
                temp = add[1] + "+" + add[2]
                add[1] = temp
                del add[2]
            else:
                break
        if len(add) == 1:
            break
        calcul = addition(add, calcul)
        # break

    #     break

    # print("Multiplications : ", multi, file=sys.stderr, flush=True)
    # print("Divisions : ", div, file=sys.stderr, flush=True)
    return calcul


n = int(input())
for i in range(n):
    equation = input()
    print(i, "Equ :", equation, file=sys.stderr, flush=True)
    equ.append(equation)

# print("Equ :", equ[:], file=sys.stderr, flush=True)

def testError(result):
    test = result.split('=')
    if int(test[0]) == int(test[1]):
        return True
    return False




for equation in equ:
    # print("*** Travail sur :", equation, file=sys.stderr, flush=True)
    # print("    = ", blok(equation), file=sys.stderr, flush=True)

    test = True
    # while test:
    equationPart = equation.split('=')

    # for i in range(len(equationPart[0])):
    #     if equationPart[0][i].isnumeric() and i == 0 or equationPart[0][i].isnumeric() and not equationPart[0][i-1].isnumeric():
    #         flack = 0

    #         for j in range(len(equationPart[0]) - i):
    #             if equationPart[0][i + j].isnumeric():
    #                 j += 1
    #                 continue
    #             else:
    #                 flack +=1
    #                 if flack == 1:
    #                     j += 1
    #                     continue
    #                 else:
    #                     newEquation = equation[i:j] + "="
    #                     print("*** newEquation :", newEquation, file=sys.stderr, flush=True)
    #                     resultat = blok(newEquation)
    #                     print("*** resultat :", resultat[:-1], file=sys.stderr, flush=True)
    #                     newEquation = resultat[:-1] + equation[j:]
    #                     print("*** newEquation :", newEquation, file=sys.stderr, flush=True)
    #                     resultat = blok(newEquation)
    #                     print("*** resultat :", resultat, file=sys.stderr, flush=True)
    #                     if testError(resultat) == False:
    #                         equation = equation[:i] + "(" +  equation[i:j] + ")" + equation[j:]
    #                         print("*** resultat WIN :", equation, file=sys.stderr, flush=True)
    #                         dataResult.append(equation)
    #                         test = False
    #                         break
                        

    #     if not test:
    #         break



        # break

            # else:
            #     i += 1
            #     if i >= len(equationPart[0]):
            #         print("//////  Error i ()", file=sys.stderr, flush=True)
            #         break
            #     continue




    resultat = blok(equation)
    print("\n*** Travail sur :", equation, file=sys.stderr, flush=True)
    print("*** Resultat :", resultat, file=sys.stderr, flush=True)

    test = testError(resultat)
    print("*** test :", test, file=sys.stderr, flush=True)
        # test = False


    # dataResult.append(equation)
    # test = result.split('=')
    if test:
        dataResult.append(equation)
    else :
        dataResult.append("Error : " + equation)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for result in dataResult:
    print(result)
