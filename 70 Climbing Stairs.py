class Solution:
    def climbStairs(self, n: int) -> int:
        if(n < 3):
            return n
        poss = [0] * n
        poss[0] = 1
        poss[1] = 2
        for i in range(2, n):
            poss[i] = poss[i-1] + poss[i-2]
        return poss[n-1]
