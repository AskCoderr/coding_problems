#include <iostream>
#include <unordered_map>

using stor = std::unordered_map<int, std::unordered_map<bool, std::unordered_map<int, int>>>;

class Solution
{
public:
    int zigZagArrays(int n, int l, int r)
    {
        // we have int total_possibilities
        // we loop through range [l, r] we call helper function with level 1 values for each value in level 0 (excluding the same value)
        // we have a helper function with base case if temp == l return 1
        // in helper function we have two ifs for inc and not inc, we will have a loop in each ifs for each value of loop
        //      we check if perumutations already known else recurse with inc = not inc,
        // handle edge cases

        if (n == 1)
        {
            return r - l;
        }

        for (int i = l; i <= r; ++i)
        {
            for (int j = l; j <= r; ++j)
            {
                if (i == j)
                {
                    continue;
                }
                else if (i > j)
                {
                    total_possibilites = (total_possibilites + recrs(j, n, l, r, 1, false)) % 1000000007;
                }
                else
                {
                    total_possibilites = (total_possibilites + recrs(j, n, l, r, 1, true)) % 1000000007;
                }
            }
        }

        return total_possibilites;
    }

private:
    stor data;
    long long total_possibilites = 0;

    int recrs(int val, int n, int l, int r, int level, bool inc)
    {
        long long possibilities = 0;
        if (level + 1 == n)
        {
            return 1;
        }

        if (inc)
        {
            for (int i = val - 1; i >= l; --i)
            {
                if (data[level + 1][false][i])
                {
                    possibilities = (possibilities + data[level + 1][false][i]) % 1000000007;
                }
                else
                {
                    possibilities = (possibilities + recrs(i, n, l, r, level + 1, false)) % 1000000007;
                }
            }
        }
        else
        {
            for (int j = val + 1; j <= r; ++j)
            {
                if (data[level + 1][true][j])
                {
                    possibilities = (possibilities + data[level + 1][true][j]) % 1000000007;
                }
                else
                {
                    possibilities = (possibilities + recrs(j, n, l, r, level + 1, true)) % 1000000007;
                }
            }
        }

        if (!data[level][inc][val])
        {
            data[level][inc][val] = possibilities;
        }
        return possibilities;
    }
};

int main()
{
    Solution sol;
    int total = sol.zigZagArrays(21, 8, 270);
    std::cout << total << '\n';
    return 0;
}
// clear doubt whether same loop variable can be reused
// two problems -> checking of existence of value in stor due to modulo, high time complexity