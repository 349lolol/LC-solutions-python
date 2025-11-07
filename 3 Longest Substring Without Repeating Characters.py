class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 1
        letters = {}
        if(len(s) < 2):
            return len(s)
        letters[s[0]] = 0
        for right in range(1, len(s)):
            if s[right] in letters and letters[s[right]] >= left:
                left = letters[s[right]] + 1
            letters[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest
