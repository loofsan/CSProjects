// Lynn T. Aung
// July 17, 2023
// Lab 10
// This class will test Lab 10

public class PlumberTest
{
     public static void main (String [] args)
     {
          Plumber plumber1 = new Plumber("Lynn", "West", 10.50);
          
          plumber1.writeOutput();
          plumber1.setName("John");
          plumber1.writeOutput(); 
          
          Plumber plumber2 = new Plumber();
          plumber2.writeOutput();
          System.out.println(plumber2.isSamePlumber(plumber1));  
          
          plumber2.setName("Chris");
          plumber2.setTripFee(920);
          // plumber2.setTownArea("DalyCity");
          plumber2.setTownArea("South");
          plumber2.writeOutput();
          
          Plumber plumber3 = new Plumber("John", "West", 10.50);
          
          System.out.println(plumber3.isSamePlumber(plumber1));
          
     }
}