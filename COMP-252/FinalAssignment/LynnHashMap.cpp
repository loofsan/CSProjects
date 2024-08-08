// Lynn T. Aung
// 5 - 15 - 2024
// Assignment 7 - Pick Your Program (Extra Credit)

#include <iostream>
#include <functional>

using namespace std;

template<class Key, class Value>
class HashMap {
private:
    struct HashMapEntry {
        Key key;
        Value value;
        bool isEntry; 
    };

    HashMapEntry* bins;
    int num_keys;
    int size;
    const float loadFactor;

    // Hash function for the keys
    int hash(const Key& key) const {
        return std::hash<Key>{}(key) % size;
    }

    // Function to automatically resize
    void resize(int newSize) {
        // Makes memory for a new array defined by newSize
        HashMapEntry* newBins = new HashMapEntry[newSize];
        // Make all the spaces in the arrays false (empty)
        for (int i = 0; i < newSize; ++i) {
            newBins[i].isEntry = false;
        }
        // Rehash the same elements and find the index in the new bin to 
        // put the elements in.
        for (int i = 0; i < size; ++i) {
            if (bins[i].isEntry) {
                int index = hash(bins[i].key);
                // Use linear probing to find the next available slot
                while (newBins[index].isEntry) {
                    index = (index + 1) % newSize;
                }
                // Give data
                newBins[index] = bins[i];
            }
        }
        delete[] bins;
        bins = newBins;
        size = newSize;
    }

    // Function to track the load factor
    void trackLoadFactor() {
        // Find out current load factor
        float currentLoadFactor = (float)(num_keys) / size;
        // Check if current load factor is more than 75% (loadFactor)
        if (currentLoadFactor > loadFactor) {
            // If it is, double the array size like a vector
            int newSize = size * 2; 
            resize(newSize);
        }
    }

public:
    // Make a constructor for the hash map
    HashMap(int initial_size = 10, float load_factor = 0.75)
        :bins(new HashMapEntry[initial_size]), num_keys(0), size(initial_size), 
          loadFactor(load_factor) 
    {
        for (int i = 0; i < size; ++i) {
            bins[i].isEntry = false;
        }
    }

    // Function to insert a key and a value into the hashmap
    void insert(const Key& key, const Value& value) {
        // See if the array needs to be resized or not
        trackLoadFactor();
        // Find the hash for the key
        int index = hash(key);
        // Use linear probing if index is filled while the key is different
        while (bins[index].isEntry && bins[index].key != key) {
            index = (index + 1) % size;
        }
        // If found empty slot, insert the new key-value pair
        if (!bins[index].isEntry) {
            bins[index] = {key, value, true};
            num_keys++;
        } else {
            // If key already exists, update the value
            bins[index].value = value;
        }
    }

    Value find(const Key& key) const {
        // Find the hash of the key
        int index = hash(key);
        int count = 0;
        // Find the key while it's valid (bin not empty, key not equal key, 
        // hasn't reached the end)
        while (bins[index].isEntry && bins[index].key != key && count != size) {
            index = (index + 1) % size;
            count++;
        }
        // Return the value
        if (bins[index].isEntry && bins[index].key == key) {
            return bins[index].value;
        } else {
            // No results
            return Value{};
        }
    }

    // Basic function to print the hashmap
    void print() const {
        for (int i = 0; i < size; ++i) {
            if (bins[i].isEntry) {
                cout << "{Key: " << bins[i].key << ", Value: " << 
                bins[i].value << "}\n" << endl;
            }
        }
    }
};

int main() {
    HashMap<string, string> dictionary;
    dictionary.insert("walk", 
    "move at a regular pace by lifting and setting down each foot in turn," 
    "never having both feet off the ground at once.");

    dictionary.insert("eat", "to take in through the mouth as food");

    dictionary.insert("kill", "cause the death of (a person, animal," 
    "or other living thing).");

    dictionary.insert("nice", "pleasant; agreeable; satisfactory.");

    cout << "Meaning of 'walk': " << dictionary.find("walk") << "\n" << endl;

    dictionary.print();

    HashMap<int, string> numHashMap;
    numHashMap.insert(1, "One");

    numHashMap.insert(2, "Two");

    numHashMap.insert(3, "Three");

    numHashMap.insert(4, "Four");

    cout << "1: " << numHashMap.find(1) << "\n" << endl;

    numHashMap.print();

    return 0;
}
