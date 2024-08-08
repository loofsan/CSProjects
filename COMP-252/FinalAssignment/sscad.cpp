/*
class MinHeap {

private:

    vector<T> array;

    void heapifyUp(int index) {
        while (index > 0 && array[index] < array[(index - 1) / 2]) {
            swap(array[index], array[(index - 1) / 2]);
            index = (index - 1) / 2;
        }
    }

    void heapifyDown(int index) {
        int smallest = index;
        int left = 2 * index + 1;
        int right = 2 * index + 2;

        if (left < array.size() && array[left] < array[smallest])
            smallest = left;

        if (right < array.size() && array[right] < array[smallest])
            smallest = right;

        if (smallest != index) {
            swap(array[index], array[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    MinHeap() {}

    void insert(const T& value) {
        array.push_back(value);
        heapifyUp(array.size() - 1);
    }

    T extractMin() {
        if (array.empty()) {
            cout << "Heap is empty" << endl;
        }

        T min = array[0];
        array[0] = array.back();
        array.pop_back();
        heapifyDown(0);

        return min;
    }

    void print() {
        for (const auto& element : array)
            cout << element << " ";
        cout << endl;
    }

    static void sort(vector<T>& unsorted) {
        vector<T> result;
        MinHeap<T> tmp_heap;

        for (const auto& value : unsorted)
            tmp_heap.insert(value);

        while (!tmp_heap.array.empty())
            result.push_back(tmp_heap.extractMin());

        unsorted = result;
    }
};

*/