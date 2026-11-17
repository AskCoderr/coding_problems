class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        def duplicates_in_string(string):
            for i in string:
                if string.count(i) != 1:
                    return True
            return False

        status = "start"  # start, checking, expanding, end
        p = 0
        q = 2
        while True:
            if status == "start":
                if len(s) == 0:
                    return 0
                if len(s) == 1:
                    return 1
                else:
                    status = "expanding"

            if status == "checking":
                while duplicates_in_string(s[p:q]):
                    p += 1
                    q += 1

                    if q > len(s):
                        status = "end"
                        p -= 1
                        q -= 1
                        break
                if not duplicates_in_string(s[p:q]):
                    status = "expanding"
                if q+1 > len(s):
                    q -= 1

            if status == "expanding":
                if duplicates_in_string(s[p:q]):
                    status = "checking"
                else:
                    q += 1
                    if q > len(s):
                        status = "end"
                        q -= 1

            if status == "end":
                return q - p
            continue


print(Solution().lengthOfLongestSubstring("thecoderboy"))

'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
