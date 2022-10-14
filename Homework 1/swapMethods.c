#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Temporary variable swap
void swapByTemp(int a, int b) {

    printf("x= %d \n", a);
    printf("y= %d \n", b);
    int temp = a;
    a = b;
    b = temp;
    printf("x= %d \n", a);
    printf("y= %d \n", b);
}

// Bitwise swap
void swapByXOR(int a, int b) {
    printf("x= %d \n", a);
    printf("y= %d \n", b);
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    printf("x= %d \n", a);
    printf("y= %d \n", b);
}

// Add/Sub swap
void swapByAddSub(int a, int b) {
    printf("x= %d \n", a);
    printf("y= %d \n", b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("x= %d \n", a);
    printf("y= %d \n", b);
}

// Mult/Div swap
void swapByMultDiv(long a, long b) {
    printf("y= %ld \n", b);
    a = a * b;
    b = a / b;
    a = a / b;
    printf("x= %ld \n", a);
    printf("y= %ld \n", b);
}

// Function that calculates average time given a timing list
void takeAvgTime(long lst[10000]) {
        double avgTime = 0;
        for (int i = 0; i < 10000; i++){
            avgTime += lst[i];
            }
        avgTime = avgTime / 10000;
        printf("%f \n", avgTime);
}

// Main driver function for swapping and time computing
int main() {
	// Initializes necessary variables and arrays
    int counter;
    long beforeTime = 0;
    long afterTime = 0;
    long oneAvg;
    long tempList[10000];
    long XORList[10000];
    long AddSubList[10000];
    long MultDivList[10000];
    clock_t t;
	// Loop for performing swaps and storing timings within respective lists
    for (counter = 0; counter < 10000; counter++) {
		// Sets random numbers to variables
        int y = (rand() % (100000 - 1 + 1)) + 1;
        int x = (rand() % (100000 - 1 + 1)) + 1 + y;
		// Takes time taken by swap method in one instance and sends to array 
        beforeTime = clock();
        swapByTemp(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        tempList[counter] = oneAvg;
        beforeTime = clock();
        swapByXOR(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        XORList[counter] = oneAvg;
        beforeTime = clock();
        swapByAddSub(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        AddSubList[counter] = oneAvg;
        beforeTime = clock();
        swapByMultDiv(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        MultDivList[counter] = oneAvg;
    }
	// Calculates average time from list and prints it out
    takeAvgTime(tempList);
    takeAvgTime(XORList);
    takeAvgTime(AddSubList);
    takeAvgTime(MultDivList);
    return 0;
}

