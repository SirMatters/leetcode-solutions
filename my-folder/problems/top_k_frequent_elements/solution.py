class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        freq_baskets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        for val, freq in num_dict.items():
            freq_baskets[freq].append(val)

        result = []
        for i in range(len(freq_baskets) - 1, 0, -1):
            for num in freq_baskets[i]:
                result.append(num)
                if len(result) == k:
                    return result