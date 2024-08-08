// Lynn T. Aung
// 9-25-23
// Recursion With Strings

public class StringHelper
{
    public static String cleanString(String input)
    {
        // My base case
        if (input.length() <= 1)
        {
            return input;
        }
        
        //Make the first character
        char firstChar = input.charAt(0);
        int charAscii = firstChar; // Make it into an Ascii
        
        /*Check if they're duplicates and check if they're letters 
          otherwise, punctuations can be duplicate */
        if (firstChar == input.charAt(1) && 
            ((charAscii >= 65 && charAscii <= 90) ||
            (charAscii >= 97 && charAscii <= 122)))
        {  
            String newString = input.substring(1); //Cut off the first char
            return (cleanString(newString));       //Recurse
        }
        else
        {   // In case there's no duplicates, recurse here with the first character added
            return (firstChar + cleanString(input.substring(1)));
        }
    }
    
    // There's an edge case of words with duplicate letters like *loop*, *door*
    
    public static void main (String [] args)
    {
        //Edge case here as words with duplicate letters exist
        String test1 = "door";
        String test2 = "watttteer in thhhhhhhheee llllakke";
        String test3 = "ggrreatttt dayyy!!";
        String test4 = "so.... whhhaaaat diiidd you sayy?";
        String test5 = "He         y";
        
        System.out.println("Before:");
        System.out.println(test1);
        System.out.println(test2);
        System.out.println(test3);
        System.out.println(test4);
        System.out.println(test5);
        
        System.out.println("\n");
        
        System.out.println("After:");
        System.out.println(cleanString(test1));    
        System.out.println(cleanString(test2));
        System.out.println(cleanString(test3));
        System.out.println(cleanString(test4));
        System.out.println(cleanString(test5));
    }
}
