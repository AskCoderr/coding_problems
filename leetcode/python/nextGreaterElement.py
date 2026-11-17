class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        indexes = {}
        for i in enumerate(nums2):
            indexes[i[1]] = i[0]
            
        for j in nums1:
            flag = False
            for k in nums2[indexes[j]+1:]:
                if k > j:
                    ans.append(k)
                    flag = True
                    break
            if not flag:
                ans.append(-1)
                
        return ans
                
            
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))