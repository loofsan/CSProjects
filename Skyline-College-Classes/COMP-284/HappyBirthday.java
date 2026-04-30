// Lynn T. Aung
// 6/21/2023
// Lab 3
// This lab will ask the user for their age and
// it will return how old they will be after their next birthday.

import java.util.Scanner;

public class HappyBirthday 
{

    public static void main (String [] args) 
    {
    
        Scanner input = new Scanner(System.in);
        // Ask for name
        System.out.println("Hello, what's your name?");
        String name = input.nextLine();
        // Ask for age
        System.out.println("How old are you?");
        int age = input.nextInt();
        input.nextLine();
        
        System.out.println("Hello, " + name + ". You will be "
                           + (++age) 
                           + " years old after your next birthday."); 
        System.out.print("Happy Birthday!");
    }
}