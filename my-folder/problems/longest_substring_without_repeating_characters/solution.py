class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        max_len = 0

        cont_chars = {}
        
        for r in range(len(s)):
            cont_chars[s[r]] = cont_chars.get(s[r], 0) + 1
            if cont_chars[s[r]] > 1:
                while cont_chars[s[r]] != 1:
                    cont_chars[s[l]] -= 1
                    l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len