// Lynn T. Aung
// July 5, 2023
// Lab 8
// This lab will take in two integer parameters and 
// compare them to see which is bigger.
import java.util.Scanner;
public class ComparisonInt
{   // This functions compares the first integer to the second integer.
    public boolean compareInt(int num1, int num2)     {
        return num1 > num2;
    }
    
    public void integerComparison()
    {
        Scanner input = new Scanner(System.in);
        // Takes in integers
        System.out.print("Hello, please type in an integer: ");
        int ans1 = input.nextInt();
        input.nextLine();
        System.out.print("Hello, please type in another integer: ");
        int ans2 = input.nextInt();
        // Uses the function compareInt() to see if the first integer is bigger.
        if (compareInt(ans1, ans2))
        {
            System.out.println("The first integer is Bigger.");
        }
        else
        {
            System.out.println("The first integer is Smaller.");
        }    
    }
}