// Lynn T. Aung
// COMP 252
// Singly Linked List Function
// 
//  main.cpp
//  SinglyLinkedList
//
//  Created by Ariel Katz on 2/7/23.
//

#include <iostream>
#include "SinglyLinkedList.h"


using namespace std;

int main() {
    
    SinglyLinkedList<int> list;
    list.insertFirst(2);
    list.insertFirst(3);
    list.insertFirst(5);
    list.insertLast(7);
    list.insertLast(11);
    list.insertLast(13);
    cout << "size: "  << list.length() << endl;
    list.print();
    cout << endl;
    
    list.deleteNode(5);
    list.print();
    cout << endl;
    
    //Test deleting last item
    list.deleteNode(13);
    list.print();
    cout << endl;
    
    //Test deleting middle item
    list.deleteNode(2);
    list.print();
    cout << endl;

    // Test delete all
    list.deleteNode(3);
    list.deleteNode(7);
    list.deleteNode(11);
    cout << "Empty List" << endl;
    list.print();
    cout << endl;

    // Test Inserting in an empty list
    list.insertFirst(1);
    list.print();
    cout << endl;
    list.deleteNode(1);

    // Test Inserting in an empty list with insert Last
    list.insertLast(10);
    list.print();
    cout << endl;
    
    return 0;
}
