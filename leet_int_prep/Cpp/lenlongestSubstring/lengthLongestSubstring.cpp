#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (size(s) == 0 or size(s) == 1) {
            return size(s);
        }

        auto left_pointer = s.begin(), right_pointer = left_pointer+1;
        int max_len = 1, len = 1;
        vector<char> data = {s[0]};

        while (right_pointer != s.end()) {
            auto slice_pointer = find(data.begin(), data.end(), *right_pointer);
            if (slice_pointer != data.end()) {
                data.erase(data.begin(), slice_pointer+1);
                max_len = max_len < len ? len : max_len;
                len = size(data);
            }
            data.push_back(*right_pointer);
            len++;
            right_pointer++;
        }
        max_len = max_len < len ? len : max_len;
        return max_len;
    }
};

/*
PLAN
if len 0 or 1: return size(s)

left_pointer = 0, right_pointer = 1, max_len = 1, len = 1, data = [s[0]]

while right_pointer != end:
    index = find(right_pointer value)
    if index
        data = data[index+1:]
        max_len = max_len < len ? len : max_len
        len = size(data)
    add right_pointer value to data array
    increment len by 1
    right_pointer++

max_len = max_len < len ? len : max_len
return max_len
        */

// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/