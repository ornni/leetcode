class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        output = 0

        for i in range(len(prices)):
            output = prices[i]
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    output = prices[i] - prices[j]
                    break
            answer.append(output)

        return answer