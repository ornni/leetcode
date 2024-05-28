class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] + j < target:
                    answer += 1
        return answer