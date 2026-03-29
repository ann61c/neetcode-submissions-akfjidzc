class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        def dfs(i, combination):
            if i == len(digits):
                if not combination:
                    return
                res.append(combination)
                return
            if i > len(digits):
                return
            digit = digits[i]
            if digit in digit_map:
                for char in digit_map[digit]:
                    new_combination = combination + char
                    dfs(i+1, new_combination)
                    new_combination = combination
        dfs(0, "")
        return res
