class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}      
        start = 0
        longest = 0

        for curr, ch in enumerate(s):
            if ch in letters and letters[ch] >= start:
                start = letters[ch] + 1
            letters[ch] = curr
            longest = max(longest, curr - start + 1)

        return longest