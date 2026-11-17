class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        li = []
        for k in range(1, numRows+1):
            temp = []
            for i in range(1, k+1):
                if i in [1, k]:
                    temp.append(1)
                else:
                    temp.append(li[k-2][i-2] + li[k-2][i-1])
            li.append(temp)
                
        return li
    
print(Solution().generate(5))

# expected output -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# https://leetcode.com/problems/pascals-triangle/