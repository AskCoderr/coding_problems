class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        dict = {}
        i = 0
        while i < length:
            if s[i] not in dict.keys():
                if t[i] in dict.values():
                    return False
                else:
                    dict[s[i]] = t[i]
            elif dict[s[i]] != t[i]:
                return False  
            i += 1
        
        return True
            
    
print(Solution().isIsomorphic("paper", "title"))
