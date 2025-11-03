class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]] 
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

#floyds cycle detection: at first meeting, slow travels p + C - x, fast travels p + C + C - x
#slow * 2 = fast, so we get p - x = 0, so p = x
#this way, by running a slow2 to meet slow, they intersect as slow travels exactly 1 cycle in the loop
