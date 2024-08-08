// Lynn T. Aung
// July 15, 2023
// Lab 10
// This lab will compute the cost of flowers sold at a flower stand.
import java.util.Scanner;
public class FlowerCounter 
{
    public void flowerShop()
    {   // Make arrays and import Scanner
        Scanner input = new Scanner(System.in);
        String [] flowerName= new String[5];
        int [] flowerCost = new int[5];
        
        flowerName[0] = "petunia";
        flowerName[1] = "pansy";
        flowerName[2] = "rose";
        flowerName[3] = "violet";
        flowerName[4] = "carnation";
        
        flowerCost[0] = 50;
        flowerCost[1] = 75;
        flowerCost[2] = 150;
        flowerCost[3] = 50;
        flowerCost[4] = 80;
        // Show Flowers 
        System.out.println("     Welcome  to \n"
         + "-----Flower Shop-----\n");
        System.out.println("Here's our available flowers: \n");
        System.out.println("[1]Petunia: 50 cents          [2]Pansy: 75 cents\n"
         + "[3]Rose: $1.50                [4]Violet: 50 cents\n"
         + "[5]Carnation: 80 cents");
         
        // Ask for flowers
        System.out.println("\nWhich flower would you like to buy?"
         + "\nType '0' to quit.");
        int flower = input.nextInt();
        // Allow the user to make mistakes and allow them to stop.
        while (flower < 0 || flower > 5)
        {
            System.out.println("This flower isn't available.");
            System.out.println("\nWhich flower would you like to buy?"
             + "\nType '0' to stop.");
            flower = input.nextInt();
        }
        // Check if the user has stopped or not.
        if (flower > 0 && flower < 5)
        {
            System.out.println("How many would you like to buy?");
            int qty = input.nextInt();
            while (qty < 0)
            {
                System.out.println("You cannot buy less flowers than 0.");
                System.out.println("How many would you like to buy?");
                qty = input.nextInt();
            }
            
            //Conversion from cents to dollars
            double money = qty * (double) flowerCost[flower - 1];
            money /= 100;
            
            // Compute the cost.
            if (qty < 1)
            {
                System.out.println("Hello, you bought " + qty + " "
                 + flowerName[flower - 1] + " and it costs $"
                 + money + ".");
            }
            else
            {
                System.out.println("Hello, you bought " + qty + " "
                 + flowerName[flower - 1] + "s and it costs $"
                 + money + ".");
            }
        }
        
        else
        {
            System.out.println("Please come again.");
        }
    }
}

