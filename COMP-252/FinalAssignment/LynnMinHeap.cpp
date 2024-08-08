// Lynn T. Aung
// 5 - 15 - 2024
// Assignment 7 - Pick Your Program (Main Program)

#include <iostream>
#include <vector>

using namespace std;

template<class Type>
class MinHeap {

    public:
        MinHeap() {}
        // Constructor for the MinHeap
        void insert(const Type& value);
        // Function to insert a value to a heap
        // it heapifies up with the inserted value.
        Type extractMin();
        // Function to extract the minimum number in the heap
        // takes the minimum value which is at the top and
        // heapifies down to re-order the heap.
        void print();
        // Function to print the heap
        static void sort(vector<Type>& unsorted);
        // Function to sort the heap
        // It puts all the values in a temporary heap 
        // and then use extractMin() to insert the minimum
        // values back in.

    private:
        vector<Type> vArray;
        // Private underlying vector for the min heap.
        void heapifyUp(int index);
        // Function to make the heap property in order.
        // The heapify up function swaps the current element with its
        // parent if the parent's value is greater than the 
        // current element's value.
        // Then, it loops
        void heapifyDown(int index);
        // Function to make the heap property in order.
        // The heapify down first calculates the index of the right and left
        // child of the current element. Then, it checks to make sure they're 
        // valid and swaps if the child is smaller than the current element
        // for both sides. Then, it recurses.
        
};

template<class Type>
void MinHeap<Type>::heapifyUp(int index) {

    // while index is more than 0 and current element at the index
    // is less than its parent
    while (index > 0 && vArray[index] < vArray[(index - 1) / 2]) {
        // swaps the current element with parent element if 
        // parent element is bigger
        swap(vArray[index], vArray[(index - 1) / 2]);
        // update
        index = (index - 1) / 2;
    }

}

template<class Type>
void MinHeap<Type>::heapifyDown(int index) {
    // Define the indices of the left and right
    // child and the smallest element "currently"
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    // Checks if left is valid and less than current smallest element
    // if so swap
    if (left < vArray.size() && vArray[left] < vArray[smallest])
        smallest = left;

    // Checks if right is valid and less than current smallest element
    // if so swap
    if (right < vArray.size() && vArray[right] < vArray[smallest])
        smallest = right;
    
    // if smallest element changed from original index, swap
    if (smallest != index) {
        swap(vArray[index], vArray[smallest]);
        // Recurse
        heapifyDown(smallest);
    }
}

template<class Type>
void MinHeap<Type>::insert(const Type& value) {
    // Add the new element to the back of the vector
    vArray.push_back(value);
    // heapify up
    heapifyUp(vArray.size() - 1);
}

template<class Type>
Type MinHeap<Type>::extractMin() {
    // Check if vector empty
    if (vArray.empty()) {
        cout << "Heap is empty" << endl;
    }

    // Save the minimum element at the front
    Type min = vArray[0];
    // The last element is now at the root
    vArray[0] = vArray.back();
    // The last element is removed
    vArray.pop_back();
    // Heapify down
    heapifyDown(0);

    return min;
}

template<class Type>
void MinHeap<Type>::print() {
    // Basic for-loop print function
    for (const auto& element : vArray) {
        cout << element << " ";
    }
    cout << endl;
}

template<class Type>
void MinHeap<Type>::sort(vector<Type>& unsorted) {

    vector<Type> result;
    MinHeap<Type> tempHeap;

    // Put all the elements into a temporary heap
    for (const auto& value : unsorted)
        tempHeap.insert(value);

    // Put all the elements from temp into the actual heap 
    // with the minimum -> maximum
    while (!tempHeap.vArray.empty())
        result.push_back(tempHeap.extractMin());

    unsorted = result;
}

int main() {

    // Making a MinHeap of integers and demonstrating functions

    MinHeap<int> numHeap;
    numHeap.insert(17);
    numHeap.insert(2);
    numHeap.insert(5);
    numHeap.insert(6);
    numHeap.insert(1);
    numHeap.insert(7);

    cout << endl;
    cout << "Demonstrating Print Function" << endl;
    cout << "Printing Integer MinHeap . . . " << endl;
    numHeap.print();
    cout << endl;

    cout << "Demonstrating ExtractMin() Function" << endl;
    int num = numHeap.extractMin();
    cout << "Minimum Number: " << num << "\n" << endl;

    cout << "Demonstrating Print Function" << endl;
    cout << "New heap: ";
    numHeap.print();
    cout << endl;

    // Making a MinHeap of doubles and demonstrating functions

    MinHeap<double> doubleHeap;
    doubleHeap.insert(17.4);
    doubleHeap.insert(22.5);
    doubleHeap.insert(3921.3);
    doubleHeap.insert(63.234);
    doubleHeap.insert(17.5);
    doubleHeap.insert(17.3);

    cout << endl;
    cout << "Demonstrating Print Function" << endl;
    cout << "Printing Double MinHeap . . . " << endl;
    doubleHeap.print();
    cout << endl;

    cout << "Demonstrating ExtractMin() Function" << endl;
    double doubleNum = doubleHeap.extractMin();
    cout << "Minimum Number: " << doubleNum << "\n" << endl;

    cout << "Demonstrating Print Function" << endl;
    cout << "New heap: ";
    doubleHeap.print();
    cout << endl;

    // Sorting an Array(vector) of strings

    vector<string> strArray = {"cow", "dog", "giraffe", "alien", "platypus"};
    cout << "Unsorted Array: " << endl;
    for(string word: strArray) {
        cout << word << " ";
    }
    cout << "\n" << endl;

    cout << "Demonstrating Sorting Function" << endl;
    MinHeap<string>::sort(strArray);
    cout << "Sorted Array: " << endl;

    for (string word: strArray) {

        cout << word << " ";

    }
    cout << "\n" << endl;

    return 0;
}
