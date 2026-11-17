#include <iostream>

class Solution
{
public:
    int mySqrt(int x)
    {
        if (x == 0 || x == 1)
        {
            return x;
        }
        return mySqrtt(x, 0, (x / 2) + 1);
    }

private:
    int mySqrtt(int x, int low, long high)
    {
        if (high - low == 1)
        {
            if (high * high == x)
            {
                return high;
            }
            else
            {
                return low;
            }
        }
        long mid = (high + low) / 2;
        if (x > mid * mid)
        {
            return mySqrtt(x, mid, high);
        }
        else if (x < mid * mid)
        {
            return mySqrtt(x, low, mid);
        }
        else
        {
            return mid;
        }
    }
};

int main()
{
    Solution sol;
    std::cout << sol.mySqrt(665765575) << '\n';

    return 0;
}

// https://leetcode.com/problems/sqrtx/description/
