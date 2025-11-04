class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1 for _ in range(len(nums))] #size
        #start off with the last digit, crawl backwards
        for i in range (len(nums)-2, -1, -1):
            longest_i = len(nums)-1 #longest by default
            for j in range (len(nums)-1, i, -1): #test each prev subsequence with curr
                if(lengths[j] >= lengths[longest_i] 
                    and nums[j] > nums[i]): #i = 1, j = 4
                        longest_i = j
            if(nums[i] < nums[longest_i]):
                lengths[i] = 1 + lengths[longest_i]
        
        longest = 0
        for i in lengths:
            if longest < i:
                longest = i
        return longest
