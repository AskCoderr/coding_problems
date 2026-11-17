#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        string temp;
        for (string i: strs) {
            temp = i;
            sort(i.begin(), i.end());
            map[i].push_back(temp);
        }

        vector<vector<string>> result;
        for (auto i: map) {
            result.push_back(i.second);
        }
        return result;
    }
};

/*
IDEA

loop through strs
    sort i
    assign i to key (sort i) in map

create array
*/