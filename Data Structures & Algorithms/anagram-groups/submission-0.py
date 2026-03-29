class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagram_groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            anagram_groups[key].append(word)

        return list(anagram_groups.values())