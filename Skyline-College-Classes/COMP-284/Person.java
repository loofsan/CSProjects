// Lynn T. Aung
// July 17, 2023
// Lab 10
// This lab will make a base class and a derived class

public class Person // Got this from the book in page 587
{
     private String name;
     
     public Person()
     {
          name = "No name yet";
     }
     
     public Person(String initialName)
     {
          name = initialName;
     }
     
     public void setName (String newName)
     {
          name = newName;    
     }
     
     public String getName()
     {
          return name;
     }
     
     public void writeOutput()
     {
          System.out.println("Name: " + name);
     }
     
     public boolean hasSameName (Person otherPerson)
     {    
          return this.name.equalsIgnoreCase(otherPerson.name);
     }
}