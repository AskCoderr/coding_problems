class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        netSum = 0
        sums = []
        for i in nums:
            netSum += i
            sums.append(netSum)
        highest = sums[0]
        lowest = 0
        for i in sums[1:]:
            if highest - lowest < 0:
                if highest-i < lowest-highest:
                    lowest = highest
                    highest = i
                else:
                    lowest -= highest-i
                    highest = i
            
            elif i > highest:
                highest = i
                
            elif i < lowest:
                highest -= lowest - i
                lowest = i
        
        return highest - lowest


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# expected output is 6
# https://leetcode.com/problems/maximum-subarray/description/

"""
suboptimal solution:-
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        length = len(nums)
        highest = float("-inf")
        for i in range(1, length+1):
            j = 0
            while i+j <= length:
                temp = nums[j:j+i]
                summ = sum(temp)
                if summ > highest:
                    highest = summ
                j += 1
        return highest
"""