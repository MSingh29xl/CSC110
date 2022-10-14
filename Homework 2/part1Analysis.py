import random
import time
import math

def decToBin(num, stat):

    if num < 0:
        num = num * -1

    tempDigit = 0
    binary = ''
    while num > 0:
        tempDigit = num % 2
        binary += str(tempDigit)
        num = num // 2
    binary = binary[::-1]
    if stat == "booth":
        if num < 0:
            twosTemp = binary
        binary = ""
        for i in twosTemp:
            if i == "0":
                binary = binary + "1"

            elif i == "1":
                binary = binary + "0"

        binary = binAdd(binary, "1", "two")

    return binary

## Function to add binary numbers
def binAdd(a, b, stat):
    carry = 0
    sum = []
    sumFinal = ""

## Make sure length of the terms are equivalent
    max_len = max(len(a),len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    i = 0
## Reverse iteration and condition handling
    while i > - (len(a)):
        i -= 1
        if int(a[i]) + int(b[i]) + carry == 0:
            sum.insert(0, 0)
            carry = 0
        elif int(a[i]) + int(b[i]) + carry == 1:
            sum.insert(0, 1)
            carry = 0
        elif int(a[i]) + int(b[i]) + carry == 2:
            sum.insert(0, 0)
            carry = 1
        elif int(a[i]) + int(b[i]) + carry == 3:
            sum.insert(0, 1)
            carry = 1

## Carry handler
    if carry == 1 and stat != "two":
        sum.insert(0,"1")
    for j in sum:
        sumFinal += str(j)

## Append signed bit for two's complement
    if stat == "two":
        sumFinal = "1" + sumFinal
    return sumFinal


## Function to multiply binary numbers
def standMult(mcand, mplier, ocand, oplier):
    twosTemp = ""
    products = []
    multSum = "0"
    M = str(mcand)
    Q = str(mplier)


    if (ocand != 0) and (oplier != 0):
        for i in reversed(Q):
            if i == "1":
                products.append(M)
            elif i == "0":
                products.append("0")
            M = M + "0"

    for i in products:
        multSum = binAdd(multSum, i, "one")

## Checks for opposite signs and performs two's complement
    if (ocand < 0 and oplier > 0) or (ocand > 0 and oplier < 0):
        twosTemp = multSum
        multSum = ""
        for i in twosTemp:
            if i == "0":
                multSum = multSum + "1"

            elif i == "1":
                multSum = multSum + "0"

        multSum = binAdd(multSum, "1", "two")



    decSum = ocand * oplier
    multTuple = (decSum, multSum)
    return multTuple

## Main driver function
def main():
    standTimes = 0
    boothTimes = 0
    standFinalAvg = 0
    boothFinalAvg = 0
    beforeStand = 0
    afterStand = 0
    standOneAvg = 0
    boothOneAvg = 0
    beforeBooth = 0
    afterBooth = 0
    for i in range(10001):
        x = random.randint(-10000, 10000)
        y = random.randint(-10000, 10000)
        standCand = decToBin(x, "no")
        standPlier = decToBin(y, "no")
        boothCand = decToBin(x, "booth")
        boothPlier = decToBin(y, "booth")
        beforeStand = time.time()
        standMult(cand, plier, x, y)
        afterStand = time.time()
        standOneAvg = afterStand - beforeStand
        standTimes += standOneAvg

    standFinalAvg = standTimes / 10000
    ##boothFinalAvg = boothTimes / 10000
    print(standFinalAvg)
    ##print(boothFinalAvg)
    return

main()
    
