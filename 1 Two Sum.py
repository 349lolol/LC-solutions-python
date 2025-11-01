class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid = defaultdict(int)
        valid[target - nums[0]] = 0
        i = 1
        while(nums[i] not in valid):
            valid[(target - nums[i])] = i
            i = i + 1
        return [valid[nums[i]], i]
