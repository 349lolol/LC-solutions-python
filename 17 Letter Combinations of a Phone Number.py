class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def solve(i, curr):
            if i == len(digits):
                result.append(curr)
                return
            for char in letters[digits[i]]:
                solve(i+1, curr + char)

        solve(0, "")
        return result
