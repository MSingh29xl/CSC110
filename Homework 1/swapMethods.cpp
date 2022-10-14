#include <iostream>
#include <time.h>
#include <list>
#include <iterator>
using namespace std;

// Temporary Variable swap
void swapByTemp(int a, int b) {

    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
    int temp = a;
    a = b;
    b = temp;
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
}

// Bitwise swap
void swapByXOR(int a, int b) {
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
}

// Add/Sub swap
void swapByAddSub(int a, int b) {
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
    a = a + b;
    b = a - b;
    a = a - b;
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
}
// Mult/Div swap
void swapByMultDiv(long a, long b) {
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
    a = a * b;
    b = a / b;
    a = a / b;
    cout<<"x= "<<a<<endl;
    cout<<"y= "<<b<<endl;
}

// Function to compute average time for each run
void takeAvgTime(list < double > lst) {
        list<double>:: iterator i;
        double avgTime = 0;
        for (auto i = lst.begin(); i != lst.end(); i++){
            avgTime += *i;
            }
        avgTime = avgTime / 10000;
        cout<<avgTime<<endl;
    }

int main() {
	// Initializes necessary variables and lists for input
    int counter;
    list< double > tempList;
    list< double > XORList;
    list< double > AddSubList;
    list< double > MultDivList;
    long beforeTime = 0;
    long afterTime = 0;
    long oneAvg;
    clock_t t;
	// Loop to conduct swap and timing calculation
    for (counter = 0; counter < 10000; counter++) {
        int y = (rand() % (10000 - 1 + 1)) + 1;
        int x = (rand() % (10000 - 1 + 1)) + 1 + y;
        beforeTime = clock();
        swapByTemp(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        tempList.push_back(oneAvg);
        beforeTime = clock();
        swapByXOR(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        XORList.push_back(oneAvg);
        beforeTime = clock();
        swapByAddSub(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        AddSubList.push_back(oneAvg);
        beforeTime = clock();
        swapByMultDiv(x, y);
        afterTime = clock();
        oneAvg = afterTime - beforeTime;
        MultDivList.push_back(oneAvg);
    }
	// Computes averages from the lists made in the loop
    takeAvgTime(tempList);
    takeAvgTime(XORList);
    takeAvgTime(AddSubList);
    takeAvgTime(MultDivList);
    return 0;
}
