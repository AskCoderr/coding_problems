#include <string>


using std::string;

class Solution {
public:
    string decodeDNA(int n, const string &s) {
        // write your code here 
        string result;
        
        for (int i = 0; i < s.size(); i += 2) {
            if (s.substr(i, 2) == "00") {
                result.push_back('A');
            } else if (s.substr(i, 2) == "01") {
                result.push_back('T');
            } else if (s.substr(i, 2) == "10") {
                result.push_back('C');
            } else {
                result.push_back('G');
            }
        }

        return result;
    }
};
