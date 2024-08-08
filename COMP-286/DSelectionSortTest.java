// Lynn T. Aung
// Double Selection Sort Test

import java.util.Arrays;

public class DSelectionSortTest {

	public static void main (String [] args) {
    
		int [] testArray = {3, 46, 93, 100, 2, 54}; 
        System.out.println("Original Array: " + Arrays.toString(testArray));
        
		DoubleSelectionSort dss = new DoubleSelectionSort();
		dss.doubleSelectionSort(testArray);
        System.out.println("Final Array: " + Arrays.toString(testArray));
        
        System.out.println("");
        
        int [] testArray2 = {300, 46, 93, 100, 2, 1}; 
        System.out.println("Original Array: " + Arrays.toString(testArray2));
        
        dss.doubleSelectionSort(testArray2);
        System.out.println("Final Array: " + Arrays.toString(testArray2));
        
	}
}