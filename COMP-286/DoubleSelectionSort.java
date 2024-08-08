// Lynn T. Aung
// Double Selection Sort
// November 6, 2023

public class DoubleSelectionSort {

	public static void doubleSelectionSort(int [] list) 
    { 
        int minIndex = 0;
		int maxIndex = list.length-1;
		for (int i = 0; i < list.length; i++) 
        {
			if (list[minIndex] > list[i]) {
				swap(list, minIndex,i);
			}
			else if (list[maxIndex] < list[i]) {
				swap(list, maxIndex,i);
			}
		}
	}


	public static void swap (int [] list, int index1, int index2) 
    {
		int temp = list[index1];
		list[index1] = list[index2];
		list[index2] = temp; 
	}
}