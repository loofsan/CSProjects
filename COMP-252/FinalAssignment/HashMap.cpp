#include <iostream>
#include <vector>
#include <list>
#include <utility>
#include <functional>

using namespace std;

template<typename KeyType, typename ValueType>
class HashMap {
private:
    struct ListNode {
        KeyType key;
        ValueType value;
        ListNode* next;
        
        ListNode(const KeyType& k, const ValueType& v) : key(k), value(v), next(nullptr) {}
    };

    std::vector<std::list<ListNode*>> bins;
    size_t size;
    float load_factor_threshold;
    size_t capacity;

    void resize(size_t new_capacity) {
        std::vector<std::list<ListNode*>> new_bins(new_capacity);
        for (auto& bin : bins) {
            for (auto node : bin) {
                size_t index = std::hash<KeyType>{}(node->key) % new_capacity;
                new_bins[index].push_back(node);
            }
        }
        bins = std::move(new_bins);
        capacity = new_capacity;
    }

    void check_load_factor() {
        if (static_cast<float>(size) / capacity > load_factor_threshold) {
            resize(capacity * 2);
        }
    }

public:
    explicit HashMap(size_t initial_capacity = 8, float load_factor = 0.75)
        : bins(initial_capacity), size(0), load_factor_threshold(load_factor), capacity(initial_capacity) {}

    ~HashMap() {
        clear();
    }

    void insert(const KeyType& key, const ValueType& value) {
        check_load_factor();
        size_t index = std::hash<KeyType>{}(key) % capacity;
        for (auto node : bins[index]) {
            if (node->key == key) {
                node->value = value;
                return;
            }
        }
        ListNode* new_node = new ListNode(key, value);
        bins[index].push_back(new_node);
        size++;
    }

    ValueType* find(const KeyType& key) {
        size_t index = std::hash<KeyType>{}(key) % capacity;
        for (auto node : bins[index]) {
            if (node->key == key) {
                return &node->value;
            }
        }
        return nullptr;
    }

    void erase(const KeyType& key) {
        size_t index = std::hash<KeyType>{}(key) % capacity;
        auto& bin = bins[index];
        auto it = bin.begin();
        ListNode* last = nullptr;
        while (it != bin.end()) {
            if ((*it)->key == key) {
                delete *it;
                bin.erase(it);
                size--;
                return;
            }
            last = *it;
            ++it;
        }
    }

    void swap(HashMap& other) {
        bins.swap(other.bins);
        std::swap(size, other.size);
        std::swap(load_factor_threshold, other.load_factor_threshold);
        std::swap(capacity, other.capacity);
    }

    void print() {
        for (size_t i = 0; i < capacity; ++i) {
            std::cout << "Bin " << i << ": ";
            for (auto node : bins[i]) {
                std::cout << "{" << node->key << ": " << node->value << "} ";
            }
            std::cout << std::endl;
        }
    }

    void clear() {
        for (auto& bin : bins) {
            for (auto node : bin) {
                delete node;
            }
            bin.clear();
        }
        size = 0;
    }
};

int main() {
    // HashMap with string keys and int values
    HashMap<std::string, int> string_map;
    string_map.insert("one", 1);
    string_map.insert("two", 2);
    string_map.insert("three", 3);

    std::cout << "String Map:" << std::endl;
    string_map.print();

    std::cout << "\nFinding 'two': ";
    int* val_str = string_map.find("two");
    if (val_str) {
        std::cout << *val_str << std::endl;
    } else {
        std::cout << "Not found" << std::endl;
    }

    string_map.erase("two");
    std::cout << "\nMap after erasing 'two':" << std::endl;
    string_map.print();


    // HashMap with int keys and string values
    HashMap<int, std::string> int_map;
    int_map.insert(1, "apple");
    int_map.insert(2, "banana");
    int_map.insert(3, "orange");

    std::cout << "\n\nInteger Map:" << std::endl;
    int_map.print();

    std::cout << "\nFinding value for key '2': ";
    std::string* val_int = int_map.find(2);
    if (val_int) {
        std::cout << *val_int << std::endl;
    } else {
        std::cout << "Not found" << std::endl;
    }

    int_map.erase(2);
    std::cout << "\nMap after erasing key '2':" << std::endl;
    int_map.print();

    return 0;
}