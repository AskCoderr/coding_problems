#include <vector>
#include <algorithm>
#include <iostream>

using std::vector;
using intVi = vector<int>;

class Solution
{
public:
    double findMedianSortedArrays(intVi &nums1, intVi &nums2)
    {
        double result;
        if (nums1.size() == 0)
        {
            result = median(nums2);
        }
        else if (nums2.size() == 0)
        {
            result = median(nums1);
        }
        else
        {
            result = median(merge(nums1, nums2));
        }
        return result;
    }

private:
    intVi merge(intVi vec1, intVi vec2)
    {
        if (vec1.at(0) > vec2.at(0))
        {
            std::swap(vec1, vec2);
        }

        intVi vec;
        auto it1 = vec1.begin();
        auto it2 = vec2.begin();
        bool state = true;

        if (vec1.size() != 1)
        {
            while (it1 != vec1.end() - 1)
            {
                vec.push_back(*it1);
                if (state)
                {
                    auto temp = it1;
                    while (it2 != vec2.end())
                    {
                        if (*temp <= *it2 && *(it1 + 1) >= *it2)
                        {
                            temp = it2;
                            vec.push_back(*it2);
                            ++it2;
                        }
                        else
                        {
                            break;
                        }
                    }
                    if (it2 == vec2.end())
                    {
                        state = false;
                    }
                }
                ++it1;
            }
        }

        bool state2 = true;
        if (state)
        {
            while (it2 != vec2.end())
            {
                if (state2)
                {
                    if (*it1 < *it2)
                    {
                        vec.push_back((*it1));
                    }
                    state2 = false;
                }
                vec.push_back(*it2);
                ++it2;
            }
        }
        else
        {
            vec.push_back(*it1);
        }
        return vec;
    }

    double median(intVi vec)
    {
        if (vec.size() == 0)
        {
            return 0;
        }
        if (vec.size() % 2 == 0)
        {
            int sum = vec.at(vec.size() / 2) + vec.at((vec.size() / 2) - 1);
            return (double)sum / 2;
        }
        else
        {
            return vec.at(vec.size() / 2);
        }
    }
};

int main()
{
    intVi v1 = {1, 3, 5};
    intVi v2 = {2, 4, 6};
    Solution sol;
    double res = sol.findMedianSortedArrays(v1, v2);
    std::cout << "Median: " << res << '\n';
}

// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
// not a real solution as it does not achieve the desired O(log(m+n)) time complexity
