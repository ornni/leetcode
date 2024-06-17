class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [0] * len(pref)
        answer[0] = pref[0]

        for i in range(1, len(pref)):
            answer[i] = pref[i-1] ^ pref[i]
        
        return answer