#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using std::vector, std::unordered_map;

class Solution
{
public:
    int leastInterval(vector<char> &tasks, int n)
    {
        int result = 0;
        unordered_map<char, int> count;
        vector<char> loopData;
        for (char &i : tasks)
        {
            if (count.count(i) > 0)
            {
                ++count[i];
            }
            else
            {
                count[i] = 1;
                loopData.push_back(i);
            }
        }
        
        while (loopData.size() != 0) {
            std::sort(loopData.begin(), loopData.end(), [&count](char a, char b) {
                return count[a] > count[b];
            });
            auto it = loopData.begin();
            int counter = 0;
            int initSize;
            if (loopData.size() > (n+1)) {
                initSize = n+1;
            } else {
                initSize = loopData.size();
            }
            for (int i = 0; i < initSize; i++) {
                if (--count[*it] == 0) {
                    it = loopData.erase(it);
                } else {
                    ++it;
                }
                ++counter;
                ++result;
            }
            if (loopData.size() != 0) {
                result += (n+1)-counter;
            }
        }
        return result;
    }
};

int main() {
    Solution sol;
    vector<char> data = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 2;
    int res = sol.leastInterval(data, n);
    std::cout << "Result: " << res << '\n';
    return 0;
}

// https://leetcode.com/problems/task-scheduler/description/