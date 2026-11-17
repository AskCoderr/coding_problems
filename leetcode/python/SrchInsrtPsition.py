class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if max(nums) < target:
            return nums.index(max(nums)) + 1

        if min(nums) > target:
            return 0

        for i in nums:
            if i == target:
                return nums.index(i)
            if i > target:
                return nums.index(i)


print(Solution().searchInsert([1, 3, 5, 6], 2))
# https://leetcode.com/problems/search-insert-position/
