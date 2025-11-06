class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        test = "qwertyuiopasdfghjklzxcvbnm1234567890"
        while(left < right):
            while(left < right and s[left] not in test):
                left = left + 1
            while(left < right and s[right] not in test):
                right = right - 1
            if(left < right and s[left] != s[right]):
                return False
            left = left + 1
            right = right - 1
        return True
            
