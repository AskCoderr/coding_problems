#include <iostream>
#include <vector>
#include <algorithm>

using std::vector, std::reverse, std::swap, std::sort, std::cout;

class Solution
{
public:
    void nextPermutation(vector<int> &nums)
    {
        int highest = nums.size() - 1;
        bool state = false;
        for (int index = nums.size() - 2; index >= 0; --index)
        {
            if (nums[index] < nums[highest])
            {
                swap(nums[index], nums[findLowest(nums, index, nums[index])]);
                state = true;
                sort(nums.begin() + index + 1, nums.end());
                break;
            }

            if (nums[highest] < nums[index])
            {
                highest = index;
            }
        }

        if (!state)
        {
            return reverse(nums.begin(), nums.end());
        }
    }

    int findLowest(vector<int> &nums, int leftLim, int lowLim)
    {
        if (leftLim == nums.size() - 2)
        {
            return nums.size() - 1;
        }
        int lowest = leftLim + 1;
        for (int i = lowest + 1; i < nums.size(); ++i)
        {
            if (nums[i] > lowLim && nums[i] < nums[lowest])
            {
                lowest = i;
            }
        }
        return lowest;
    }
};

int main() {
    Solution sol;
    vector<int> vc = {4, 7, 2, 1, 8, 5, 4};
    sol.nextPermutation(vc);
    for (int &i: vc){
        cout << i << " ";
    }
    return 0;
}

// https://leetcode.com/problems/next-permutation/description/
