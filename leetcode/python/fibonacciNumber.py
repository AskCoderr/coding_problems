class Solution:
    def fib(self, n: int) -> int:
        li = [0, 1]
        if n <= 1:
            return li[n]
        else:
            for i in range(2, n+1):
                li.append(li[i-2] + li[i-1])      
        
        return li[-1]          

print(Solution().fib(10000))
