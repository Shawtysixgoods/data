#include <vector>
#include <stdexcept>
#include <iostream>

using namespace std;

template<typename T>
class Stack {
public:
    void push(const T& value) {
        data_.push_back(value);
    }

    void pop() {
        if (empty())
            throw out_of_range("Stack is empty");
        data_.pop_back();
    }

    T& top() {
        if (empty())
            throw out_of_range("Stack is empty");
        return data_.back();
    }

    bool empty() const noexcept {
        return data_.empty();
    }

    size_t size() const noexcept {
        return data_.size();
    }

private:
    vector<T> data_;
};

int main() {
    Stack<int> s;
    s.push(1);
    s.push(2);
    cout << "Top: " << s.top() << "\n";
    s.pop();
    cout << "Top: " << s.top() << "\n";
}
