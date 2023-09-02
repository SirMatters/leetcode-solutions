class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq_len = 0

        for num in num_set:
            len = 1

            if num - 1 in num_set:
                continue

            while num + 1 in num_set:
                len += 1
                num += 1

            max_seq_len = max(max_seq_len, len)
        
        return max_seq_len
            