// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         sort(nums.begin(), nums.end());

//         for (int i = 0; i < nums.size() - 1; i++) {
//             for (int j = i + 1; j < nums.size(); j++) {
//                 if (nums[j] > target - nums[i]) {
//                     break;
//                 }
//                 if (nums[i] + nums[j] == target) {
//                     return {i, j};
//                 }
//             }
//         }
//         return {-1, -1};
//     }
// };

// /*
// BRUTE FORCE

//     outer loop (i) - (from 0 to n-1)
//         inner loop (j) - (from i+1 to n-1)
//             if (i + j == target):
//                 return [i, j]

// PLAN

//     - we can ignore numbers greater than target
//     - we can ignore numbers greater than target - i
//     - so seems like we have to sort it

// OPTIMIZED
//     - sort
//     - for i stop when point > target (redundant cause there will always be a solution)
//     - for j stop when point > target - i

// HOW TO SELECT APPROPRIATE END POINT
//     - while going through the array just stop once the element is greater than target - i
// */



// AFTER READ SOLUTION

/*
- loop through nums (i)
-   if element's complement present in map
-       return
-   map[element] = i
- 
*/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            if (map.find(target - nums[i]) != map.end()) {
                return {i, map[target - nums[i]]};
            }
            map[nums[i]] = i;
        }
        return {-1, -1};
    }
};