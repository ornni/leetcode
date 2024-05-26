class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = 0
        
        for i in range(len(nums)):
            for j in nums[i+1:]:
                Max = max(Max, (nums[i]-1)*(j-1))
        
        return Max