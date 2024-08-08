// Lynn T. Aung
// July 24, 2023
// Lab 13
// This lab will take in shop purchases and write them into a text file
// and read it out.

import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.io.File;

public class ShopPurchase
{
    public static void itemBeeper()
    {
        Scanner keyboard = new Scanner (System.in);
        String fileName = "answers.txt";
        PrintWriter outputStream = null;
        Scanner inputStream = null;
        double totalCost = 0;
        int totalItems = 0;
        //Open the file to write it in.
        try
        {
            outputStream = new PrintWriter(fileName);
        }
        catch (FileNotFoundException e)
        {
            System.out.println("File Not Found");
            System.exit(0);
        }
        // Write the answers in the text file.
        System.out.println("Enter " 
         + "Items, Item Price, Number Of Items");
        System.out.println("For example: 'Mangoes, 3, 20'"); 
        for (int i = 1;i < 5;i++)
        {   
            String answer = keyboard.nextLine();
            outputStream.println(answer);        
        }
        outputStream.close(); //Flush buffer
        System.out.println("Items saved in file.\n");
        // Open the text file to read it
        try
        {
            inputStream = new Scanner(new File(fileName));
            while (inputStream.hasNextLine())//Check if there's more lines
            {
                String ans = inputStream.nextLine(); //Parse the strings
                String [] array = ans.split(", ");
                String item = array[0];
                double itemPrice = Double.parseDouble(array[1]);
                int numberOfItems = Integer.parseInt(array[2]);  
                System.out.printf("Purchased %d %s at $%1.2f for each.\n",
                 numberOfItems, item, itemPrice);
                totalCost += (itemPrice * numberOfItems);   
                totalItems += Integer.parseInt(array[2]);    
            }
            
            System.out.println("\nTotal Items: " + totalItems);
            System.out.printf("Total Cost: $%1.2f", totalCost);
            inputStream.close(); //Flush
        }
        catch (FileNotFoundException e)
        {
            System.out.println("File Not Found");
            System.exit(0);
        }     
    }
}