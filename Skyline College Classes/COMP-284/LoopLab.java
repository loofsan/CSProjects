// Author: Lynn T. Aung
// Date: June 28, 2023
// Lab 7, Loop Lab
/* 
   This lab will loop to ask a user for scores and returns
   the biggest score, smallest score and average score and
   number of scores entered.
*/

import java.util.Scanner;
public class LoopLab
{
    public void calculateTestScores() 
    {
        int answer;
        int sumOfScores = 0;
        int numOfScores = 0;
        int largestNum = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("(Type negative numbers to quit)\n"
         + "Please type in a number: ");
        answer = input.nextInt();
        
        while (answer > 100) 
        { // Makes sure the score is not above 100.
            System.out.println("***** Please put a score under or equal to 100. *****");
            System.out.println("(Type negative numbers to quit)\n"
             + "Please type in a number: ");
            answer = input.nextInt();
        }
        
        
        int smallestNum = answer; // Take in the first number as the smallest number.
        
        while (answer >= 0 && answer <= 100)
        {          
            numOfScores ++; // Adds to the counter 'numOfScores'
            sumOfScores += answer; // Adds to the total score
            if (answer < smallestNum) 
            {// If the answer is smaller, it will be the new smallest number.
                smallestNum = answer; 
            }
            if (answer > largestNum)
            {// If the answer is bigger, it will be the new biggest number.
                largestNum = answer;
            }
            
            System.out.println("(Type negative numbers to quit)\n"
             + "Please type in a number: ");
            answer = input.nextInt(); // Loop the question.
            
            if (answer > 100) 
            { // Makes sure the score is not above 100;
                System.out.println("***** Please put a score under or equal to 100. *****");
                System.out.println("(Type negative numbers to quit)\n"
                 + "Please type in a number: ");
                answer = input.nextInt();
            }
            
        }
        
        // The code below finds average and print the numbers
        double arithmeticAverage = (double) sumOfScores/numOfScores;
        
        System.out.println("Over " + numOfScores + " numbers"
          + " entered,");
        System.out.println("This is the largest number: "
          + largestNum + ".");
        System.out.println("This is the smallest number: "
          + smallestNum + ".");
        System.out.println("This is the average: "
          + arithmeticAverage + ".");
    }
}