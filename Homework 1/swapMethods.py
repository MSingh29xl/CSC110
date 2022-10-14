import random
from time import time

## Temporary variable swap
def swapByTemp(a, b):
    print("X is : ", int(a))
    print("Y is : ", int(b))
    temp = a
    a = b
    b = temp
    print("X is : ", int(a))
    print("Y is : ", int(b))

##Bitwise swap
def swapByXOR(a, b):
    print("X is : ", int(a))
    print("Y is : ", int(b))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("X is : ", int(a))
    print("Y is : ", int(b))

## Add/Sub swap
def swapByAddSub(a, b):
    print("X is : ", int(a))
    print("Y is : ", int(b))
    a = a + b
    b = a - b
    a = a - b
    print("X is : ", int(a))
    print("Y is : ", int(b))
    
## Mult/Div swap
def swapByMultDiv(a, b):
    print("X is : ", int(a))
    print("Y is : ", int(b))
    a = a * b
    b = a / b
    a = a / b
    print("X is : ", int(a))
    print("Y is : ", int(b))

## Function to conduct one time average given an output list and swap function
def takeOneTime(listEx, func):
    ## Generates Random Numbers
    y = random.randrange(1, 10000)
    x = random.randrange(1, 10000) +y
    ## Calculates before and after times, uses swap method, and computes the time
    beforeTime = int(time() * 1000000)
    func(x, y)
    afterTime = int(time() * 1000000)
    oneAvg = afterTime - beforeTime
    ## Time taken is stored to list
    listEx.append(oneAvg)
    return listEx

## Function that takes lists from takeOneTime and computes averages for each method
def takeAvgTime(outList):
    avgTime = 0
    for i in outList:
        avgTime += i
    avgTime = avgTime / 10000
    return avgTime

## Main Driver Function
def main():
## Initializes necessary variables
    counter = 0
    tempList = []
    XORList = []
    AddSubList = []
    MultDivList = []
    avgTemp = 0
    avgXOR = 0
    avgAddSub = 0
    avgMultDiv = 0
    ## Loop for conducting swap and instantial times
    while counter <= 10000:
        takeOneTime(tempList, swapByTemp)
        takeOneTime(XORList, swapByXOR)
        takeOneTime(AddSubList, swapByAddSub)
        takeOneTime(MultDivList, swapByMultDiv)
        counter += 1
       ## Computes averages and prints them out
    avgTemp = takeAvgTime(tempList)
    avgXOR = takeAvgTime(XORList)
    avgAddSub = takeAvgTime(AddSubList)
    avgMultDiv = takeAvgTime(MultDivList)
    print("Average time for Temp: ", avgTemp, "us")
    print("Average time for XOR: ", avgXOR, "us")
    print("Average time for AddSub: ", avgAddSub, "us")
    print("Average time for MultDiv: ", avgMultDiv, "us")

main()
