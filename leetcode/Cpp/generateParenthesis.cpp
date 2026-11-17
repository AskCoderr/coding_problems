#include <iostream>
#include <vector>
#include <string>

using std::vector, std::string, std::cout;

class Solution
{
public:
    vector<string> result;

    vector<string> generateParenthesis(int n)
    {
        string str = "";
        generateParenthesisUtil(str, n, 0, 0);
        return result;
    }

private:
    void generateParenthesisUtil(string str, int n, int opened, int closed)
    {
        if (opened == n && closed == n)
        {
            result.push_back(str);
            return;
        }
        if (opened < n)
        {
            generateParenthesisUtil(str + "(", n, opened + 1, closed);
        }
        if ((opened - closed) > 0)
        {
            generateParenthesisUtil(str + ")", n, opened, closed + 1);
        }
    }
};

int main()
{
    Solution sol;
    vector<string> result = sol.generateParenthesis(5);
    for (auto i : result)
    {
        for (auto j : i)
        {
            cout << j;
        }

        cout << "   ";
    }

    return 0;
}

// https://leetcode.com/problems/generate-parentheses/description/
