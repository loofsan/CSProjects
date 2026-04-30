// Lynn T. Aung
// 6-21-2023
// Lab 4, Inches To Centimeters
// This lab will convert inches to centimeters.

import java.util.Scanner;
public class InchesToCm
{
    
    public static void main (String [] args)
    {
    
        Scanner input = new Scanner(System.in);
        
        System.out.println
        ("*** This program will convert inches to centimeters ***\n");
        
        // Grab the number of inches we want to convert
        System.out.print("Number of inches (Whole Numbers) to convert: ");
        int inches = input.nextInt();
        input.nextLine();
        
        // Convert inches to cm
        double cm = inches * 2.54;
        
        System.out.println("Centimeters: " + cm + " cm");
           
    }
}