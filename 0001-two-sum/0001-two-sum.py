class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for n in range(i+1, len(nums)):
                if num + nums[n] == target:
                    return [i, n]