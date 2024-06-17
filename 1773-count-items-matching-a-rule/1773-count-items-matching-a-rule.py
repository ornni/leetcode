class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0

        if ruleKey == 'type':
            for i in items:
                if i[0] == ruleValue:
                    answer += 1
        
        elif ruleKey == 'color':
            for i in items:
                if i[1] == ruleValue:
                    answer += 1
        
        elif ruleKey == 'name':
            for i in items:
                if i[2] == ruleValue:
                    answer += 1
        
        return answer
