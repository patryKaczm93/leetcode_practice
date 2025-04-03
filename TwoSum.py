from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        results = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return print([i, j])


a = Solution()

a.twoSum([2,7,10,15], 9)