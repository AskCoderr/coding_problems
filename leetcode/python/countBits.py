class Solution:
    def countBits(self, n: int) -> list[int]:
        li = []
        for i in range(n+1):
            bina = bin(i)
            ones = bina[2:].count("1")
            li.append(ones)
        return li 
    
print(Solution().countBits(5))

# https://leetcode.com/problems/counting-bits/