#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int currentIndex = 0;

    int firstMissingPositive(vector<int>& nums) {
        while (true) {
            nextCheck(nums);
            if (currentIndex >= nums.size()) {
                break;
            }
            swap(nums[currentIndex], nums[nums[currentIndex]-1]);
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }
        return nums.size()+1;
    }

private:
    void nextCheck(vector<int>& nums) {
        while (currentIndex < nums.size() && (nums[currentIndex] < 1 || nums[currentIndex] > nums.size() || nums[currentIndex] == currentIndex+1)) {
            currentIndex++;
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1};
    cout << "Answer: " << sol.firstMissingPositive(nums);
    return 1;
}

// https://leetcode.com/problems/first-missing-positive/description/

/*
currentIndex
nextCheck() {
    while nums[currentIndex] < 1 or nums[currentIndex] > nums.length {
        currentIndex++
    }
}

swap() {
    swap two elements in the vector
}

while true {
    if currentIndex >= nums.length {
        break
    }

    swap()

    nextCheck()
}

loop through nums and check for first missing adjacent integer starting from 1
*/