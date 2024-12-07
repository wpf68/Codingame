# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Pertes en bourse.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/07 17:49:38 by pwolff            #+#    #+#              #
#    Updated: 2024/12/07 17:57:28 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


value = []
perte = 0
n = int(input())
# print("n : ", n, file=sys.stderr, flush=True)
for i in input().split():
    v = int(i)
    value.append(v)

print("value :", value, file=sys.stderr, flush=True)
# print("floor :", min(value), file=sys.stderr, flush=True)




# ******************  Method 1 ***************
# begin =0
# while begin < len(value):
#     # print(begin, " : ", value[begin], file=sys.stderr, flush=True)
#     end = begin + 1
#     while end < len(value):
#         temp = value[end] - value[begin] 
#         if temp < perte:
#             perte = temp
#         end += 1
#     begin += 1



# # ******************  Method 2 ***************
# for begin in range (0, n):
#     for end in range (begin + 1, n):
#         temp = value[end] - value[begin] 
#         if temp < perte:
#             perte = temp



# # ******************  Method 3 ***************
# for begin in range (0, n):
#     temp = min(value[begin:]) - value[begin] 
#     if temp < perte:
#         perte = temp


# ******************  Method 3 ***************
# maximum = value[0] - 1
# for begin in range (0, n):
#     if value[begin] > maximum:
#         temp = min(value[begin:]) - value[begin] 
#         if temp < perte:
#             perte = temp
#         maximum = begin
#     # else:
#     #     continue

# ******************  Method 4 ***************
maximum = value[0]
maximum2 = maximum
for begin in range (1, n):
    if value[begin] > maximum and value[begin] > maximum2:
        maximum = maximum2
        maximum2 = value[begin]
        # print("\nMax :", maximum2, "Max2", maximum2, file=sys.stderr, flush=True)
        # print("value :", value[begin], file=sys.stderr, flush=True)
        # print("perte :", perte, file=sys.stderr, flush=True)
        continue
    if value[begin] - maximum < perte:
        perte = value[begin] - maximum
    if value[begin] - maximum2 < perte:
        perte = value[begin] - maximum2
        maximum = maximum2
    


    # print("\nMax :", maximum2, "Max2", maximum2, file=sys.stderr, flush=True)
    # print("value :", value[begin], file=sys.stderr, flush=True)
    # print("perte :", perte, file=sys.stderr, flush=True)

    




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(perte)




# **************************************************************************

stocks=[]
drop=0
max=0
n=int(input())
for i in input().split():
    v=int(i)
    stocks.append(v)
for s in stocks:
    if s>max:max=s
    else:
        if max-s>drop:drop=max-s
if drop<=0:drop=0
print(drop * -1)


# **************************************************************************


n = int(input())
maxV = -1
maxL = 0
for i in input().split():
    v = int(i)
    maxV = v if v > maxV else maxV
    maxL = v-maxV if v-maxV<maxL else maxL
print(maxL)


# **************************************************************************

n = int(input())
prices = map(int, input().split())

loss = 0
high = next(prices)

for p in prices:
    high = max(high, p)
    loss = min(loss, p - high)

print(loss)
