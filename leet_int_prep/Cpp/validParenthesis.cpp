#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        char opening_brackets[] = {'(', '{', '['};
        unordered_map<char, char> map = { {')', '('}, {'}', '{'}, {']', '['} };
        for (char i: s) {
            if (find(opening_brackets, opening_brackets+3, i) != opening_brackets+3) {
                stk.push(i);
            } else {
                if (map[i] != stk.top()) {
                    return false;
                } else {
                    stk.pop();
                }
            }
        }
        return stk.empty();
    }
};