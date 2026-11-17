class Solution:
    def isPalindrome(self, x: int) -> bool:
        frwrd = str(x)
        bkwrd = frwrd[::-1]
        if frwrd == bkwrd:
            return True
        else:
            return False


print(Solution().isPalindrome(10000900001))
# https://leetcode.com/problems/palindrome-number/
