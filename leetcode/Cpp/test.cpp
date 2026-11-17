#include <iostream>

int main() {
    int i;
    for (i = 0; i < 5; i++) {
        if (i == 1) {
            break;
        }
    }
    std::cout << i;
    return 0;
}