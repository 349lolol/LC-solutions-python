class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (int)((left + right) / 2)
        while(nums[mid] != target and left < right):
            if(nums[mid] < target):
                left = mid + 1
                if(nums[left] == target):
                    return left
                mid = (int)((left + right + 1) / 2)
            else:
                right = mid - 1
                if(nums[right] == target):
                    return right
                mid = (int)((left + right + 1) / 2)
        if(nums[mid] == target):
            return mid
        return -1
