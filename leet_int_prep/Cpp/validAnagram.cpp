#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int i: nums) {
            if (mp.count(i)) {
                return true;
            } else {
                mp[i] = 1;
            }
        }
        return false;
    }
};

/*
for i in nums
    if i in map
        return True
return False        
*/