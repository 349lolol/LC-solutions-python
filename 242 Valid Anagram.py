class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for i in range(len(s)):
            letters[s[i]] = letters[s[i]] + 1
        for i in range(len(t)):
            letters[t[i]] = letters[t[i]] - 1
        for i in letters:
            if(letters[i] != 0):
                return False
        return True
