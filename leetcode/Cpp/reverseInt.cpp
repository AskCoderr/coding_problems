#include <iostream>

class Solution {
public:
    int reverse(int x) {
        // find out if the number if negative or positive and get the according limit, if negative change the sign and put it back at the last
        // use mod, floor to extract the digit and mul, add to append it
        // at the last add operation, do the check condition for the limit, if yes return 0 else append and return new num
        // check edge cases (smallest number)

        if (x == -2147483648) {
            return 0;
        }

        int result = 0;
        bool negative;

        if (x >= 0) {
            negative = false;
        } else {
            x *= -1;
            negative = true;
        }

        int temp;
        while (x != 0) {
            if (x / 10 == 0) {
                if (negative) {
                    if (result > 214748364 || (x == 9 && result == 214748364)) {
                        return 0;
                    }
                } else {
                    if (result > 214748364 || (x >= 8 && result == 214748364)) {
                        return 0;
                    }
                }
            }
            temp = x % 10;
            x /= 10;
            result *= 10;
            result += temp;
        }

        if (negative) {
            result *= -1;
        }

        return result;
    }
};

int main() {
    Solution sol;
    int reversed = sol.reverse(-122987433);
    std::cout << reversed << '\n';
    return 0;
}

// https://leetcode.com/problems/reverse-integer/description/
