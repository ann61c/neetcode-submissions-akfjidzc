class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            char_count[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            char_count[index] -= 1

        for count in char_count:
            if count != 0:
                return False

        return True
