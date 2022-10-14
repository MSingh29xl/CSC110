import random
import time


## Function for Arithmetic right shift
def ARS(num):
    after = ""
    if num[0] == "0":
        after = "".join(["0"]) 
    else:
        after = "".join(["1"]) 
    return after[:len(num)]


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

## Function to convert multiplicand and multiplier to decimal
def decToBin(num, stat):
    twosTemp = "0"

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

## Function to execute the Booth multiplication method
def boothMult(mcand, mplier, ocand, oplier):
    ## Set necessary variables
    A = "0"
    Qnot = "0"
    M = str(mcand)
    Q = str(mplier)
    n = len(mcand)
    tempReg = ""
    binTemp = 0

    ## Condition handling
    while n > 0:
        tempReg = Q[-1] + Qnot
        if tempReg == "00" or tempReg == "11":
            Q = ARS(Q)
        elif tempReg == "10":
            binTemp = bin(int(A,2) - int(M,2))
            binTemp = str(binTemp)
            A = binTemp[2:]
            Q = ARS(Q)
        elif tempReg == "01":
            A = binAdd(A, M, "no")
            Q = ARS(Q)
            A = ARS(A)
        n -= 1

## Main driver function
def main():
    time = 0
    cand = random.randint(-4294967297, 4294967295)
    plier = random.randint(-4294967297, 4294967295)
    candBin = decToBin(cand, "booth")
    plierBin = decToBin(plier, "booth")
    start = time.time()
    boothMult(candBin, plierBin, cand, plier)
    end = time.time()
    time = end - start

main()

