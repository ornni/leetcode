import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in nums:
            if i not in count_dict.keys():
                count_dict[i] = 1
            else:
                count_dict[i] += 1

        largest_keys = heapq.nlargest(k, count_dict, key=count_dict.get)
        return largest_keys