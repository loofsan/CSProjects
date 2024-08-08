// Lynn T. Aung
// July 10, 2023
// Lab 9
// This lab will create a method which will count.

public class Counter
{
    private int counter = 0;
    
    public void reset()
    {
        counter = 0;
    }
    
    public void add()
    {
        counter += 1;
    }
    
    public void subtract()
    {
        if (counter == 0) 
        {
            counter = 0;
        }
        else
        {
            counter -= 1;
        }
    }
    
    public int returnCounter()
    {
        return counter;
    }
    
    public void showCount() 
    {
        System.out.println(counter);
    }
}