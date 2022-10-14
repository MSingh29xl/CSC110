#include <iostream>
#include <math.h>
using namespace std;

// Function used to convert base number b to decimal
void baseConversion() {

    // Initializes necessary variables and arrays
    int b;
	int n = 0;
	int sum = 0;
	/* 10 is assigned to MaxNumDigits as the highest value handled in an int is 2147483647,
	 a 10 digit number*/
	const int MaxNumDigits = 10;
    char num[MaxNumDigits];

    // Takes values for base and number from user
	cout << "Type the base of the number here: ";
    cin >> b;
    cout << "Type your non-negative number here (from 0 - 2147483647): ";
    cin >> num;
	cout << "Your base is "<<b<<" and your number is "<<num<<endl;

	// Get the proper length of the number and set value of n
	for (int i=0; i <MaxNumDigits; i++) {
		if (num[i] == 0) { // Checks for empty value in char array
			break;
		}
		else {
			n += 1;
		}
	}

	// Traverse num digit array and convert num in base b to decimal
	for (int i=0; i <MaxNumDigits; i++) {
		int temp = 0;
		n -= 1;

		if (num[i] == 0) { // Checks for empty value in char array
			break;
			}

		// Handles values for numbers from base 11 - 36
		if (b <= 10) {
			sum += ((int)num[i]-48) * pow(b, n);
		}

		if ((num[i] == 'a' or num[i] == 'A') && b >= 11) {
			temp = 10;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'b' or num[i] == 'B') && b >= 12) {
			temp = 11;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'c' or num[i] == 'C') && b >= 13) {
			temp = 12;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'd' or num[i] == 'D') && b >= 14) {
			temp = 13;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'e' or num[i] == 'E') && b >= 15) {
			temp = 14;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'f' or num[i] == 'F') && b >= 16){
			temp = 15;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'g' or num[i] == 'G') && b >= 17) {
			temp = 16;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'h' or num[i] == 'H') && b >= 18){
			temp = 17;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'i' or num[i] == 'I') && b >= 19) {
			temp = 18;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'j' or num[i] == 'J') && b >= 20) {
			temp = 19;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'k' or num[i] == 'K') && b >= 21) {
			temp = 20;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'l' or num[i] == 'L') && b >= 22) {
			temp = 21;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'm' or num[i] == 'M') && b >= 23) {
			temp = 22;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'n' or num[i] == 'N') && b >= 24) {
			temp = 23;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'o' or num[i] == 'O') && b >= 25) {
			temp = 24;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'p' or num[i] == 'P') && b >= 26) {
			temp = 25;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'q' or num[i] == 'Q') && b >= 27) {
			temp = 26;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'r' or num[i] == 'R') && b >= 28) {
			temp = 27;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 's' or num[i] == 'S') && b >= 29) {
			temp = 28;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 't' or num[i] == 'T') && b >= 30) {
			temp = 29;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'u' or num[i] == 'U') && b >= 31) {
			temp = 30;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'v' or num[i] == 'V') && b >= 32) {
			temp = 31;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'w' or num[i] == 'W') && b >= 33) {
			temp = 32;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'x' or num[i] == 'X') && b >= 34) {
			temp = 33;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'y' or num[i] == 'Y') && b >= 35) {
			temp = 34;
			sum += temp * pow(b, n);
		}
		else if ((num[i] == 'z' or num[i] == 'Z') && b >= 36) {
			temp = 35;
			sum += temp * pow(b, n);
		}
	}
	cout << "Your number in decimal base is: "<<sum<<endl;
}

// Main Driver Function
int main() {
    baseConversion();
    return 0;
}

