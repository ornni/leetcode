class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        Max = max(nums)
        Min = min(nums)

        nums = [x for x in nums if x != Max]
        nums = [x for x in nums if x != Min]

        if nums:
            return nums[0]
        else:
            return -1