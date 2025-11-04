class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[0, temperatures[0]]]
        days = [0] * len(temperatures)
        
        for i in range(1, len(temperatures)):
            while(len(stack) > 0 and 
            stack[-1][1] < temperatures[i]):
                days[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, temperatures[i]])
        return days

