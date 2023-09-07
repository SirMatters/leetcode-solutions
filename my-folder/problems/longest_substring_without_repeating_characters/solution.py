class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        letter_cache = {}

        left = 0
        pos = 0

        while pos < len(s):
            letter = s[pos]
            if letter not in letter_cache or letter_cache[letter] < left:
                letter_cache[letter] = pos
                max_len = max(max_len, pos - left + 1)
            else:
                max_len = max(max_len, pos - left)
                left = letter_cache[letter] + 1
                letter_cache[letter] = pos

            pos += 1

        return max_len