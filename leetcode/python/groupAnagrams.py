class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictionary = {}
        for i in strs:
            x = sorted(i)
            temp = ""
            for j in x:
                temp += j
                
            if temp in dictionary.keys():
                dictionary[temp].append(i)
            else:
                dictionary[temp] = [i]
                
        li = []
        for i in dictionary.keys():
            li.append(dictionary[i])
        
        return li
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=array
