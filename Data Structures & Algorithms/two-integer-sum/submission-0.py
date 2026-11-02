class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b = i + 1
            while b < len(nums):
                if nums[i] + nums[b] == target:
                    return [i, b]
                b += 1
                