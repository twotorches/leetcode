from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newnums = list(set(nums))
        print(newnums)
        for i in range (len(newnums)):
            nums[i] = newnums[i]
        print(nums)    
        k = len(newnums)
        return k


sol = Solution()
print(sol.removeDuplicates([1,1,2]))