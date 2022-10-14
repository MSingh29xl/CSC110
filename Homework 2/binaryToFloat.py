import random
from time import time
import math


## Function to convert binary integer to decimal
def binToDec(bin):
    decPart = 0
    i = 0
    n = 0
    dec = 0
    while bin != 0:
        decPart = bin % 10
        dec += decPart * 2**i
        bin = bin // 10
        i += 1
    return dec

## Function to convert binary float to decimal floating number
def binToFloat(binary, form):
    ## Define necessary variables
    binFloat = ''
    exp = ''
    expDec = 0
    mant = ''
    sCand = ''
    bin = ''
    sign = ""
    decimalNum = ""
    binTemp = ""
    decFinal = 0
    floatDec = ""
    
    ## Sets sign based on sign bit
    if binary[0] == "1":
        sign = "-"

    ## Retrieve exponent and mantissa

    if form == "binary32":
        exp = str(binary[1:9])
        expDec = binToDec(int(exp))
        expDec -= 127
        sCand = binary[9:]

    elif form == "binary64":
        exp = str(binary[1:12])
        expDec = binToDec(int(exp))
        expDec -= 1023
        sCand = binary[12:]
            
    elif form == "binary128":
        exp += str(binary[1:16])
        expDec = binToDec(int(exp))
        expDec -= 16383
        sCand = binary[16:]

    ## Find binary format of integer and decimal numbers
    for i in range(expDec, len(sCand)): 
        decimalNum += sCand[i]

        
    for i in range(expDec):
        mant += sCand[i]
        
    ## One is (almost) always included
    if expDec >= 0:
        mant = "1" + mant
    else:
        mant = "0"

    print(decimalNum)

    binTemp =  mant + "." + decimalNum
    
    ## Convert binary floating number to decimal
    mant = binToDec(int(mant))
    
    j = 1
    for i in decimalNum:
        decFinal += int(i) * 2**-j
        j += 1

    if expDec < 0:
        decFinal += 2**expDec

    decFinal = str(decFinal)
    
    ## Assemble the final number
    floatDec = sign + str(mant) + str(decFinal[1:])
    
    return(floatDec)
    
    
## Main Driver function
def main():
    binFloat = "00111111000000000000000000000000"
    form = "binary32"
    print(binToFloat(binFloat, form))


main()
