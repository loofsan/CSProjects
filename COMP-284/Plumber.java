// Lynn T. Aung
// July 17, 2023
// Lab 10
// This lab will make a derived class of the Person class in page 587

public class Plumber extends Person
{
     private String townArea;
     private double tripFee;
     
     public Plumber() // Constructor
     {
          super();
          townArea = "None";
          tripFee = 0;
     }
     
     public Plumber(String initialName, String initialTownArea, double initialTripFee) //Contructor
     {
          super(initialName);
          setTownArea(initialTownArea);
          setTripFee(initialTripFee);
     }
     
     @Override
     public void writeOutput() //Override the Person class's writeOutput()
     {
          super.writeOutput();
          System.out.println("Town Area: " + townArea
           + "\nTrip Fee: " + tripFee + "\n");
     }
     
     public void setTownArea(String newTownArea) 
     {// Check to see if townArea is correct and mutate it if need be
          String newTA = newTownArea.toLowerCase();
          if (newTA.equals("west") || newTA.equals("east")
           || newTA.equals("south") || newTA.equals("north"))
          {
               townArea = newTownArea;
          }
          
          else
          {
               System.out.println("Town area is not allowed.");
               System.exit(0);
          }
     }
     
     public String getTownArea()
     {
          return townArea;
     }
     
     public void setTripFee(double newTripFee)
     {//Check to see if tripFee is positive and mutate it if need be
          if (newTripFee > 0)
          {
               tripFee = newTripFee;
          }
          else
          {
               System.out.println("The fee cannot be negative.");
               System.exit(0);
          }
     }
     
     public double getTripFee()
     {
          return tripFee;
     }
     
     public boolean isSamePlumber (Plumber otherPlumber)
     {
          return hasSameName((Person) otherPlumber) && 
           (this.townArea.equals(otherPlumber.townArea)) &&
           (this.tripFee == otherPlumber.tripFee);
     }
}
