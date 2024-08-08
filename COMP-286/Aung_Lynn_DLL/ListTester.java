import java.util.List;

public class ListTester{
	public static void main(String[] args) {

		System.out.println();

		System.out.println("Testing doubly linked list...");
        System.out.println();
        
		DLinkedList<Integer> numberList = new DLinkedList<>();
		testListWithIntegers(numberList);

		DLinkedList<String> strList = new DLinkedList<>();
		testListWithStrings(strList);
        
		System.out.println("...end of double link tests");

	}

	public static void testListWithIntegers(List<Integer> numList){
		numList.add(12);
		numList.add(3);
		numList.add(0, 15);

		try {
			numList.add(5, 45);
			System.out.println("ERROR - exception missed");
		} catch (IndexOutOfBoundsException e) {
			System.out.println("Correctly caught add out of bounds exception");
		}

		System.out.println(numList);
		System.out.println("Expected list: 15, 12, 3");
        System.out.println();
        
        numList.remove(0);
        System.out.println(numList);
        System.out.println("Expected list: 12, 3");
        System.out.println();
        
        numList.add(20);
        numList.add(30);
        numList.add(89);
        System.out.println(numList);
        System.out.println("Expected list: 12, 3, 20, 30, 89");
        System.out.println();
        
        numList.remove(4);
        System.out.println(numList);
        System.out.println("Expected list: 12, 3, 20, 30");
        System.out.println();
        
        numList.set(2, 99);
        System.out.println(numList);
        System.out.println("Expected list: 12, 3, 99, 30");
        System.out.println();
        
        numList.remove(3);
        System.out.println(numList);
        System.out.println("Expected list: 12, 3, 99");
        System.out.println();
        
        numList.clear();
        System.out.println(numList);
        System.out.println("Expected list: ");
        System.out.println();
 
        numList.add(89);
        System.out.println(numList);
        System.out.println("Expected list: 89");
		System.out.println();
	}

	public static void testListWithStrings(List<String> wordList){

		wordList.add("house");
		wordList.add("window");
		wordList.add("door");
		wordList.add(1, "roof");

		if ( wordList.size() != 4 ){
			System.out.println("ERROR - incorrect size");
		}

		System.out.println(wordList);
		System.out.println("Expected list: house, roof, window, door");
        System.out.println();
        
		String test = wordList.get(2);
		if ( !test.equals("window")){
			System.out.println("Error - Unexpected element at index 2");
		}
		
		System.out.println(wordList);
		System.out.println("Expected list: house, roof, window, door");
        System.out.println();
        
        wordList.remove(3);
        System.out.println(wordList);
		System.out.println("Expected list: house, roof, window");
        System.out.println();
        
        wordList.set(0, "school");
        wordList.set(2, "new");
        System.out.println(wordList);
		System.out.println("Expected list: school, roof, new");
        
        System.out.println();
	}
}