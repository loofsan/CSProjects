// Lynn T. Aung
// 9-26-2023
// Generics Exercises
// Exercise 1

public class ProductDisplay<T, E, V>
{// Three different items with different classes
    private T displayItem1;
    private E displayItem2;
    private V displayItem3;
    
    public ProductDisplay(T item) // Constructor
    {   
        displayItem1 = item;
    }
    
    public ProductDisplay(T item, E item2, V item3) // Overloaded Constructor
    {
        displayItem1 = item;
        displayItem2 = item2;
        displayItem3 = item3;
    }
    
    public static void main (String [] args)
    {   
        // Making objects with FileClassesExample.java
        AudioFile testFile1 = new AudioFile("hello.mp3");
        VideoFile testFile2 = new VideoFile("ScreenRecording.mp4");
        VideoFile testFile3 = new VideoFile("ScreenRecording1.mp4");
        
        // Instantiating
        ProductDisplay<AudioFile, VideoFile, VideoFile> display = 
         new ProductDisplay(testFile1, testFile2, testFile3);
        
    }
}

/* 
A Pro & Con of using different types

Pro
- It can hold many different types of objects in one class

Con
- A con of using a lot of different types is that the programmer
  has to keep track of all of them so as to not mix any types for 
  certain methods and they have to be careful with it.
*/