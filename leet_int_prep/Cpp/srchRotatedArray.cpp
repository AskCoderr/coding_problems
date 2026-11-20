#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums[0] == target) return 0;
        bool inRotated = target < nums[0] ? true : false;
        int tempIndex = 0, top = size(nums) - 1, bottom = 0;
        if (!inRotated) {
            while (top-bottom > 1) {
                if (target == nums[bottom]) return bottom;
                else if (target < nums[bottom] || (target > nums[bottom] && nums[bottom] < nums[0])) {
                    top = bottom;
                    bottom = (tempIndex + top) / 2;
                } else if (target > nums[bottom]) {
                    tempIndex = bottom;
                    bottom = (bottom + top) / 2;
                }
            }
            if (nums[top] == target) return top;
            if (nums[bottom] == target) return bottom;
        } else {
            while (top-bottom >= 1) {
                cout << bottom << ' '<< top << '\n';
                if (target == nums[top]) return top;
                else if (target > nums[top] || (target < nums[top]  && nums[top] >= nums[0])) {
                    bottom = top;
                    top = (tempIndex + bottom) / 2;
                } else if (target < nums[top]) {
                    tempIndex = top;
                    top = (bottom + top) / 2;
                }
            }
        }

        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {4,5,6,7,8,1,2,3};
    cout << sol.search(nums, 8); 
    return 0;
}

/*
IDEA

- check if it belongs to rotated or unrotated group, by comparing to the
    first element of the array

- if in rotated, top pointer at end and bottom pointed at start of the array and
    compare the top pointer always to the target variable

- else, do same but compare the bottom pointer

- now during comparison we should keep track of the previous node we jumped from,
    cause in case if the value newly compared asks to, then we have to move back

- if greater than bottom pointer move the bottom pointer, else go back to
    previous node and move the bottom pointer again after updating top

- if is target return the index and be happy

- if (top-bottom) == 1: then return -1

ALGORITHM

if array[0] == target return 0
inRotated = target < array[0] ? true : false
tempIndex = 0

if inRotated:
    top = len(array) - 1
    bottom = 0

    while (top-bottom > 1) {
        if target == array[bottom] return bottom
        elif target > bottom
            tempIndex = bottom
            bottom = (bottom + top) / 2
        elif target < bottom
            top = bottom
            bottom = (tempIndex + top) / 2
    }
else:
    top = len(array) - 1
    bottom = 0

    while (top-bottom > 1) {
        if target == array[top] return top
        elif target > top
            bottom = top
            top = (tempIndex + bottom) / 2
        elif target < top
            tempIndex = top
            top = (bottom + top) / 2
    }

return -1;

*/

// https://leetcode.com/problems/search-in-rotated-sorted-array/description/