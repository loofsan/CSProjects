// Lynn T. Aung
// July 10, 2023
// Lab 9
// This will test the method in Lab 9.

public class CounterTest
{
    public static void main (String [] args)
    {
        Counter test = new Counter();
        test.subtract();
        test.showCount();
        System.out.println(test.returnCounter());
        
        test.add();
        test.add();
        test.add();
        test.add();
        test.showCount();
        System.out.println(test.returnCounter()); 
        
        test.subtract();
        test.showCount();
        System.out.println(test.returnCounter());   
          
        test.reset();
        test.showCount();
        System.out.println(test.returnCounter());  

    }
}