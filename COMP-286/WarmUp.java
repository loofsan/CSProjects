// Lynn T. Aung
// 8-24-2023

public class WarmUp 
{
    /*
    This method will reply with FizzBuzz if the number given is divisible by both 3 and 5, 
    it will reply with Fizz if it is only divisible by 3 and a Buzz if it is divisible by 5 only.
    Otherwise, if they're not divisible by both, it will just return the number.
    */
    public static void fizzBuzz(int num)
    {
        if (num % 3 == 0 && num % 5 == 0)
        {
            System.out.println("Fizz Buzz");
        }
        else if (num % 3 == 0)
        {
            System.out.println("Fizz");
        }
        else if (num % 5 == 0)
        {
            System.out.println("Buzz");
        }
        else
        {
            System.out.println(num);
        }
    }
    
    public static void main (String []args)
    {
        int [] testArray = {0, 10, 6, 15, 7, 17};
        
        for (int i=0;i<testArray.length;i++)
        {
            fizzBuzz(testArray[i]);
        }
    }
}