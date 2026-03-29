class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        output = 0
        left = 0 
        for right in range(len(s)):
            while s[right] in curr:
                    curr.remove(s[left])
                    left+=1
            
            curr.add(s[right])

            output = max(output, right - left + 1)
        return output
        

'''
This has error. need to remove the if-else statement, because 
it is actually removing the character from the curr set that is not 
present. 
which can happen when left moves forward but doesn't correspond 
to a character currently in the set 
(for instance, after duplicates are removed).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        output = 0
        left = 0 
        for right in range(len(s)):
            if s[right] not in curr:
                curr.add(s[right])  # Add the character, not the index
            else:
                while s[right] in curr:
                    curr.remove(s[left])  # Remove from the left to shrink the window
                    left += 1

            output = max(output, right - left + 1)  # Update the maximum length
        return output
'''