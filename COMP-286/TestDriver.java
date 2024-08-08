// Lynn T. Aung
// 9-10-23
// This is the test driver class for CellPhone
import java.util.ArrayList;

public class TestDriver
{
    public static void main (String [] args)
    {
        // Instantiating cellphones and fax machines
        CellPhone cell1 = new CellPhone("Apple", "Owner1", 131313434, true);
        CellPhone cell2 = new CellPhone("Samsung", "Owner2", 864803838, true);
        CellPhone cell3 = new CellPhone("Pixel", "Owner3", 938483502, false);
        FaxMachine fax1 = new FaxMachine(929838);
        fax1.setModel("foo123");
        FaxMachine fax2 = new FaxMachine(666666);
        fax2.setModel("quux456");
        FaxMachine fax3 = new FaxMachine(888888);
        
        
        // Making a communicator ArrayList with both cellphones and faxes
        ArrayList<Communicator> communicators = new ArrayList<Communicator>();
        communicators.add(cell1);
        communicators.add(cell2);
        communicators.add(cell3);
        communicators.add(fax1);
        communicators.add(fax2);
        communicators.add(fax3);
        
        //testing communicate method
        for (Communicator c : communicators) 
        {
            c.communicate();
        }
        
        // Adding space between outputs
        System.out.print("\n");
        
        // testing getter methods for cellphones
        System.out.println("Testing cell phones (Cell1). . .");
        System.out.println("Before Setting: ");
        System.out.println(cell1.getPhoneNumber());
        System.out.println(cell1.getOwner());
        System.out.println(cell1.getIsSmartPhone());
        
        // testing setter methods for cellphones
        System.out.println("\nAfter Setting: ");
        cell1.setPhoneNumber(000000000);
        cell1.setOwner("fooBar");
        cell1.setIsSmartPhone(false);
        
        System.out.println(cell1.getPhoneNumber());
        System.out.println(cell1.getOwner());
        System.out.println(cell1.getIsSmartPhone());
        
        // testing getter methods for faxes
        System.out.println("\nTesting Faxes (fax1) . . .");
        System.out.println("Before Setting: ");
        System.out.println(fax1.getModel());
        System.out.println(fax1.getFaxNumber());
        
        System.out.println("\nAfter Setting: ");
        fax1.setModel("Lynn123");
        fax1.setFaxNumber(444444444);
        System.out.println(fax1.getModel());
        System.out.println(fax1.getFaxNumber());
    }
}