# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PlaceTheParenthesis.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/25 08:19:29 by pwolff            #+#    #+#              #
#    Updated: 2024/11/01 10:43:20 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

equ = []
calcul = ""
dataResult = []
listSolution = []

# travail = equation.split("=")[0] + "$"
# print("equation : ", equation)
# print("travail : ", travail)

dataEquations = []
dataResultats = []



n = int(input())
for i in range(n):
    equation = input()
    print(i, "Equ :", equation, file=sys.stderr, flush=True)
    equ.append(equation)

print("Equ :", equ[:], file=sys.stderr, flush=True)





def clean(firstPart):
    while True:
        if firstPart[-1:].isnumeric():
            firstPart = firstPart[:len(firstPart) - 1]
        else:
            break
    return firstPart


def testInt(string, sens):
    value = 0
    if sens == 1:
        for i in string:
            if i.isnumeric() or (i == '-' and value == 0):
                value += 1
            else:
                break
    else:
        for i in reversed(string):
            if i.isnumeric():
                value -= 1
                if value == -(len(string) - 1):
                    value -= 1
            else:
                break
    return value



def splitSous(calcul):
    split = []
    i = 1
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


def multiplication(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    b = int(multi[1][:testInt(multi[1], 1)])
    # print("A = ", a, file=sys.stderr, flush=True)
    # print("B = ", b, file=sys.stderr, flush=True)
    c = a * b
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]

    firstPart = clean(firstPart)
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    # print("newString = ", newString, file=sys.stderr, flush=True)
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
    # print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)

def addition(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    if len(multi[0]) - len(str(a)) == 1:
        a = -a
    b = int(multi[1][:testInt(multi[1], 1)])
    # print("A = ", a, file=sys.stderr, flush=True)
    # print("B = ", b, file=sys.stderr, flush=True)
    c = (a + b)
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    firstPart = clean(firstPart)
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    # print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)

def soustraction(multi, calcul):
    newString = ""
    a = int(multi[0][testInt(multi[0], 0):])
    if len(multi[0]) - len(str(a)) == 1:
        a = -a
    b = int(multi[1][:testInt(multi[1], 1)])
    # print("A = ", a, file=sys.stderr, flush=True)
    # print("B = ", b, file=sys.stderr, flush=True)
    c = (a - b)
    firstPart = multi[0][:len(multi[0])-(len(str(a)))]
    firstPart = clean(firstPart)
    newString = firstPart + str(c) + multi[1][len(str(b)):]
    # print("newString = ", newString, file=sys.stderr, flush=True)
    return (newString)




def CalculDivision(calcul):
    div = calcul.split('/')
    # print("Divisions : ", div, file=sys.stderr, flush=True)
    while True:
        if len(div) > 2:
            temp = div[1] + "/" + div[2]
            div[1] = temp
            del div[2]
        else:
            break
    if len(div) == 1:
        return calcul
    calcul = division(div, calcul)
    return calcul

def CalculMultiplication(calcul):
    multi = calcul.split('*')
    # print("Multiplications : ", multi, file=sys.stderr, flush=True)
    while True:
        if len(multi) > 2:
            temp = multi[1] + "*" + multi[2]
            multi[1] = temp
            del multi[2]
        else:
            break
    if len(multi) == 1:
        return calcul
    calcul = multiplication(multi, calcul)
    return calcul




def CalculSoustraction(calcul):
    # soustract = calcul.split('-')
    # soustract = []
    soustract = splitSous(calcul)
    # print("Soustraction : ", soustract, file=sys.stderr, flush=True)
    while True:
        if len(soustract) > 2:
            temp = soustract[1] + "-" + soustract[2]
            soustract[1] = temp
            del soustract[2]
        else:
            break
    if len(soustract) == 1:
        return calcul
    # print("Soustraction : ", soustract, file=sys.stderr, flush=True)
    calcul = soustraction(soustract, calcul)
    return calcul


def CalculAddition(calcul):
    add = calcul.split('+')
    # print("Additions : ", add, file=sys.stderr, flush=True)
    while True:
        if len(add) > 2:
            temp = add[1] + "+" + add[2]
            add[1] = temp
            del add[2]
        else:
            break
    if len(add) == 1:
        return calcul
    calcul = addition(add, calcul)
    return calcul



def blok(calcul):
    value = 0
    # travail = calcul


    while True:
        if '/' in calcul and '*' in calcul:
            if calcul.index('/') < calcul.index('*'):
                calcul = CalculDivision(calcul)
            else:
                calcul = CalculMultiplication(calcul)
        elif '/' in calcul:
            calcul = CalculDivision(calcul)
        elif '*' in calcul:
            calcul = CalculMultiplication(calcul)
        else:
            break

    while True:
        test = 0
        print("Boucle +/- : ", calcul, file=sys.stderr, flush=True)
        if calcul[0] == "-":
            calcul = calcul[1:]
            test = 1

        if '-' in calcul and '+' in calcul:
            if calcul.index('-') < calcul.index('+'):
                if test:
                    calcul = "-" + calcul
                    test = 0
                calcul = CalculSoustraction(calcul)
            else:
                if test:
                    calcul = "-" + calcul
                    test = 0
                calcul = CalculAddition(calcul)
        elif '+' in calcul:
            if test:
                calcul = "-" + calcul
                test = 0
            calcul = CalculAddition(calcul)

        elif '-' in calcul.split('=')[0]:
            if test:
                calcul = "-" + calcul
                test = 0
            calcul = CalculSoustraction(calcul)                
        else:
            if test :
                calcul = "-" + calcul
            break
    

    return calcul




def testError(result):
    test = result.split('=')
    if int(test[0]) == int(test[1]):
        return True
    return False









def testInterParent(equation):
    parenthese = equation.split('(')
    test = False
    for i in range(parenthese[1].index(")")):
        if not parenthese[1][i].isnumeric():
            test = True


    return test



def testAllEquations(equation):

    dataEquations.append(equation)
    travail = equation.split("=")[0] + "$"
    # print("equation : ", equation)
    # print("travail : ", travail)
    for i in range(len(travail)):

        if i == 0 or travail[i].isnumeric() and not travail[i - 1].isnumeric():
            temp = travail[:i] + "(" + travail[i:]
            # print("temp : ", temp)

            j = i
            
            while j < (len(temp) - 1):
                if j == len(temp) - 2 or temp[j].isnumeric() and not temp[j+1].isnumeric():
                    temp2 = temp[:j + 1] + ")" + temp[j + 1:]
                    test = testInterParent(temp2)
                    if test :
                        # print("     temp2 : ", temp2)
                        if not (temp2.index('(') == 0 and temp2.index(')') == len(temp2) - 2):
                            # print("No test", equation, file=sys.stderr, flush=True)

                            dataEquations.append(temp2[:-1] + "=" + equation.split("=")[1])
                j += 1
        i += 1
    print("dataEquations", dataEquations, file=sys.stderr, flush=True)
    return dataEquations


    # ********************** Verifier les differentes combinaisons

for equation in equ:
    print("***  equation : ", equation, file=sys.stderr, flush=True)
    dataEquations = []
    dataEquations = testAllEquations(equation)

    for equa in dataEquations:
        print(equa, file=sys.stderr, flush=True)
        test = equa.find('(')
        print("***  Travail equa : ", equa, file=sys.stderr, flush=True)
        if test == -1:
            resultat = blok(equa)
            test = testError(resultat)
            if test:
                listSolution.append(equa)
                break
                continue
            else:
                continue
        premiereParent = equa.find('(')
        deuxiemeParent = equa.find(')')
        chaine1 = equa[:premiereParent]
        chaine2 = equa[premiereParent + 1:deuxiemeParent]
        chaine3 = equa[deuxiemeParent + 1:]
        print("**** chaines ****", file=sys.stderr, flush=True)
        print(chaine1, file=sys.stderr, flush=True)
        print(chaine2, file=sys.stderr, flush=True)
        print(chaine3, file=sys.stderr, flush=True)
        if len(chaine1) == 1:
            chaine2 = chaine1 + chaine2
            chaine1 = ""
        result = blok(chaine2+"=0")
        newEqua = chaine1 + result.split('=')[0] + chaine3
        print("**** NewChaine : ", newEqua, file=sys.stderr, flush=True)
        result = blok(newEqua)
        testEqua = testError(result)
        if testEqua:
            listSolution.append(equa)
            break        




print("**** Solution ****** : ", file=sys.stderr, flush=True)
for solution in listSolution:
    print(solution)









# ***************************************************
# ***************************************************
# ***************************************************



for i in range(int(input())):
    equation = input()
    eq, va = equation.split('=')
    if eval(eq) != int(va):
        for j in range(len(eq)):
            for k in range(j + 1, len(eq) + 1):
                line = eq[:j] + "(" + eq[j:k] + ")" + eq[k:]
                try:
                    if eval(line) == int(va):
                        equation = line + "=" + va
                        break
                except:
                    continue
    print(equation)