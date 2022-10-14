import random
from time import time
import math

## Function to convert decimal to binary
def decToBin(num):
    if num < 0:
        num = num * -1

    tempDigit = 0
    bin = ''
    while num > 0:
        tempDigit = num % 2
        bin += str(tempDigit)
        num = num // 2
    bin = bin[::-1]
    return bin

## Function to convert floating point number to binary float notation
def floatToBin(num, form):
    ## Checks for initial bit
    if num < 0:
        sign = "1"
    elif num > 0:
        sign = "0"
        
    if num < 0:
        num = num * -1
    # Define necessary variables
    binFloat = ''
    exp = ''
    mant = ''
    sCand = ''
    binStr = ''

    num = str(num)
    whole, dec = num.split(".")
    num = float(num)
    whole = int(whole)
    dec = int(dec)

    tempDigit = 0

    while whole > 0:
        tempDigit = whole % 2
        binStr += str(tempDigit)
        whole = whole // 2
    binStr = binStr[::-1]
    binStr += "."

## Handles digits following decimal and rounds off numbers that cannot be represented
    while dec >= 0:
        dec = dec * 10**-len(str(dec))
        dec = dec * 2
        dec = str(dec)
        dig, dec = dec.split(".")
        binStr += str(dig)
        dec = int(dec)
        if form == "binary32":
            if len(binStr) >= 32:
                break
        if form == "binary64":
            if len(binStr) >= 64:
                break
        if form == "binary128":
            if len(binStr) >= 128:
                break

    print("binStr: ", binStr)
    ## Retrieve Exponent in excess form
    for i in range(0, len(binStr)):
        if binStr[1] == '.':
            mant = "1"
            break
        if binStr[i] == '.':
            break
        mant += binStr[i]
    print("Value of mant: ", mant)
    expDec = 0
    expLength = 0

    if len(mant) == 1 or binStr[0] == ".":
        expLength = binStr.find('.') - binStr.find('1')


    if binStr[0] == ".":
        for i in mant:
            expLength -= 1
            if i == "1":
                break

    else:
        expLength = len(mant) - 1


    print("expLength: ", expLength)
    if form == "binary32":
        expDec = expLength  + 127
    elif form == "binary64":
        expDec = expLength + 1023
    elif form == "binary128":
        expDec = expLength + 16383

    print("expDec val: ", expDec)

    binTemp = 0
    binTemp = str(num)
    exp = str(decToBin(expDec))



    if form == "binary32":
        if expDec <= 127:
            exp = "0" + exp
    elif form == "binary64":
        if expDec <= 1023:
            exp = "0" + exp
    elif form == "binary128":
        if expDec <= 16383:
            exp = "0" + exp
    
## Retrieve Significand
    for i in range(1, len(binStr)):
        if binStr[i] == '.':
            continue
        sCand += binStr[i]
       
    ## Combine terms to form standard format and handle special cases
    if expLength < 0:
        sCand = binStr[binStr.find('1')+1:]

    binFloat = sign + exp + sCand

    print("Value of exp: ", exp)
    print("Value of sCand: ", sCand)

    if form == "binary32":
        while len(binFloat) < 32:
            binFloat += "0"
        while len(binFloat) > 32:
            binFloat = binFloat[:-1]
    elif form == "binary64":
        while len(binFloat) < 64:
            binFloat += "0"
        while len(binFloat) > 64:
            binFloat = binFloat[:-1]
    elif form == "binary128":
        while len(binFloat) < 128:
            binFloat += "0"
        while len(binFloat) > 128:
            binFloat = binFloat[:-1]

    return binFloat


## Main Driver function
def main():
   floatDec = 0.25
   form = "binary32"
   print(floatToBin(floatDec, form))

main()
