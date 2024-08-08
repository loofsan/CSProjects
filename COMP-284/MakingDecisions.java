// Lynn T. Aung
// June 26, 2023
// Lab 5, Making Decisions
// This lab will return change to the user from their input.

import java.util.Scanner;
public class MakingDecisions 
{
    public static void main (String [] args) 
    {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter the price of the item " 
          + "(Whole numbers of 30 to 100 in increments of 5): ");
        int price = input.nextInt();
        int change = 100 - price; // Find change
        
        // Check to see if the number inputted is valid
        boolean isValid = true;  // Make a flag
        if (price < 30)
        {
            System.out.println("Invalid input. Please put a number " 
             + "higher than or equal to 30.");
             isValid = false;
        }
        else if (price > 100) 
        {    
            System.out.println("Invalid input. Please put a number "
             + "lower than or equal to 100."); 
            isValid = false;
        }
        else if (price % 5 != 0)
        {
            System.out.println("Invalid input. Please put a number in " 
             + "increments of 5.");
            isValid = false;
        }
        
        /* 
        Got the code below from the textbook (Java: An Introduction To Problem 
        Solving and Programming by Walter Savitch; Kenrick Mock p. 125)
        */
        // Finding out the change
        int quarters = change / 25;
        change = change % 25;
        int dimes = change / 10;
        change = change % 10;
        int nickels = change / 5;
        change = change % 5;
        int pennies = change;
        
        // Use the flag so that this statement below
        // only prints if the value is valid
        if (isValid) 
        {
            System.out.println("You bought an item for " + price 
             + " and gave me a dollar, \nso your change is \n");
             
            System.out.println(quarters + " quarters, \n"
             + dimes + " dimes, \n"
             + nickels + " nickels and\n"
             + pennies + " pennies."); 
        }
    }
}

