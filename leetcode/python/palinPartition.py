class Solution:
    def partition(self, s: str) -> list[list[str]]:
        di = {}
        li = []
        for i in range(len(s)):
            di[i] = []
            li.append("")
        
        for i in range(1, len(s)+1):
            for k in range(i):
                li[k] += s[i-1]
                if li[k] == li[k][::-1]:
                    di[k].append(i-1)
                    
        li2 = []
        temp = []
        length = len(di)
        def recrs(t):
            for i in di[t]:
                temp.append(s[t:i+1])
                if i == length-1:
                    li2.append([i for i in temp])
                    temp.pop()
                    break
                else:
                    recrs(i+1)
                temp.pop()
        recrs(0)
        
        return li2
                    
        
print(Solution().partition("racecar"))

# https://leetcode.com/problems/palindrome-partitioning/description/
