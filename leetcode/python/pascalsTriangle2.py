class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        li = [1]
        previous_row = self.getRow(rowIndex-1)
        length = len(previous_row)
        x = 0
        while x != length - 1:
            li.append(previous_row[x] + previous_row[x+1])
            x += 1
        li.append(1)
        
        return li
    
print(Solution().getRow(35))

"""
pascal's triangles uses the mathematical concept of binomial coefficients,
implementing this idea, this problem can be solved in O(n) time complexity.
"""
# https://leetcode.com/problems/pascals-triangle-ii/description/
