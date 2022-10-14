import java.io.*;
import java.util.Random;
import java.lang.reflect.Method;

public class swapMethods {

// Temporary Variable swap
    static void swapByTemp(int a, int b) {
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
    }

// Bitwise swap
    static void swapByXOR(int a, int b) {
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
    }

// Add/Sub swap
    static void swapByAddSub(int a, int b) {
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
    }

// Mult/Div swap
    static void swapByMultDiv(int a, int b) {
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
        a = a * b;
        b = a / b;
        a = a / b;
        System.out.println("x = "+ a);
        System.out.println("y = "+ b);
    }
// Function for calculating averages
    static void takeAvgTime(long[] list) {
        float avgTime = 0;
        for(int i = 0; i < list.length; i++){
            avgTime += list[i];
            }
        avgTime = avgTime / 10000;
        System.out.println(avgTime);
    }

// Main Driver Function
    public static void main(String a[]) {
        Random rand = new Random();
		// Sets necessary variables and lists for functiions
        int counter = 0;
        long[] tempList = new long[10000];
        long[] XORList = new long[10000];
        long[] AddSubList = new long[10000];
        long[] MultDivList = new long[10000];
        long beforeTime = 0;
        long afterTime = 0;
        long oneAvg;
		// Loop for conducting the swapping process
        while (counter < 10000) {
			// Sets random numbers
            int y = rand.nextInt(1, 10000);
            int x = rand.nextInt(1, 10000) + y;
			// Sets time before and after the running of each method and stores time difference to the given list
            beforeTime = (System.currentTimeMillis() * 1000);
            swapByTemp(x, y);
            afterTime = (System.currentTimeMillis() * 1000);
            oneAvg = afterTime - beforeTime;
            tempList[counter] = oneAvg;
            beforeTime = (System.currentTimeMillis() * 1000);
            swapByXOR(x, y);
            afterTime = (System.currentTimeMillis() * 1000);
            oneAvg = afterTime - beforeTime;
            XORList[counter] = oneAvg;
            beforeTime = (System.currentTimeMillis() * 1000);
            swapByAddSub(x, y);
            afterTime = (System.currentTimeMillis() * 1000);
            oneAvg = afterTime - beforeTime;
            AddSubList[counter] = oneAvg;
            beforeTime = (System.currentTimeMillis() * 1000);
            swapByMultDiv(x, y);
            afterTime = (System.currentTimeMillis() * 1000);
            oneAvg = afterTime - beforeTime;
            MultDivList[counter] = oneAvg;
            counter++;
            }
		// Uses list to compute averages and displays them
        takeAvgTime(tempList);
        takeAvgTime(XORList);
        takeAvgTime(AddSubList);
        takeAvgTime(MultDivList);
    }
}
