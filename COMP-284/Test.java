import java.util.Scanner;

public class Test 
{
    public static void main(String [] args)
    {
        int item;
        Scanner keyboard = new Scanner (System.in);
        
        System.out.println("Put in a number");
        item = keyboard.nextInt();
        
        if (item % 5 != 0) 
        {
            System.out.println("it doesn't work!!");
        }
        else
        {
            System.out.println("This work");
        }
            
    }


}