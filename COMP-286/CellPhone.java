// Lynn T. Aung
// 9-10-23

/* 
   Making Communicator Abstract class with constructor 
   with a getter and setter for model
*/
abstract class Communicator 
{
    private String model;
    
    public Communicator(String model)
    {   
        this.model = model;
    }
    
    public String getModel()
    {
        return model;
    }
    
    public void setModel(String newModel)
    {
        model = newModel;
    }
    
    abstract void communicate();
}

// CellPhone Class
class CellPhone extends Communicator 
{
    private long phoneNumber;
    private String owner;
    private boolean isSmartPhone;
    
    //Cellphone Constructor
    public CellPhone(String model, String owner, long phoneNumber, 
      boolean isSmartPhone)
    {
        super(model);
        this.owner = owner;
        this.phoneNumber = phoneNumber;
        this.isSmartPhone = isSmartPhone;
    }
    
    //Getters and Setters for all variables
    public long getPhoneNumber()
    {
        return phoneNumber;
    }
    
    public void setPhoneNumber(long newPhoneNumber)
    {
        phoneNumber = newPhoneNumber;
    }
    
    public String getOwner()
    {
        return owner;
    }
    
    public void setOwner(String newOwner)
    {
        owner = newOwner;
    }
    
    public boolean getIsSmartPhone()
    {
        return isSmartPhone;
    }
    
    public void setIsSmartPhone(boolean newIsSmartPhone)
    {
        isSmartPhone = newIsSmartPhone;
    }
    
    // Making method communicate()
    public void communicate()
    {
        System.out.println("Calling from a " + getModel() + " with number "
         + phoneNumber);
    }
}

// Fax Machine Class
class FaxMachine extends Communicator
{
    private long faxNumber;
    
    // Constructor
    public FaxMachine(long faxNumber)
    {
        super("Fax Machine");
        this.faxNumber = faxNumber;
    }
    
    //Setters and Getters for Fax Machines
    public long getFaxNumber()
    {
        return faxNumber;
    }
    
    public void setFaxNumber(long newFaxNumber)
    {
        faxNumber = newFaxNumber;
    }
    
    @Override 
    public void setModel(String model)
    {
        super.setModel("Fax:" + model);
    }
    
    // Making method communicate for Fax
    public void communicate()
    {
        System.out.println("Sending data to " + getModel());
    }
}

