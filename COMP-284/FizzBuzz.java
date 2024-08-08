// Lynn T. Aung
// June 29, 2023
// Fizz-Buzz Lab
// This will prompt the user for a game of FizzBuzz 
// and how long they want to play it.

import java.util.Scanner;
public class FizzBuzz
{
	public void fizzBuzzGame()
	{	
		Scanner input = new Scanner(System.in);
		System.out.println("Please type the number of rounds to play "
		 + "Fizz-Buzz");
		int answer = input.nextInt();
        
        while (answer < 0) 
        {
            System.out.println("Please type a positive number.");
            System.out.println("Please type the number of rounds to play "
		     + "Fizz-Buzz");
		    answer = input.nextInt();
        }
        
		System.out.println("\n");
        System.out.println("***** Fizz-Buzz Game *****");
		for(int i = 0; i <= answer; i++) 
		{
			if (i%3 == 0 && i%5 == 0 && i!=0)
			{
				System.out.println("Fizz-Buzz");
			}
			else if (i%3 == 0 && i!=0)
			{
				System.out.println("Fizz");
			}
			else if (i%5 == 0 && i!=0) 
			{		
				System.out.println("Buzz");
			}
			else
			{
				System.out.println(i);
			}
		}
		
	}
		
}