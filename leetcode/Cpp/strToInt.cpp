#include <string>
#include <regex>
#include <iostream>
#include <climits>

using std::string;

class Solution {
public:
    int myAtoi(string s) {
        int result = 0;
        std::regex pattern1("\\d");
        std::regex pattern2("^\\s*([-+]?)0*(\\d+).*$");
        std::smatch m;
        
        if (std::regex_search(s, pattern1)) {
            if (std::regex_match(s, m, pattern2)) {
                if (m[1] == "-") {
                    if (m[2] == "2147483648") {
                        return INT_MIN;
                    }
                    std::string temp = std::to_string(INT_MAX);
                    temp[temp.size() - 1] = '9';
                    if (greaterNumStr(temp, m[2])) {
                        result = -(std::stoi(m[2]));
                    } else {
                        result = INT_MIN;
                    }
                } else {
                    std::string temp = std::to_string(INT_MAX);
                    temp[temp.size() - 1] = '8';
                    if (greaterNumStr(temp, m[2])) {
                        result = std::stoi(m[2]);
                    } else {
                        result = INT_MAX;
                    }
                }
            }
        }
        return result;
    }

private:
    bool greaterNumStr(std::string a, std::string b) {
        if (a.size() > b.size()) {
            return true;
        } else if (a.size() < b.size()) {
            return false;
        } else {
            return a > b;
        }
    }
};


int main() {
    Solution sol;
    int result = sol.myAtoi("2147483646");
    std::cout << result << '\n';
    return 0;
}