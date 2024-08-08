#include <iostream>
#include <vector>
#include <functional> 

using namespace std;

template<class KeyType, class ValueType>
class HashMap {
private:
    struct HashTableEntry {
        KeyType key;
        ValueType value;
        bool occupied; // To track whether a bin is occupied or not
    };

    vector<HashTableEntry> bins;
    int num_keys;
    int size; // Current size of the hash table
    const double load_factor_threshold = 0.75;

    void resize(int new_size) {
        vector<HashTableEntry> new_bins(new_size);
        for (const auto& entry : bins) {
            if (entry.occupied) {
                int index = hash(entry.key) % new_size;
                while (new_bins[index].occupied) {
                    index = (index + 1) % new_size; // Linear probing
                }
                new_bins[index] = entry;
            }
        }
        bins = move(new_bins);
        size = new_size;
    }

    void check_load_factor() {
        if (static_cast<double>(num_keys) / size > load_factor_threshold) {
            int new_size = size * 2;
            resize(new_size);
        }
    }

public:
    HashMap() : num_keys(0), size(8) { // Initial size of 8
        bins.resize(size);
    }

    void insert(const KeyType& key, const ValueType& value) {
        check_load_factor();

        int index = hash(key) % size;
        while (bins[index].occupied && bins[index].key != key) {
            index = (index + 1) % size; // Linear probing
        }

        if (!bins[index].occupied) {
            bins[index].key = key;
            bins[index].value = value;
            bins[index].occupied = true;
            num_keys++;
        } else {
            // Key already exists, update the value
            bins[index].value = value;
        }
    }

    ValueType* find(const KeyType& key) {
        int index = hash(key) % size;
        int start_index = index;

        while (bins[index].occupied) {
            if (bins[index].key == key) {
                return &bins[index].value;
            }
            index = (index + 1) % size; // Linear probing
            if (index == start_index) {
                // Reached back to the starting point, key not found
                return nullptr;
            }
        }
        return nullptr;
    }

    void print() const {
        for (const auto& entry : bins) {
            if (entry.occupied) {
                cout << "Key: " << entry.key << ", Value: " << entry.value << endl;
            }
        }
    }

private:
    hash<KeyType> hash;
};

int main() {
    HashMap<string, int> hash_map;
    hash_map.insert("Morning Shock", 1);
    hash_map.insert("Liquid Alarm Clock", 2);
    hash_map.insert("Pure Caffeine", 3);
    hash_map.insert("Morning Zap", 4);

    // Finding and updating value
    int* value_ptr = hash_map.find("Morning Zap");
    if (value_ptr) {
        *value_ptr = 5;
    }

    hash_map.print();

    return 0;
}
