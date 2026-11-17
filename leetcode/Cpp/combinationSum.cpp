#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        recrs(candidates, 0, target);
        vector<vector<int>> result;
        vector<int> temp;
        for (auto &i : sequences)
        {
            for (auto &j : i)
            {
                temp.push_back(j);
            }
            result.push_back(temp);
            temp.clear();
        }
        return result;
    }

private:
    multiset<int> sequence;
    vector<multiset<int>> sequences;

    void recrs(vector<int> &candidates, int curr, int target)
    {
        for (int elem : candidates)
        {
            curr += elem;
            sequence.emplace(elem);
            if (curr == target)
            {
                if (find(sequences.begin(), sequences.end(), sequence) == sequences.end())
                {
                    sequences.push_back(sequence);̥̥
                }
            }
            else if (curr < target)
            {
                recrs(candidates, curr, target);
            }
            sequence.erase(sequence.find(elem));
            curr -= elem;
        }
    }
};

int main()
{
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    Solution sol;
    vector<vector<int>> result = sol.combinationSum(candidates, target);
    for (auto i : result)
    {
        for (auto j : i)
        {
            cout << j << ' ';
        }
        cout << endl;
    }
    return 0;
}

/*
---- 1st breakdown ----
- take the array pass it tot he recursive function
- the recursive function will loop through the elements of the array, add it to the current sequence, add to the current total, and check if the current total = target, if yes then do necessaary
else if total > target, ignore


---- 2nd breakdown ----
- sequence(vector<int>)
- sequences(vector<vector<int>>)
recrs(arr, curr, total)

recrs {
    - loop through each elem of arr
    - if equal to target
    -   add sequence to sequences
    - else if greater than target
    -   continue
    - else
    -   add to sequence
    -   recrs(arr, curr+elem, total)
    -   remove from sequence

}

*/

// https://leetcode.com/problems/combination-sum/description/
// very inefficient but works