#include <vector>
#include <cmath>
#include <iostream>

using std::vector;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        return recrs(height, 0, height.size() - 1, std::min(height[0], height[height.size() - 1]) * height.size() - 1);
    }

private:
    int recrs(vector<int> &height, int l, int r, int currArea)
    {
        // base condition - if r - l == 1, return abs(r-l)
        // check which side is smaller
        // if inc and still smaller inc
        // if inc and greater -
        //      if area greater inc
        //      else recurse and return max (current, recurse)
        // if two side equal -
        //      if (r-l) <= 2 -
        //          return current
        //      recurse with one inc on each side, return max (current, recurse)

        if ((r - l) == 1)
        {
            return std::min(height[r], height[l]);
        }
        while ((r - l) > 1)
        {
            if (height[r] < height[l])
            {
                if (height[r - 1] < height[l])
                {
                    --r;
                }
                else if (height[r - 1] > height[l])
                {
                    if ((height[l] * (r - l)) >= currArea)
                    {
                        --r;
                        currArea = height[l] * (r - l);
                    }
                    else
                    {
                        int temp = recrs(height, l, r - 1, (r - l) * height[l]);
                        return std::max(temp, currArea);
                    }
                }
            }
            else if (height[r] > height[l])
            {
                if (height[l + 1] < height[r])
                {
                    ++l;
                }
                else if (height[l + 1] > height[r])
                {
                    if ((height[r] * (r - l)) >= currArea)
                    {
                        ++l;
                        currArea = height[r] * (r - l);
                    }
                    else
                    {
                        int temp = recrs(height, l + 1, r, (r - l) * height[r]);
                        return std::max(temp, currArea);
                    }
                }
            }
            else
            {
                if ((r - l) <= 2)
                {
                    return currArea;
                }
                int temp = recrs(height, l + 1, r - 1, std::min(height[l + 1], height[r - 1]) * ((r - 1) - (l + 1)));
                return std::max(currArea, temp);
            }
        }

        if (std::min(height[r], height[l]) > currArea)
        {
            return std::min(height[r], height[l]);
        }
        return 0;
    }
};

int main()
{
    Solution sol;
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int maxArea = sol.maxArea(height);
    std::cout << maxArea << '\n';
    return 0;
}