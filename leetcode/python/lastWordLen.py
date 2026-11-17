class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = 0
        for i in s[::-1]:
            if i == " " and a != 0:
                break
            elif i != " ":
                a += 1
        return a


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))

# https://leetcode.com/problems/length-of-last-word/
