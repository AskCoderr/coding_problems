#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector, std::unordered_map;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int k = 0;
        unordered_map<int, int> mp;
        for (auto it = nums.begin(); it != nums.end();)
        {
            if (mp.count(*it))
            {
                it = nums.erase(it);
            }
            else
            {
                mp[*it] = 1;
                ++k;
                ++it;
            }
        }

        return k;
    }
};

int main()
{
    vector<int> nums = {1, 2, 2, 3, 4, 4, 4, 5};

    Solution sol;
    int k = sol.removeDuplicates(nums);

    std::cout << "k = " << k << "\n";
    std::cout << "nums after removal: ";
    for (int x : nums)
        std::cout << x << " ";

    return 0;
}

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
