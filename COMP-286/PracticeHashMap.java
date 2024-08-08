// Lynn T. Aung
// COMP - 286
// October 24, 2023

import java.util.HashMap;

public class PracticeHashMap 
{
    public static void main (String [] args) 
    {
        // Make Eng dict
        HashMap<String, String> dictionary = new HashMap<String, String>();
        // Add keys and values of words and 
        // definitions for the English Dictionary
        dictionary.put("stop",
            "(of an event, action, or process) come to an end; cease to happen");
        dictionary.put("eat",
            "put (food) into the mouth and chew and swallow it");
        dictionary.put("walk",
            "move at a regular pace by lifting and setting down each foot " +
            "in turn, never having both feet off the ground at once");
        dictionary.put("clap",
            "strike the palms of (one's hands) together repeatedly, " +
            "typically in order to applaud someone or something");
            
        // Make spanish dict    
        HashMap<String, String> notEnglish = new HashMap<String, String>();
        // Add keys and values of words and 
        // definitions for the Spanish Dictionary
        notEnglish.put("parar", 
            "(de un evento, acción o proceso) llegan a su fin; dejar de suceder");
        notEnglish.put("comer", 
            "Ponga (alimento) en la boca y mastique y trague");
        notEnglish.put("caminar", 
            "moverse a un ritmo regular levantando y colocando cada pie a su" +
            " vez, nunca teniendo ambos pies fuera del suelo a la vez");
        notEnglish.put("aplaudir",
            "golpear las palmas de las manos juntas repetidamente, " +
            "generalmente para aplaudir a alguien o algo");
        
        // Make a hashmap of language dictionaries
        HashMap<String, HashMap<String, String>> languageDictionary = new HashMap<String, HashMap<String, String>>();
        
        languageDictionary.put("English", dictionary);
        languageDictionary.put("Spanish", notEnglish);
        
        // Print the English Dictionary
        System.out.println("Printing all words in the English dictionary . . .");
        System.out.println("(word) : (definition)\n");
        
        for(String word: dictionary.keySet()) 
        {
            System.out.println(word + ": " + dictionary.get(word));
        }
        
        System.out.println("\nEnd of process . . .\n");
       
        // Print the Spanish Dictionary
        System.out.println("Printing all words in the Spanish dictionary . . .");
        System.out.println("(word) : (definition)\n");
        
        for(String word: notEnglish.keySet()) 
        {
            System.out.println(word + ": " + notEnglish.get(word));
        }
        
        System.out.println("\nEnd of process . . .\n");
        
        // Print both dictionaries from the language dictionary
        System.out.println("Printing dictionaries from the language Dictionary . . .\n");
        
        for(String lang: languageDictionary.keySet()) 
        {
            System.out.println("Available dictionaries: " + lang);
        }
       
        System.out.println("\nEnd of process . . .\n");
    }
}