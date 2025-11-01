class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [0] * len(nums)
        last_start = 0
        last_reach = 0
        count = 0
        while(last_reach < len(nums) - 1):
            start = last_start
            reach = last_reach
            while(start <= last_reach):
                reach = max(reach, start + nums[start])
                start = start + 1
            last_reach = reach
            last_start = start
            count = count + 1
        return count
