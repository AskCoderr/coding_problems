#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        if (size(s) == 0 or size(s) == 1)
        {
            return size(s);
        }

        unordered_map<int, int> map = { {s[0], 0} };
        int left = 0, right = 1, len = 1, max_len = 1;

        while (right != size(s))
        {
            if (map.count(s[right]))
            {   
                int i = left;
                left = map[s[right]] + 1;
                for (i; i <= map[s[right]]; i++) {
                    map.erase(s[i]);
                }
                max_len = max_len < len ? len : max_len;
                len = right - left;
            }
            map[s[right]] = right;
            len++;
            right++;
        }
        max_len = max_len < len ? len : max_len;
        return max_len;
    }
};

/*
PLAN

if len 0 or 1: return size(s)

map = instantiate map (int, int) with first char included
left = 0, right = 1, len = 1, max_len = 1

while right != size(s) {
    if right in hash map:
        update left to +1 of the index in hash map
        max_len = max_len < len ? len : max_len
        len = right - left;
    update index for char in hash map
    len++
    right++
}
max_len = max_len < len ? len : max_len
return max_len
*/

// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
