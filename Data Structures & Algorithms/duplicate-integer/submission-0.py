class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set(nums)
        if len(output) != len(nums):
            return True
        return False