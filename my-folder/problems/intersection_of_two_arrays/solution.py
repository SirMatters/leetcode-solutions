class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f_set = set(nums1)
        res = set()

        for num in nums2:
            if num not in res and num in f_set:
                res.add(num)
        
        return list(res)