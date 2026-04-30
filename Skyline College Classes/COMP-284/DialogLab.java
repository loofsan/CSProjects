// Author: Lynn T. Aung
// Date: June 27, 2023
// Lab 6
// This lab will use dialog boxes to check if the user wants sandwiches.
import javax.swing.JOptionPane;
public class DialogLab
{
    public static void main (String [] args) 
    {
        int answer = JOptionPane.showConfirmDialog(null, "Do you want ham sandwiches?",
                        "Ham Sandwiches", JOptionPane.YES_NO_OPTION);
        if (answer == JOptionPane.YES_OPTION) 
        {
            System.out.println("Hello, here's your Ham Sandwich!");
        }
        else
        {
            System.out.println("Thank you, Please come visit again! :)");
        }
    }
}