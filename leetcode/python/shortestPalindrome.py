class Solution:
    def shortestPalindrome(self, s: str) -> str:
        final_middle = 0
        temp = 0
        for i in range(1, len(s)):
            middle = i//2
            if (i%2 == 0 and s[: middle] == s[2*middle:middle:-1]) or (i%2 != 0 and s[: middle+1] == s[(2*middle)+1:middle:-1]):
                final_middle = middle
                temp = i%2
                
        return s[-1: (2*final_middle)+temp: -1] + s

print(Solution().shortestPalindrome("aacecaaa"))
# https://leetcode.com/problems/shortest-palindrome/description/
