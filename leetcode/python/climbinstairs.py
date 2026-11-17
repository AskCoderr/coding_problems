class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 1
            for i in range(3, n+1):
                b = a+b
                a = b-a
            return a+b


print(Solution().climbStairs(7))

# the main logic i had to look up so gotta give credit to the internet 😁
# https://leetcode.com/problems/climbing-stairs/
